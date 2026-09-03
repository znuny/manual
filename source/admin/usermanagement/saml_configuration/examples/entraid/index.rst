.. meta::
   :description: Configure Microsoft Entra ID as a SAML 2.0 Identity Provider for Znuny, from creating the Enterprise Application through a working Kernel/Config.pm.
   :keywords: znuny entra id saml, azure ad saml, entra id sso, enterprise application, saml identity provider

.. _PageNavigation admin_usermanagement_saml_configuration_examples_entraid_index:

Microsoft Entra ID
##################

This example walks through configuring Microsoft Entra ID (formerly Azure Active Directory) as a SAML 2.0 Identity Provider (IdP) for Znuny, using the native :ref:`Kernel::System::Auth::SAML backend <PageAdminSAMLConfigurationIndex>`. It requires **Znuny 7.3.1 or later**; earlier releases do not ship this backend.

Throughout this example, the Znuny instance is ``https://support.example.com/znuny/``. Replace it with your own URL wherever it appears.

Requirements
~~~~~~~~~~~~

* Administrator access to an Entra ID tenant.
* Administrator access to the target Znuny instance's ``Kernel/Config.pm``.
* A test agent (or customer) account in Entra ID to sign in with once configuration is complete.

.. note::

    The Entra admin portal's navigation changes frequently, but page names are more stable than the menu paths used to reach them. Use the **Search** box at the top of the portal and search for a page by name; results are grouped by category, and **Enterprise applications** appears under **Services**.

Create the Enterprise Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search for **Enterprise applications** and select **New application**, then **Create your own application**. Znuny is not in the application gallery, so select **Integrate any other application you don't find in the gallery (Non-gallery)** and name the application, for example ``Znuny - Agent SSO``.

.. tip::

    Use a separate enterprise application for agent and customer sign-in, each with its own user assignment. A single shared application gives every assigned user access to both interfaces.

Configure Single Sign-On
~~~~~~~~~~~~~~~~~~~~~~~~

Open **Single sign-on** on the application, choose **SAML**, and edit **Basic SAML Configuration**:

