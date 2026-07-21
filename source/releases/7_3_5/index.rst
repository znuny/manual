.. meta::
   :description: Znuny 7.3.5 release notes — security fixes (CVE-2026-6659, CVE-2026-8368), new features, changes and bug fixes for this patchlevel release, released 22 July 2026.
   :keywords: znuny 7.3.5, znuny release notes, znuny changelog, 7.3.5 fixes, znuny patchlevel release, znuny update 7.3.5, znuny security fixes

Znuny 7.3.5
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 22-JUL-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.5.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_5>`_           |
+---------------------+--------------------------------------------------------------+

Features
********
- Added delete-by-status option for the ``Maint::Log::CommunicationLog`` console command.

Changes & Improvements
**********************
- Margin around paragraphs is now smaller in RTE content and ticket details article preview.
- Password reset now sends a one-time link to change the password instead of a random password via email. Thanks to `@besendorf <https://github.com/besendorf>`_ for suggesting this feature. (`#56 <https://github.com/znuny/znuny-feature-requests/issues/56>`_)
- The "Out-of-office enabled" notification can now be dismissed for the remainder of the current session without being shown again.

Security Fixes
**************
- **CVE-2026-6659:** Fixed weak, predictable salt generation in bundled CPAN module Crypt::PasswdMD5 by updating from 1.40 to 1.44.
- **CVE-2026-8368:** Fixed exposure of Authorization and Proxy-Authorization headers on cross-origin redirects in bundled CPAN module LWP by updating from 6.53 to 6.83.
- Updated bundled nunjucks from 3.2.3 to 3.2.4.

Bug Fixes
*********
- Fixed submenus not visible in the customer interface.
- Fixed console root execution hint to suggest the detected application user instead of a hard-coded user.
- Fixed CKEditor full-screen mode not working after switching to full-screen 3 times. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG) for reporting. (`#747 <https://github.com/znuny/Znuny/issues/747>`_)
- Fixed erroneous green background color on ``.MainBox``. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG). (`PR#824 <https://github.com/znuny/Znuny/pull/824>`_)
- Fixed swapped ``sn`` and ``givenName`` default mapping in ``znuny.SyncLDAP2DB.pl``. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG). (`PR#825 <https://github.com/znuny/Znuny/pull/825>`_)
- Fixed main form width expanding over boundaries when the RTE line width is greater than the width of the RTE.
- Fixed agent ticket move dialog: the "create article" checkbox not being automatically enabled when the communication section is expanded.
- Fixed content overflow in the date picker when week numbers are shown.
- Fixed ticket being unnecessarily locked again when the owner stays the same in dialogs based on the AgentTicketActionCommon module.
- Fixed applying CKEditor width via the system configuration option ``Frontend::RichText::Settings###Width`` or module-specific options, e.g. ``Ticket::Frontend::AgentTicketEmail###RichTextWidth``.
- Fixed errors executing ticket search in AgentTicketService if the user has no queues or services assigned. Thanks to Paweł Bogusławski for reporting. (`#803 <https://github.com/znuny/Znuny/issues/803>`_)
- Fixed command ``Maint::Ticket::ArchiveCleanup`` not deleting article flags correctly. Thanks to `@parkingups69-netizen <https://github.com/parkingups69-netizen>`_ for reporting. (`#780 <https://github.com/znuny/Znuny/issues/780>`_)
- Fixed dialog to resend an email (AgentTicketEmailResend), which is now only usable for articles in channel Email with a previous transmission failure.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_5/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_5>`_ for a list of all changes.
