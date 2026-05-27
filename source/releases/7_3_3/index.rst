.. meta::
   :description: Znuny 7.3.3 release notes — security fixes (CVE-2025-26843, CVE-2025-59490), download links, changes and bug fixes for this patchlevel release, released 27 May 2026.
   :keywords: znuny 7.3.3, znuny release notes, znuny changelog, 7.3.3 fixes, znuny patchlevel release, znuny update 7.3.3, znuny security fixes

Znuny 7.3.3
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 27-MAY-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.3.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_3>`_           |
+---------------------+--------------------------------------------------------------+

Security Fixes
**************
- **CVE-2025-26843:** Fixed infinite loop when replacing tags in the template generator.
- **CVE-2025-59490:** Follow-up fix for scrambled script tags.
- Fixed XSS via JavaScript in URL parameters in the communication log admin view.
- Fixed XSS in user preferences DB.

Changes & Improvements
**********************
- Updated CKEditor 5 to version 48.0.0.
- Extended ``Calendar::GetTextColor`` to support RGBA hex values and fixed ``#RGB`` blue parsing. Thanks to `@LuBroering <https://github.com/LuBroering>`_, Sector Nord AG. (`#786 <https://github.com/znuny/Znuny/issues/786>`_)
- Changed the name of the user with ID 1.
- Removed support for IIS 6. Znuny does not officially support IIS 6.0.

Bug Fixes
*********
- Fixed: Package manager does not use the user ID for package operations.
- Fixed: Deployment of custom translations during migration.
- Fixed: Default RTE label "Rich Text Editor" is shown in some dialogs in addition to the intended field label.
- Fixed: Added missing primary key for database table ``pm_process_preferences``.
- Fixed: Use of the letter "O" instead of the digit "0" in hex color values. Thanks to `@LuBroering <https://github.com/LuBroering>`_, Sector Nord AG. (`#790 <https://github.com/znuny/Znuny/issues/790>`_)
- Fixed: Missing whitespace between HTML attributes results in invalid markup. Thanks to `@LuBroering <https://github.com/LuBroering>`_, Sector Nord AG. (`#792 <https://github.com/znuny/Znuny/issues/792>`_)
- Fixed: Email security option cannot be removed manually in the compose dialog when the queue has a default signing key configured. Thanks for reporting to `@LSI-BassdScho <https://github.com/LSI-BassdScho>`_. (`#766 <https://github.com/znuny/Znuny/issues/766>`_)
- Fixed: Archiving tickets removes flags for mentions and "seen".

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_3/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_3>`_ for a list of all changes.
