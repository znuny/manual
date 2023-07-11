Two-Factor Authentication
#########################
.. _PageNavigation admin_authentication_two_factor_index:

The framework supports 2FA or two-factor authentication by providing for the use of Time-based One-Time Passwords (TOTP). This requires the user to use an authenticator app. This can be:

- Google authenticator
- Microsoft authenticator
- 1Password
- Sophos Authenticator
- and many more

2FA Setup
*********

To activate this, you must go to the system configuaration in the administrator area, and navigate to **Core⇾Auth⇾(Agent or Customer)⇾TwoFactor**. The module is called GoogleAuthenticator, but complies to `RFC 6238 <https://www.rfc-editor.org/rfc/rfc6238>`_ and works with compliant software token generators.

Once activated, unless your administrator should manually generate the shared secret for the users, navigate to **Frontend⇾Agent⇾View⇾Preferences** and enable the preference module. Do this in ``PreferencesGroups###GoogleAuthenticatorSecretKey`` by setting it to **Active => 1**.

To allow customers to generate their own secret, navigate to **Frontend⇾Agent⇾View⇾Preferences** and set ``CustomerPreferencesGroups###GoogleAuthenticatorSecretKey`` to **Active => 1**.

Additional settings are:

AllowEmptySecret
  Allow users to not use 2FA.
AllowPreviousToken
  Grant a 30-second grace period on the token and allow the last and current token to be accepted.

.. seealso::

  :ref:`Personal Settings <PageNavigation agentinterface_personalsettings_index>` 
