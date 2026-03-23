Znuny 7.3.1
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 25-MAR-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Minor version release                                        |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.1.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_1>`_           |
+---------------------+--------------------------------------------------------------+

Security Fixes
**************
- **CVE-2025-52204:** Fixed XSS issue with session ID in URL parameter. Thanks to Miguel P. for reporting.
- **CVE-2025-59490:** Fixed XSS issue with unfiltered URL parameters given to backend.
- Fixed: For security reasons, detailed error messages are no longer shown in the GUI.
- Fixed: Improved content security policy HTTP header.
- Fixed: Source view for rich text editor deactivated in customer frontend to prevent arbitrary code injection.

Features
********
- Added support for **SAML authentication**.
- Added new **GUI redesign**. Thanks to Tim Binder, stbt.de.
- Integrated package **Znuny-AdditionalTicketAttributeSelection**.
- Integrated package **Znuny-AgentTicketActionCommonCustomer**.
- Integrated package **Znuny-CopyTicketNumber**.
- Integrated package **Znuny-MultiSendmail**.
- Added **Znuny XSLT helper** and updated mappings to use it.
- Added **Sender column** support for dashboard ticket widgets.
- Added **download** function to AttachmentList.
- Added **AgentSession module** to store ``UserClosedMessages`` in the current UserSession (AuthSession).
- Added wildcard ``*`` support to system configuration setting search.
- Added new **ToolBarModule** ``161-Ticket::AgentTicketProcessCategory``.
- Added **configurable filter** for ticket search to the ticket merge dialog (AgentTicketMerge).
- Added **'Prio' parameter** to AgentTicketZoom MenuModules for individual sorting. Thanks to `@itweserems <https://github.com/itweserems>`_. (`#646 <https://github.com/znuny/Znuny/issues/646>`_, `PR#647 <https://github.com/znuny/Znuny/pull/647>`_)
- **AdminSystemConfiguration:** Added "Quick Deploy" in SysConfig to apply pending changes faster.
- Added ``NotificationEmailDefaultTemplate`` option to system configuration. Thanks to Paweł Bogusławski (`@pboguslawski <https://github.com/pboguslawski>`_) (`PR#382 <https://github.com/znuny/Znuny/pull/382>`_).
- Added parameter ``FormID`` to AJAX requests of autocompletion modules (needed for inserting FAQ entries with inline images into RTE via autocompletion).
- **PostMaster:** Added ability to assign multiselect dynamic fields. Thanks to Christian Ullrich (`@chrullrich <https://github.com/chrullrich>`_) (`PR#699 <https://github.com/znuny/Znuny/pull/699>`_).
- **Sector Nord AG:** ArticleRender — Added title to ArticleFields for MIMEBase. Thanks to `@LuBroering <https://github.com/LuBroering>`_. (`PR#577 <https://github.com/znuny/Znuny/pull/577>`_)

Changes
*******
- **Changed:** Reply function in the agent ticket compose dialog is no longer available if the article is internal and was created by an agent or by the system.
- **Changed:** Mentions feature now only triggers if the symbol before the trigger character does not exist or is a space — prevents selection options from appearing while typing an email address. Thanks to `@Dherlou <https://github.com/Dherlou>`_. (`#738 <https://github.com/znuny/Znuny/issues/738>`_)
- Changed ticket zoom information widget to count only open tickets with the same customer when ``Ticket::Frontend::ZoomCustomerTickets`` is enabled.
- Number of stored activities per user is now limited for performance reasons. User activities are now loaded asynchronously.
- Increased length of the password column for ``users``, ``customer_user``, and ``mail_account``.
- Improved commandline parameter parsing in ``Admin::Article::StorageSwitch`` console command.
- Improved handling of read-only fields for ``CustomerUser::DB`` and ``CustomerCompany::DB`` backends.
- Improved date formatting at the language level.
- Sped up UUID creation for DBCRUD modules.
- ``Admin::Package::RepositoryList`` console command now indicates which displayed packages are installed.
- Migration refactoring: Added new ``FollowUp`` component. Migration order: CheckPreviousRequirement → Run → FollowUp.
- Updated jscolor third-party library to 2.5.2; altered database table ``calendar`` and ``article_color`` column ``color`` size to 25.
- Fixed: AgentTicketCompose Ajax error. Fixed TimeUnits position in AgentTicketCompose.

