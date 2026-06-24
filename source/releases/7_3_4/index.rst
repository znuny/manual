.. meta::
   :description: Znuny 7.3.4 release notes — new features (multiselect column filters, extended generic interface invoker), improvements and bug fixes for this patchlevel release, released 24 June 2026.
   :keywords: znuny 7.3.4, znuny release notes, znuny changelog, 7.3.4 fixes, znuny patchlevel release, znuny update 7.3.4

Znuny 7.3.4
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 24-JUN-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.4.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_4>`_           |
+---------------------+--------------------------------------------------------------+

Features
********
- Added multiselect column filters for agent ticket overview screens and dashboard ticket widgets.
- Extended generic interface invoker configuration with configurable fields (per invoker) that will be omitted and/or encoded as Base64.
- Added confirmation dialog when database entries of packages are to be deleted on uninstallation.
- Agent and customer error pages now show a configurable link for the next action.

Changes & Improvements
**********************
- Updated bundled CPAN module Devel::StackTrace to 2.05.

Bug Fixes
*********
- Fixed sorting by dynamic field columns in dashboard ticket widgets falling back to age; process tickets without articles could be hidden. Thanks to `@sergiykhan <https://github.com/sergiykhan>`_ for reporting. (`#811 <https://github.com/znuny/Znuny/issues/811>`_)
- Fixed process tickets without articles not being displayed in the dashboard widget "Running Process Tickets".
- Fixed system configuration hash key duplication for keys containing ###. Thanks to `@FloFaber <https://github.com/FloFaber>`_ (Flo Faber) for reporting. (`#789 <https://github.com/znuny/Znuny/issues/789>`_)
- Fixed missing translation in date picker week header. Thanks to `@urbalazs <https://github.com/urbalazs>`_ (Balázs Úr) for reporting.
- Fixed issue with mentioning out-of-office users via group mention.
- Fixed column filter dropdowns in ticket overviews showing entries for ticket attributes marked as invalid.
- Fixed missing translation in AdminTranslation screen. Thanks to `@urbalazs <https://github.com/urbalazs>`_ (Balázs Úr). (`PR#800 <https://github.com/znuny/Znuny/pull/800>`_)
- Fixed search via search toolbar not being executable with a mouse click.
- Fixed notification about changed system configuration in dialog AdminSystemConfiguration.
- Fixed attachments being assignable to Snippet templates in AdminTemplateAttachment.
- Fixed copy ticket number icon missing when Ticket::Hook is customized. Thanks to `@mamojdick <https://github.com/mamojdick>`_ for reporting. (`#805 <https://github.com/znuny/Znuny/issues/805>`_)
- Fixed configured limit for activities not being applied correctly.
- Fixed context menu for editing tables in RTE not being visible in fullscreen mode.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_4/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_4>`_ for a list of all changes.
