Znuny LTS 6.5.9
###############

**Release Information:**

+--------------+-------------------------------------------------------------+
| Release Date | 26-JUN-2024                                                 |
+--------------+-------------------------------------------------------------+
| Release Type | Patchlevel                                                  |
+--------------+-------------------------------------------------------------+
| Download     | `<https://download.znuny.org/releases/znuny-6.5.9.tar.gz>`_ |
+--------------+-------------------------------------------------------------+
| GitHub       | `<https://github.com/znuny/Znuny/tree/rel-6_5_9>`_          |
+--------------+-------------------------------------------------------------+

Changes
*******
- The invoker Ticket::Generic provides the date and time parts of UntilTime.
- A new console command exports the modified system configuration settings.
- Integration of BugfixCustomerUserDBPasswordCryptType to allow different CryptType settings for each customer user backend.
- 2FA is now supported when using the Generic Interface (Provider). Thanks to Flávio Marta (`@CallMeFlanby <https://github.com/CallMeFlanby>`_). `#502 <https://github.com/znuny/Znuny/pull/502>`_

Fixed Issues
************
- The AdminSystemFiles modules now work correctly when the application directory is a symbolic link.
- Improved regular expression to reduce long parsing times on complex emails.
- Fixed session handling while saving user preferences. `#559 <https://github.com/znuny/Znuny/issues/559>`_
- Fixed value used for owner lookup in AgentTicketProcess. Thanks to Falko Saller (`@falkos <https://github.com/falkos>`_). `#556 <https://github.com/znuny/Znuny/pull/556>`_
- Removed links to unsupported functions in the system configuration.
- Smart tags in article subjects in the process management are now correctly replaced.
- Fixed CSS class for sorted columns of dynamic fields in the customer portal.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_9/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_9>`_ for a list of all changes.