Fixed Issues
************
- Fixed: Misaligned column filter dropdowns in TableSmall views.
- Fixed: Activities are not marked as seen after clicking an activity entry.
- Fixed: Form submit not triggered when pressing Enter after entering a new draft's title.
- Fixed: Misleading popup message when opening more than one ticket from overviews using a shortcut to open in a new tab/window.
- Fixed: Invisible ticket pagination count when there is only one page.
- Fixed: Text in the dashboard dropdown menu overlaid by other text in mobile mode.
- Fixed: Missing locale sensitivity in VacationDay config type.
- Fixed: Problems with leftover UTF-16 surrogates in incoming UTF-8 text.
- Fixed: Issue with sorting dropdown elements when ``Ticket::Frontend::AccountTimeType`` is set to Dropdown.
- Fixed: Console commands ``Admin::Group::UserLink`` and ``Admin::Group::RoleLink`` with inconsistent available permissions. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_. (`#756 <https://github.com/znuny/Znuny/issues/756>`_)
- Fixed: Sender address for process tickets not assigned properly in the customer interface.
- Fixed: Attachment dialog displays a preview for non-presentable items; removed ``application/octet-stream``.
- Fixed: Restored breadcrumb rendering on the AdminTicketAttributeRelations Edit and Add views.
- Fixed: SLA cache now clears after service assignments change so data stays current. Thanks to `@dkmonaghan <https://github.com/dkmonaghan>`_. (`#643 <https://github.com/znuny/Znuny/issues/643>`_)
- Fixed: Various issues after GUI redesign — added widget functions to AgentTicketActionCommon, fixed unlock notification, added ``UndoClosePopup`` class, changed "Unlock and close popup" button.
- Fixed: Znuny redirects after login to the default view even when an ``ExternalURL`` parameter with an ``Action`` is encoded in the link.
- Fixed: Process ticket submission validates the Responsible field client-side.
- Fixed: URL parameters were not used to pre-fill new email and phone ticket forms.
- Fixed: The tags ``<OTRS_TICKET>`` and ``<OTRS_MERGE_TO_TICKET>`` could only be used once in ``Ticket::Frontend::AutomaticMergeText`` due to missing 'global' flag. Thanks to Tim Püttmanns (`@tipue-dev <https://github.com/tipue-dev>`_), maxence. (`PR#753 <https://github.com/znuny/Znuny/pull/753>`_)
- Fixed: Customer interface ``PopupClose`` function loaded agent interface header/footer, referencing unsupported features. Added ``CustomerPopupClose`` function.
- Fixed: Missing translation for 'last-search' in ToolBar/TicketSearchProfile.
- Fixed: Date check regex for config option ``ICSParser::StartDate`` now actually matches ``YYYYMMDD``.
- Fixed: Dynamic field labels were capitalized via CSS in AgentTicketProcess.
- Fixed: In certain settings, only greyscale could be selected in the color picker.
- Fixed: Wrong Subaction for TranslationDeployment in AdminTranslation. Thanks to `@LuBroering <https://github.com/LuBroering>`_, Sector Nord AG. (`PR#741 <https://github.com/znuny/Znuny/pull/741>`_)
- Fixed: Typo in ``--regenerate`` command option in ``Dev/Tools/TranslationsUpdate``. Thanks to `@urbalazs <https://github.com/urbalazs>`_. (`PR#751 <https://github.com/znuny/Znuny/pull/751>`_)
- Fixed: Issue with cache applied incorrectly to "My last changed tickets" widget.
- Fixed: Article overview text difficult to read in Dark Skin due to double filter inversion.
- Fixed: MariaDB/MySQL error regarding foreign keys when converting character set of tables to UTF8MB4.
- Fixed: Wrong description text in personal preference. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_. (`#712 <https://github.com/znuny/Znuny/issues/712>`_)
- Fixed: Resource module displays deactivated agents.
- Fixed: Checkbox in AgentTicketActionCommon views did not collapse the article widget after enabling.
- Fixed: Firefox browser did not wrap overflow text in article content in AgentTicketZoom.
- Fixed: Unexpected rate limit applied when ``SendmailModule::RateLimit`` is disabled.
- Fixed: ``CustomerShortcutIconCustom`` config not working. Thanks to Daylton Rodrigues (`@dayltonr <https://github.com/dayltonr>`_). (`#737 <https://github.com/znuny/Znuny/issues/737>`_)
- Fixed: Images in articles inverted in Dark Skin. Thanks to `@Vocta1310 <https://github.com/Vocta1310>`_. (`#724 <https://github.com/znuny/Znuny/issues/724>`_)
- Fixed: No styles when printing process in the admin interface.
- Fixed: Customer ticket details screen now redirects to the ticket overview if accessed without permissions.
- Fixed: The link to a specific article in a ticket did not work if users have different "Show all articles" settings. Article links now handle both display modes.
- Fixed: ProcessPrint produced empty results when printing a process.
- Fixed: Ticket age was displayed in seconds instead of human-readable format in agent ticket zoom (asynchronous widget) and ticket list (view mode L).
- Fixed: Issue with popup redirections after submitting a process category form.
- Fixed: Parameter error in ``Kernel::System::Web::UploadCache`` — no longer tries to dereference undef.
- Fixed: Breadcrumb now loads immediately when switching System Configuration groups via Ajax.
- Fixed: "Title" field on the customer login screen was not set for new customer users.
- Fixed: Console commands not loaded/listed if located in the ``/Custom`` directory.
- Fixed: Removed unnecessary synchronization of hidden text area with RTE instance due to performance issues. Thanks to `@PrimeYeti <https://github.com/PrimeYeti>`_. (`#721 <https://github.com/znuny/Znuny/issues/721>`_)
- Fixed: Web Channel Actions. Thanks to `@ArthurRitscher <https://github.com/ArthurRitscher>`_, Sector Nord AG (`PR#717 <https://github.com/znuny/Znuny/pull/717>`_). Thanks to `@MadsDane <https://github.com/MadsDane>`_. (`#729 <https://github.com/znuny/Znuny/issues/729>`_)
- Fixed: Improved error logging when fetching emails.
- Fixed: RichTextEditor uses wrong instance in ``Core.Agent.TicketAction.js``.
- Fixed: Queue selection in the customer ticket dialog can no longer be set to empty.
- Fixed: Misplaced attachment tooltip. Thanks to `@LuBroering <https://github.com/LuBroering>`_, Sector Nord AG. (`PR#692 <https://github.com/znuny/Znuny/pull/692>`_)
- Fixed: Problem filtering by Owner in the ticket view. Thanks to `@giovanna-bolsoni <https://github.com/giovanna-bolsoni>`_ (`#698 <https://github.com/znuny/Znuny/issues/698>`_), `@LuBroering <https://github.com/LuBroering>`_, Sector Nord AG. (`PR#703 <https://github.com/znuny/Znuny/pull/703>`_)
- Fixed: Only able to delete Signatures, Salutations, and Auto Responses after accepting a popup.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_1/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_1>`_ for a list of all changes.
