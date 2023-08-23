Overview
########

Welcome to Znuny LTS version 6.5.4

Security Vulnerabilities Fixed
******************************

- Preventing the possibility to inject JavaScript via the CustomerID and execution in the customer user admin module.

Improvements
************

- Updated bundled JavaScript libraries jQuery, jQuery UI, and Moment.js.
- Added the setting to configure default search for responsible.
- Changed default value for Frontend::Avatar and using https when connecting gravatar.com.
- Removal of all permissions during LDAP synchronization if the user is not a member of any group.

Issues Fixed
************

- Snippets in the rich text editor are now shown sorted by name.
- Remove orphaned mentions after deleting tickets.
- Fixed the Select All function in the Dynamic Fields Screen module.
- Fixed the prefilled subject in Activity dialogues to work for customer users too.
- Prevent using system addresses in phone tickets.
- Added the missing scrollbar in the popup windows when creating calendar appointments.


Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_4/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_4>`_ for a list of all changes.
