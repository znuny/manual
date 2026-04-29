Znuny LTS 6.5.20
################

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 29-APR-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-6.5.20.tar.gz>`_ |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-6_5_20>`_          |
+---------------------+--------------------------------------------------------------+


Features
********
- Added EmailSecurity section from Article to GenericInterface. Thanks to `@DonMarlowne <https://github.com/DonMarlowne>`_. (`PR#612 <https://github.com/znuny/Znuny/pull/612>`_)
- PostMaster/Filter/ExternalTicketNumberRecognition: Added support of the SysConfig setting "Ticket::SubjectFormat".

Changes & Improvements
**********************
- Ticket list views for "escalation", "locked", "mention", "owner", "responsible", "status" and "watch" now each have a config option TicketSearchWithAdminUser to decide if the tickets will be searched with admin user or the logged in user.
- Changed log level of "missing user" message in HTTP basic auth.

Bug Fixes
*********
- Fixed sorting in ticket overview modes "Medium" and "Preview" throws an error. Thanks for reporting to `@przemekrzyzanski-cmyk <https://github.com/przemekrzyzanski-cmyk>`_. (`#779 <https://github.com/znuny/Znuny/issues/779>`_)
- Fixed AgentTicketOwnerView missing in dynamic field screen selection.
- Fixed iFrame elements reuse the same ID in CustomerTicketZoom.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_20/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_20>`_ for a list of all changes.
