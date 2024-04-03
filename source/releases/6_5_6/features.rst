Overview
########

Welcome to Znuny LTS version 6.5.6

Improvements
************

- MailQueue send of the daemon now increases attempts before sending to avoid stalled processing if cases the process dies unexpectedly.
- Improved PostMaster attachment detection that caused slow processing of some emails.

Issues Fixed
************

- CKEditor: performance improvements and restored behavior when inserting links.
- Fixed setting default value for time units when using dropdown fields (`#464 <https://github.com/znuny/Znuny/issues/464>`_).
- Fixed rich text editor's field height problems by disabling CKEditor's autogrow plugin. Thanks to Paweł Bogusławski (@pboguslawski) (`#526 <https://github.com/znuny/Znuny/pull/526>`_).


Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_6/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_6>`_ for a list of all changes.
