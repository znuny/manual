Znuny 7.3.2
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 29-APR-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.2.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_2>`_           |
+---------------------+--------------------------------------------------------------+


Features
********
- Added EmailSecurity section from Article to GenericInterface. Thanks to `@DonMarlowne <https://github.com/DonMarlowne>`_. (`PR#612 <https://github.com/znuny/Znuny/pull/612>`_)
- PostMaster/Filter/ExternalTicketNumberRecognition: Added support of the SysConfig setting "Ticket::SubjectFormat".
- Added a link to CUIC to edit customer user ``AgentCustomerUserInformationCenter::MainMenu###010-EditCustomerUser``.

Changes & Improvements
**********************
- Renamed system configuration definition for Daemon::Log::RotationType to Znuny.
- Ticket list views for "escalation", "locked", "mention", "owner", "responsible", "status" and "watch" now each have a config option TicketSearchWithAdminUser to decide if the tickets will be searched with admin user or the logged in user.
- Changed log level of "missing user" message in HTTP basic auth.
- AgentTicketMerge: Card "Inform Sender" will initially be shown collapsed and disabled. Will be enabled automatically when user expands the card.

Bug Fixes
*********
- Fixed process management: Field help tooltip not fully visible for long descriptions.
- Fixed field order in "ticket data" card.
- Fixed link text does not fit button size in dialog AdminGenericInterfaceTransportHTTPREST.
- Fixed sorting in ticket overview modes "Medium" and "Preview" throws an error. Thanks for reporting to `@przemekrzyzanski-cmyk <https://github.com/przemekrzyzanski-cmyk>`_. (`#779 <https://github.com/znuny/Znuny/issues/779>`_)
- Fixed dashboard queue column filter offers inaccessible queues. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting the issue. (`#603 <https://github.com/znuny/Znuny/issues/603>`_)
- Fixed: StandardTemplates are not usable in AgentTicketEmailOutbound, AgentTicketPhoneOutbound and AgentTicketPhoneInbound (TicketPhoneCommon). Thanks for reporting to `@AVONON-DST <https://github.com/AVONON-DST>`_ (Dennis). (`#776 <https://github.com/znuny/Znuny/issues/776>`_)
- Fixed visibility of dynamic fields in some views.
- Fixed broken file list for non-installed packages. Thanks for reporting to `@urbalazs <https://github.com/urbalazs>`_ (Balázs Úr). (`#771 <https://github.com/znuny/Znuny/issues/771>`_)
- Fixed: Template selection in agent ticket details view (AgentTicketZoom) does not open when clicking "Reply" or "Reply All".
- Fixed missing email security options in dialog for new email ticket (AgentTicketEmail).
- Fixed AgentTicketOwnerView missing in dynamic field screen selection.
- Fixed iFrame elements reuse the same ID in CustomerTicketZoom.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_2/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_2>`_ for a list of all changes.
