Changes
#######


Improvements
************

- Increased column size for standard templates and notification event messages (`#504 <https://github.com/znuny/Znuny/issues/504>`_).
- Added the optional parameter 'send-timeout' to the console command Maint::Email::MailQueue.
- Improved session handling when renaming an agent to prevent misleading error entries in the log files.

Issues Fixed
************

- Fixed Bug that prevented using customer user ids longer than 100 characters.
- Drafts are now working again as they should (`#507 <https://github.com/znuny/Znuny/issues/507>`_).
- SearchInArchive parameter is now taken into account for the toolbart fulltext search. Thanks to `Tim Püttmanns <https://github.com/tipue-dev>`_, maxence (`PR#479 <https://github.com/znuny/Znuny/pull/479>`_).

Developer
*********

- No changes.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_14/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_14>`_ for a list of all changes..

