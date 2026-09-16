Znuny LTS 6.5.25
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 16-SEP-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.25.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_25>`_          |
+---------------+--------------------------------------------------------------+


Changes & Improvements
**********************
- ``Kernel::SystemAddress::SystemAddressLookup`` is now case-insensitive when comparing system addresses.

Security Fixes
**************
- **CVE-2026-48188:** Fixed a possible SQL injection vulnerability in the agent login.
- Fixed an SQL injection vulnerability via the ``ContentSearch`` parameter of the ticket search. Thanks for reporting to Mokrane ABDELMALEK (via the Ghent University VDP programme).
- Fixed an unauthenticated login vulnerability via the generic interface when combined with HTTP basic auth and a request header containing the username (``REMOTE_USER`` in the HTTP header). Thanks for reporting to Mokrane ABDELMALEK (via the Ghent University VDP programme).
- Updated the JavaScript library nunjucks from version 3.2.3 to 3.2.4.

Bug Fixes
*********
- Fixed a warning thrown by the ticket event storing customer company data in dynamic fields when the ticket had no customer ID set.
- Fixed ticket search "Newer/Older" Date and Minutes filters no longer matching tickets that fall exactly on the given time. Thanks to `@martinpintar-pixel <https://github.com/martinpintar-pixel>`_ for reporting. (`#840 <https://github.com/znuny/Znuny/issues/840>`_)
- Fixed content type and attachment keys leaking into transition action modules (e.g. ``DynamicFieldSet``) that treat every config key as a dynamic field name, causing the transition action to fail.
- Fixed agent/customer redirection after accepting the initial information dialog (``AgentInfo``/``CustomerAccept``).
- Fixed some ticket attributes not being properly inserted into ``OTRS_TICKET_*`` placeholders.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_25/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_25>`_ for a list of all changes.
