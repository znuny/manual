Changes
#######


Improvements
************

- MailQueue send of the daemon now increases attempts before sending to avoid stalled processing if cases the process dies unexpectedly.
- Improved PostMaster attachment detection that caused slow processing of some emails.

Issues Fixed
************

- CSS fixes for the login screen.
- CKEditor: performance improvements and restored behavior when inserting links.
- Fixed setting default value for time units when using dropdown fields (`#464 <https://github.com/znuny/Znuny/issues/464>`_)
- Fixed the file list display in the package manager for installed add-ons.

Developer
*********

- No changes

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_15/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_15>`_ for a list of all changes.