* **Identifier (Entity ID)**: ``https://support.example.com/znuny/``, must match ``AuthModule::SAML::Issuer1`` below, exactly.
* **Reply URL (Assertion Consumer Service URL)**: ``https://support.example.com/znuny/index.pl?Action=Login``, must match ``AuthModule::SAML::RequestAssertionConsumerURL1`` below, exactly.
* **Sign on URL**: optional for an SP-initiated login (the user starts at Znuny, not at Microsoft's application portal).
* **Relay State**: optional; Znuny's SAML backend does not require one for a standard login.
* **Logout URL**: leave empty. Znuny's SAML backend authenticates but does not implement Single Logout (SLO); there is no endpoint to receive a logout request.

Configure Attributes & Claims
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Entra ID populates a default set of claims using the ``http://schemas.xmlsoap.org/ws/2005/05/identity/claims/`` namespace (``givenname``, ``surname``, ``emailaddress``, ``name``). Znuny's SAML backend reads attributes by their exact claim name, so these default URIs work directly in ``UserSyncMap`` without renaming anything.

.. tip::

    Renaming claims to shorter names (``givenName``, ``sn``, ``mail``) is optional and purely cosmetic: only the label on the claim changes, not its value. Keep the Microsoft defaults unless an existing configuration elsewhere already depends on the shorter names.

Federation Metadata
~~~~~~~~~~~~~~~~~~~

On the same Single sign-on page, open **SAML Certificates** and copy the **App Federation Metadata Url**:

.. code-block::

    https://login.microsoftonline.com/<tenant-id>/federationmetadata/2007-06/federationmetadata.xml?appid=<application-id>

Point Znuny at this URL rather than pasting a certificate's contents directly. Entra ID rotates its signing certificate periodically; a URL always resolves to whatever is currently valid, while a copied certificate goes stale silently the next time Entra ID rotates.

Assign Users
~~~~~~~~~~~~

Under **Users and groups**, select **Add user/group** and assign a single test account. Entra ID blocks sign-in for anyone not explicitly assigned to the application, regardless of tenant membership.

.. tip::

    Assign one test user first and confirm the full flow before assigning a group or the whole organization.

Configure Znuny
~~~~~~~~~~~~~~~

Add the following to ``Kernel/Config.pm``, using the values collected above. See the :ref:`SAML configuration <PageAdminSAMLConfigurationIndex>` chapter for a full description of each setting.

.. code-block:: perl

    # --- Agent SAML Authentication ---
    $Self->{'AuthModule1'} = 'Kernel::System::Auth::SAML';
    $Self->{'AuthModule::SAML::RequestLoginButtonText1'} = 'Login with Microsoft Entra ID';

    $Self->{'AuthModule::SAML::RequestAssertionConsumerURL1'}
        = ( $Self->{HttpType} // '' ) . '://' . $Self->{FQDN} . '/' . $Self->{ScriptAlias} . 'index.pl?Action=Login';

    $Self->{'AuthModule::SAML::Issuer1'} = 'https://support.example.com/znuny/';

    $Self->{'AuthModule::SAML::RequestMetaDataURL1'}
        = 'https://login.microsoftonline.com/<tenant-id>/federationmetadata/2007-06/federationmetadata.xml?appid=<application-id>';

    # --- Agent Attribute Synchronization ---
    $Self->{'AuthSyncModule1'} = 'Kernel::System::Auth::Sync::SAML';

    $Self->{'AuthSyncModule::SAML::UserSyncMap1'} = {
        UserFirstname => 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname',
        UserLastname  => 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname',
        UserEmail     => 'http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress',
    };

    $Self->{'AuthSyncModule::SAML::UserSyncInitialGroups1'} = [
        'users',
    ];

.. warning::

    Keep at least one local (database) administrator account that does not depend on SAML. If Entra ID becomes unreachable or this configuration has a mistake, a SAML-only admin population has no way back in.

Validate and Test
~~~~~~~~~~~~~~~~~

Check the syntax of the edited file, then clear the cache and restart the web server:

.. code-block:: bash

    perl -cw -I . Kernel/Config.pm
    bin/znuny.Console.pl Maint::Cache::Delete

Open the agent login page and select the SAML login button. You should be redirected to Entra ID, prompted for credentials (and MFA, if required), and returned to the Znuny agent interface already signed in, with the test account's name and email populated from the synced claims.

Troubleshooting
~~~~~~~~~~~~~~~

**Entra ID reports a Reply URL (redirect URI) mismatch.**
Compare the Reply URL in Basic SAML Configuration against what ``AuthModule::SAML::RequestAssertionConsumerURL1`` actually computes to. They must match exactly, including any trailing slash.

**Authentication succeeds at Entra ID, but Znuny shows an error afterward.**
Confirm the Znuny server can reach the metadata URL outbound; it is fetched directly by the server, not through the user's browser:

.. code-block:: bash

    curl -I 'https://login.microsoftonline.com/<tenant-id>/federationmetadata/2007-06/federationmetadata.xml?appid=<application-id>'

**Login succeeds, but the agent's name or email is missing.**
Compare the claim names actually sent by Entra ID (a SAML tracer browser extension shows the raw assertion) against ``AuthSyncModule::SAML::UserSyncMap1``. If claims were renamed in Attributes & Claims, the mapped names must be updated to match.

Customer Authentication
~~~~~~~~~~~~~~~~~~~~~~~

Customer sign-in through ``customer.pl`` follows the same process against a second, separate enterprise application: a Reply URL of ``https://support.example.com/znuny/customer.pl?Action=Login``, and the ``Customer::AuthModule::SAML::*`` settings documented in the :ref:`SAML configuration <PageAdminSAMLConfigurationIndex>` chapter in place of ``AuthModule::SAML::*``.
