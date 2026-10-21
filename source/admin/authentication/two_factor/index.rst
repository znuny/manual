.. meta::
   :description: Set up TOTP two-factor authentication for Znuny agents and customer users with Google Authenticator, Microsoft Authenticator, FreeOTP, Aegis or any RFC 6238 compliant app.
   :keywords: two-factor authentication, totp, znuny 2fa, google authenticator, rfc 6238, shared secret, login security, authenticator app

.. _PageNavigation admin_authentication_two_factor_index:

Two-Factor Authentication
#########################

Znuny can ask for a six-digit code from an authenticator app in addition to the password. This uses Time-based One-Time Passwords (TOTP). Any app that follows `RFC 6238 <https://www.rfc-editor.org/info/rfc6238>`_ works, for example:

- Google Authenticator
- Microsoft Authenticator
- FreeOTP
- Aegis

The module is called GoogleAuthenticator, but it is not tied to that app.

This page sets up two-factor authentication for agents in five steps. The same steps work for the customer interface, see :ref:`2fa_customer_interface`.

All settings are in **Admin -> System Configuration**.

Before You Start
****************

- Keep one admin account without two-factor authentication until you have tested everything, so a mistake cannot lock you out.
- The server clock must be correct. Codes are time-based and change every 30 seconds. Check that NTP is running on the Znuny server.

Step 1: Enable the Two-Factor Module
************************************

1. Navigate to **Admin -> System Configuration** and search for ``AuthTwoFactorModule``.
2. Edit the setting ``AuthTwoFactorModule``.
3. Keep the value ``Kernel::System::Auth::TwoFactor::GoogleAuthenticator``, tick **Enabled** and save.
4. Deploy the change.

The agent login page now shows an additional field, **2 Factor Token**.

.. note::

   Do not change ``AuthTwoFactorModule::SecretPreferencesKey``. Its default ``UserGoogleAuthenticatorSecretKey`` must match the preference used in step 2.

Step 2: Let Agents Enter Their Own Secret
*****************************************

By default only an admin can store an agent's secret. To let agents do it themselves in their personal preferences:

1. Search for ``PreferencesGroups###GoogleAuthenticatorSecretKey``.
2. Change **Active** from ``0`` to ``1`` and save.
3. Deploy the change.

Agents now see a **Google Authenticator** box with a **Shared Secret** field under **Personal Preferences -> User Profile**.

If you skip this step, an admin enters the secret for each agent under **Admin -> Agents -> (agent)**.

Step 3: Create a Shared Secret
******************************

Each agent needs their own secret. Znuny accepts exactly 16 characters, using only uppercase letters ``A`` to ``Z`` and digits ``2`` to ``7``. The result looks like ``JBSWY3DPEHPK3PXP``. Treat it like a password.

Agents
   Open **Personal Preferences -> User Profile**. Next to the **Shared Secret** field is a **Generate** button. Click it and Znuny fills in a new secret. It is not saved yet, that happens in step 4.

Admins and Customer Users
   The **Generate** button only appears in the agent's own preferences (step 2). It is not available in **Admin -> Agents** or in the customer interface. An admin who enters secrets for others, or a customer user, creates one with one of the following commands instead. All of them run offline.

Linux, macOS, or Git Bash on Windows:

.. code-block:: bash

   head -c 10 /dev/urandom | base32

Any system with Python, including Windows:

.. code-block:: bash

   python -c "import base64,os; print(base64.b32encode(os.urandom(10)).decode())"

Windows PowerShell, no extra tools needed:

.. code-block:: powershell

   $b = New-Object byte[] 16; [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($b); -join ($b | ForEach-Object { 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'[$_ % 32] })

.. warning::

   Do not use a website to generate the secret. The site could keep a copy, and anyone who has the secret can create valid codes.

Step 4: Connect the Authenticator App, Then Save in Znuny
*********************************************************

The order matters. Set up the app first and save in Znuny last, so you can log in again afterwards.

1. Copy the secret from step 3.
2. In the authenticator app, choose **Add account** and then **Enter a setup key** (the wording varies by app).
3. Account name: anything, for example ``Znuny (jdoe)``.
4. Key: the 16-character secret.
5. Type: **Time-based**.
6. Check that the app now shows a six-digit code that changes every 30 seconds.
7. In Znuny, make sure the same secret is in **Personal Preferences -> User Profile -> Shared Secret**, and save.

Step 5: Test the Login
**********************

1. Log out.
2. Log in with user name, password and the current code from the app in **2 Factor Token**.
3. If the login fails, check the server time first, then check that the secret in the app and in Znuny are identical.

Make Two-Factor Authentication Mandatory
****************************************

As long as ``AuthTwoFactorModule::AllowEmptySecret`` is enabled (the default), agents without a secret log in with just their password. To require two-factor authentication for everyone:

1. Make sure every agent, including your admins, has a secret stored and has tested their login.
2. Search for ``AuthTwoFactorModule::AllowEmptySecret``, untick the checkbox, save and deploy.

Agents without a secret can no longer log in.

Other Settings
**************

``AuthTwoFactorModule::AllowPreviousToken``
   Enabled by default. Also accepts the code from the previous 30 seconds, which helps users who need a little more time to type it. Untick it for slightly stricter security.

Lost Device
***********

If an agent loses their phone, an admin opens **Admin -> Agents**, selects the agent, clears the **Shared Secret** field and saves. If empty secrets are allowed, the agent can log in with the password again and repeat steps 3 and 4. If two-factor authentication is mandatory, the admin enters a new secret for the agent and hands it over securely.

.. _2fa_customer_interface:

Customer Interface
******************

Customer users work the same way. Use the settings with the ``Customer::`` prefix:

.. list-table::
   :header-rows: 1

   * - Agents
     - Customer users
   * - ``AuthTwoFactorModule``
     - ``Customer::AuthTwoFactorModule``
   * - ``AuthTwoFactorModule::AllowEmptySecret``
     - ``Customer::AuthTwoFactorModule::AllowEmptySecret``
   * - ``AuthTwoFactorModule::AllowPreviousToken``
     - ``Customer::AuthTwoFactorModule::AllowPreviousToken``
   * - ``PreferencesGroups###GoogleAuthenticatorSecretKey``
     - ``CustomerPreferencesGroups###GoogleAuthenticatorSecretKey``

Once **Active** is set to ``1``, customer users find the **Shared Secret** field in the **Miscellaneous** section of their preferences in the customer interface.

Web Service Logins
******************

If you use the REST web service with sessions (``SessionCreate``), send the current code as ``TwoFactorToken`` together with the user name and password. See :ref:`PageNavigation admin_webservices_provider_index`.

.. seealso::

   :ref:`Personal Settings <PageNavigation agentinterface_personalsettings_index>`
