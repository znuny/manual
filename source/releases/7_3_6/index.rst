.. meta::
   :description: Znuny 7.3.6 release notes — security fix (CVE-2025-25977), new features, changes and bug fixes for this patchlevel release, released 19 August 2026.
   :keywords: znuny 7.3.6, znuny release notes, znuny changelog, 7.3.6 fixes, znuny patchlevel release, znuny update 7.3.6, znuny security fixes

Znuny 7.3.6
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 19-AUG-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel with security fixes                               |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.6.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_6>`_           |
+---------------------+--------------------------------------------------------------+

Features
********
- Added split Quote and Remove Quote buttons for CKEditor 5.

Changes & Improvements
**********************
- The REST transport module now keeps query parameters that don't contain placeholders.
- Cc and Bcc are now also set when only an article is created instead of sent in the generic interface operation ``TicketCreate``.

Security Fixes
**************
- **CVE-2025-25977:** Fixed a prototype pollution vulnerability in the bundled JavaScript library canvg by updating from version 1.5 to 4.0.3.

Bug Fixes
*********
- Fixed unnecessary whitespace in Baselink URLs in the TicketInformation templates for ``AgentTicketActionCommon`` and ``AgentTicketZoom``.
- Fixed article pagination being displayed incorrectly.
- Fixed ``CustomerSelector`` losing the customer key for numeric customer user logins, and added a new function to fully set new customer users in the ``CustomerSelector`` field.
- Fixed ``LinkTarget`` options not being marked as translatable. Thanks to `@urbalazs <https://github.com/urbalazs>`_ (Balázs Úr). (`PR#814 <https://github.com/znuny/Znuny/pull/814>`_)
- Fixed the migration follow-up step for removing mention flags from archived tickets being shown even when ``Ticket::ArchiveSystem`` is disabled.
- Removed unused leftover thirdparty directories ``jquery-ui-1.13.2`` and ``momentjs-2.29.4``.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_6/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_6>`_ for a list of all changes.
