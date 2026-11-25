.. meta::
   :description: Encrypt passwords in Znuny Kernel/Config.pm with AES-256 — generate a key, encrypt database, LDAP and RADIUS passwords and keep the key outside the config file.
   :keywords: znuny encrypted password, config.pm password, aes-256, Maint::Secret::Encrypt, Maint::Secret::KeyGenerate, ZNUNY_CONFIG_SECRET_KEY, ConfigSecretKeyFile, database password

.. _PageNavigation standardoperations_configsecrets_index:

Encrypted Configuration Secrets
###############################

.. versionadded:: 7.5.1

Some credentials must be read before the system configuration is available and therefore have to be stored in ``Kernel/Config.pm``, for example the database password. Instead of plain text, such values can be stored encrypted with AES-256 (GCM mode). A wrong key or a manipulated value is always detected.

An encrypted value looks like this:

.. code-block:: text

   {AES256:<base64 IV>:<base64 ciphertext and authentication tag>}

Values that are not wrapped in ``{AES256:...}`` are used unchanged, so encrypted and plain text values can be mixed.

Supported Settings
******************

- ``DatabasePw``
- ``Password`` in the ``Params`` of database backends for customer users and customer companies
- ``SearchUserPw`` of the LDAP backends for agent authentication, customer authentication and agent synchronization
- ``UserPw`` of the LDAP customer user backend
- ``Password`` (shared secret) of the RADIUS backends for agent and customer authentication

Requirements
************

The Perl module ``CryptX`` (provides ``Crypt::AuthEnc::GCM``) is required. It is not bundled with Znuny. Install it with the package manager of your distribution or with ``cpanm CryptX``. Check it with ``bin/znuny.CheckModules.pl --all``.

Setup
*****

A. Generate an encryption key.

   .. code-block:: bash

      su - znuny -c 'bin/znuny.Console.pl Maint::Secret::KeyGenerate'

#. Store the key so that it is available for the web server, the daemon, cron jobs and console commands. Do **not** store the key in ``Kernel/Config.pm``. Use one of these options:

   - The environment variable ``ZNUNY_CONFIG_SECRET_KEY``. It takes precedence over the key file.
   - A key file outside of the web root that contains only the key. Restrict access to the users that run Znuny, i.e. the web server user and the Znuny user (e.g. owner ``znuny``, group of the web server, permissions ``0640``). Add the path to ``Kernel/Config.pm``:

     .. code-block:: perl

        $Self->{ConfigSecretKeyFile} = '/etc/znuny/config_secret.key';

#. Encrypt the value.

   .. code-block:: bash

      su - znuny -c "bin/znuny.Console.pl Maint::Secret::Encrypt 'my-secret-password'"

#. Replace the plain text value in ``Kernel/Config.pm`` with the output, e.g.:

   .. code-block:: perl

      $Self->{DatabasePw} = '{AES256:...}';

.. important::

    An encrypted value can only be decrypted with the key that was used to encrypt it. Make sure the key is available on all systems that use the configuration, e.g. all nodes of a cluster, and keep a backup of the key separately from the configuration.

.. note::

    The encryption protects secrets at rest, e.g. if ``Kernel/Config.pm`` is committed to a version control system, contained in a backup or readable for someone without access to the key. It does not protect against an attacker who can read arbitrary files as the Znuny user, because this user needs access to the key at runtime.

.. note::

    The older command ``Maint::Database::PasswordCrypt`` is still available for backward compatibility. It only obfuscates the password with a fixed algorithm without a key and is not real encryption. Use ``Maint::Secret::Encrypt`` instead.
