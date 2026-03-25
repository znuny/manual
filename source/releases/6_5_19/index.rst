Znuny LTS 6.5.19
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 25-MAR-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.19.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_19>`_          |
+---------------+--------------------------------------------------------------+


Security Vulnerabilities Fixed
******************************
- CVE-2025-52204: Fixed XSS issue with session ID in URL parameter. Thanks to Miguel P. for reporting.
- CVE-2025-59490: Fixed XSS issue with unfiltered URL parameters given to backend.
- For security reasons, detailed error messages are no longer shown in the GUI.
- Improved content security policy HTTP header.
- Source view for rich text editor deactivated in customer frontend to prevent arbitrary code injection.
- Replaced ``EncodeInput()`` method in ``KS:Encode`` with a safe version.


Features
********
- Added Sender column support for dashboard ticket widgets.
- Added configurable filter for ticket search to the ticket merge dialog (AgentTicketMerge).
- Added console command ``Maint::Ticket::Unwatch``.
- Added parameter ``FormID`` to AJAX requests of autocompletion modules (needed for inserting FAQ entries with inline images into RTE via autocompletion).
- Sector Nord AG: Added support for multiple RichText instances. Thanks to `@LuBroering <https://github.com/LuBroering>`_. (`PR#736 <https://github.com/znuny/Znuny/pull/736>`_)


Changes
*******
- Reply function in the agent ticket compose dialog is no longer available if the article is internal and was created by an agent or by the system.
- Changed ticket zoom information widget to count only open tickets with the same customer when ``Ticket::Frontend::ZoomCustomerTickets`` is enabled.
- Increased length of the password column for ``users``, ``customer_user``, and ``mail_account``.
- Improved handling of read-only fields for ``CustomerUser::DB`` and ``CustomerCompany::DB`` backends.
- Sped up UUID creation for DBCRUD modules.
- Simplified handling of the ``Admin::Package::Export`` console command.


Fixed Issues
************
- Fixed CustomerUser article iframe not resizing when all articles are shown.
- Fixed misleading popup message when opening more than one ticket from overviews using a shortcut to open in a new tab/window.
- Fixed problems with leftover UTF-16 surrogates in incoming UTF-8 text.
- Fixed issue with sorting dropdown elements when ``Ticket::Frontend::AccountTimeType`` is set to Dropdown.
- Fixed console commands ``Admin::Group::UserLink`` and ``Admin::Group::RoleLink`` with inconsistent available permissions.
- Fixed sender address for process tickets not assigned properly in the customer interface.
- Fixed Znuny redirecting after login to the default view even when an ``ExternalURL`` parameter with an ``Action`` is encoded in the link.
- Fixed ``TemplateGenerator`` broken when using RichText.
- Fixed customer interface ``PopupClose`` function loading agent interface header/footer, referencing unsupported features. Added ``CustomerPopupClose`` function.
- Fixed the tags ``<OTRS_TICKET>`` and ``<OTRS_MERGE_TO_TICKET>`` could only be used once in ``Ticket::Frontend::AutomaticMergeText`` due to missing 'global' flag. Thanks to Tim Püttmanns (`@tipue-dev <https://github.com/tipue-dev>`_), maxence. (`PR#753 <https://github.com/znuny/Znuny/pull/753>`_)
- Fixed date check regex for config option ``ICSParser::StartDate`` now actually matches ``YYYYMMDD``.
- Fixed unexpected rate limit applied when ``SendmailModule::RateLimit`` is disabled.
- Fixed the link to a specific article in a ticket not working if users have different "Show all articles" settings. Article links now handle both display modes.
- Fixed issue with cache applied incorrectly to "My last changed tickets" widget.
- Removed unnecessary HTML quoting of data in template generator backend.
- Fixed missing styles when printing process in the admin interface.
- Fixed ticket age displayed in seconds instead of human-readable format in agent ticket zoom (asynchronous widget) and ticket list (view mode L).
- Fixed parameter error in ``Kernel::System::Web::UploadCache`` — no longer tries to dereference undef.
- Fixed "Title" field on the customer login screen was not set for new customer users.
- Fixed console commands not loaded/listed if located in the ``/Custom`` directory.
- Improved error logging when fetching emails.
- Fixed customer ticket details screen now redirects to the ticket overview if accessed without permissions.
- Fixed session validation before redirect; fixed related frontend test.
- Fixed navigation path for ``Ticket::Frontend::AgentTicketNoteToLinkedTicket###IsVisibleForCustomerDefault``.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_19/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_19>`_ for a list of all changes.
