Znuny 7.0.18
############

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 29-MAY-2024                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.0.18.tar.gz>`_ |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_0_18>`_          |
+---------------------+--------------------------------------------------------------+

Changes
*******
- InnoDB is now the required storage engine when using MySQL or MariaDB.
- Integration of BugfixCustomerUserDBPasswordCryptType to allow different CryptType settings for each customer user backend.
- 2FA is now supported when using the Generic Interface (Provider). Thanks to Flávio Marta (`@CallMeFlanby <https://github.com/CallMeFlanby>`_). `#502 <https://github.com/znuny/Znuny/pull/502>`_

Fixed Issues
************
- Session are not terminated anymore when saving user preferences.
- Removed links without function from the system configuration.
- Smart tag replacement in the article subject process activity dialogs is now working.
- Fixed CSS class for sorted columns of dynamic fields in the customer portal.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_18/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_18>`_ for a list of all changes.
