.. meta::
   :description: Znuny 7.3.7 release notes — security fixes (CVE-2026-48188 and more), changes and bug fixes for this patchlevel release, released 16 September 2026.
   :keywords: znuny 7.3.7, znuny release notes, znuny changelog, 7.3.7 fixes, znuny patchlevel release, znuny update 7.3.7, znuny security fixes

Znuny 7.3.7
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 16-SEP-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel with security fixes                               |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.7.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_7>`_           |
+---------------------+--------------------------------------------------------------+

Changes & Improvements
**********************
- ``Kernel::SystemAddress::SystemAddressLookup`` is now case-insensitive when comparing system addresses.
- Enabled linking images (LinkImage plugin) in CKEditor 5.
- ``Admin::Package::List`` now always reports the package deployment status and warns about local modifications.

Security Fixes
**************
- **CVE-2026-48188:** Fixed a possible SQL injection vulnerability in the agent login.
- Fixed an SQL injection vulnerability via the ``ContentSearch`` parameter of the ticket search. Thanks for reporting to Mokrane ABDELMALEK (via the Ghent University VDP programme).
- Fixed an unauthenticated login vulnerability via the generic interface when combined with HTTP basic auth and a request header containing the username (``REMOTE_USER`` in the HTTP header). Thanks for reporting to Mokrane ABDELMALEK (via the Ghent University VDP programme).
- Updated the JavaScript library nunjucks from version 3.2.3 to 3.2.4.

Bug Fixes
*********
- Fixed a warning thrown by the ticket event storing customer company data in dynamic fields when the ticket had no customer ID set.
- Fixed accounted time (time units) being lost when working with drafts.
- Fixed content type and attachment keys leaking into transition action modules (e.g. ``DynamicFieldSet``) that treat every config key as a dynamic field name, causing the transition action to fail.
- Fixed custom translations containing Perl sigils leading to syntax errors.
- Fixed process management: the scope entity ID selection remained visible when the scope was set to global.
- Fixed multiselect column filters being lost when paginating dashboard ticket widgets. Thanks to `@ghost-train1 <https://github.com/ghost-train1>`_ for reporting. (`#832 <https://github.com/znuny/Znuny/issues/832>`_)
- Fixed ticket search "Newer/Older" Date and Minutes filters no longer matching tickets that fall exactly on the given time. Thanks to `@martinpintar-pixel <https://github.com/martinpintar-pixel>`_ for reporting. (`#840 <https://github.com/znuny/Znuny/issues/840>`_)
- Fixed plain text conversion breaking in several ways after the upgrade to CKEditor 5.
- Fixed multiselect dynamic field values being rendered without proper spacing in the customer interface. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG). (`PR#836 <https://github.com/znuny/Znuny/pull/836>`_)
- Fixed agent/customer redirection after accepting the initial information dialog (``AgentInfo``/``CustomerAccept``).
- Fixed some ticket attributes not being properly inserted into ``OTRS_TICKET_*`` placeholders.
- Fixed clearing multiselect column filters in agent ticket overview screens and dashboard ticket widgets not removing the filter.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_7/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_7>`_ for a list of all changes.
