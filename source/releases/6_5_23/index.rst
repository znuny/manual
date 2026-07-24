Znuny LTS 6.5.23
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 22-JUL-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.23.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_23>`_          |
+---------------+--------------------------------------------------------------+


Security Vulnerabilities Fixed
******************************
- CVE-2026-6659: Fixed weak, predictable salt generation in bundled CPAN module Crypt::PasswdMD5 by updating from 1.40 to 1.44.
- CVE-2026-8368: Fixed exposure of Authorization and Proxy-Authorization headers on cross-origin redirects in bundled CPAN module LWP by updating from 6.53 to 6.83.


Bug Fixes
*********
- Fixed documentation links in config options. Thanks to `@bjinthahouse <https://github.com/bjinthahouse>`_ for reporting. (`#763 <https://github.com/znuny/Znuny/issues/763>`_)
- Fixed swapped sn and givenName default mapping in znuny.SyncLDAP2DB.pl. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG). (`PR#825 <https://github.com/znuny/Znuny/pull/825>`_)
- Fixed errors executing ticket search in AgentTicketService if the user has no queues or services assigned. Thanks to Paweł Bogusławski for reporting. (`#803 <https://github.com/znuny/Znuny/issues/803>`_)
- Fixed command Maint::Ticket::ArchiveCleanup not deleting article flags correctly. Thanks to `@parkingups69-netizen <https://github.com/parkingups69-netizen>`_ for reporting. (`#780 <https://github.com/znuny/Znuny/issues/780>`_)
- Fixed dialog to resend an email (AgentTicketEmailResend), which is now only usable for articles in channel Email with a previous transmission failure.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_23/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_23>`_ for a list of all changes.
