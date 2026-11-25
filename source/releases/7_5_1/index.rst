.. meta::
   :description: Znuny LTS 7.5.1 release notes — security fixes, SAML admin module, integrated attachment preview, encrypted configuration secrets, queue and service navigation layouts, renamed OTRS identifiers and developer information, released 25 November 2026.
   :keywords: znuny 7.5.1, znuny lts 7.5, znuny release notes, znuny changelog, 7.5.1 fixes, znuny lts release, znuny update 7.5.1, znuny security fixes

Znuny LTS 7.5.1
###############

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 25-NOV-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Long Term Support (LTS) release                              |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.5.1.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_5_1>`_           |
+---------------------+--------------------------------------------------------------+

Znuny LTS 7.5 is based on Znuny 7.3 and contains all changes and fixes up to and including Znuny 7.3.8. The notes below list what is new compared to Znuny 7.3.8. See :doc:`/updating/update-7.5` for the update from Znuny 7.3.

Security Fixes
**************
- **CVE-2026-78357:** Sessions are now removed when a customer user is invalidated or renamed in the admin interface (as already done for agents), and when the password of an agent or customer user is changed. The session used to change the own password via the personal preferences is kept.
- **CVE-2026-18089, CVE-2026-18092, CVE-2026-18108:** SAML login now verifies assertion signatures against the configured IdP certificate (``AuthModule::SAML::IdPCACert`` and ``Customer::AuthModule::SAML::IdPCACert``). Net::SAML2 0.89 or higher is now required. Thanks to HARIPRASAD M. and Fabian Bührmann for reporting.
- Fixed access to articles of tickets without permission on PostgreSQL 16+ by rejecting non-numeric article IDs. Thanks to Timotej Doležal (ESET) for reporting.
- Fixed XSS via the URL parameter ``Action`` in the installer. Thanks to Elisa Popowicz (AWARE7) for reporting.
- Inline file responses of ``PictureUpload`` now send the same sandbox Content-Security-Policy as other attachment downloads. Attachment responses now also send ``X-Content-Type-Options: nosniff``. Thanks to `@kta1kri <https://github.com/kta1kri>`_ for reporting.
- The customer selector in agent ticket screens now always escapes customer names, also when a name already contains HTML entities. Thanks to Timotej Doležal (ESET) for reporting.
- The customer ticket zoom now escapes the plain-text article body outside the sandbox iframe. Thanks to Timotej Doležal (ESET) for reporting.
- Splitting a process ticket now requires read permission on the source ticket before its data is used or shown.
- The XSLT mapping of the generic interface no longer evaluates regex replacements as Perl code and restricts file, network and write access. Thanks to Gabriel Rodrigues and João Pedro Gonçalves (Hakai Offensive Security, hakaisecurity.io) for reporting.
- The generic interface operations ``TicketCreate`` and ``TicketUpdate`` no longer let a customer user set an agent article sender or other agent-related ticket fields.
- Fixed SQL injection via ticket link keys in the link cleanup of ticket merges on MySQL/MariaDB. Thanks to Timotej Doležal (ESET) for reporting.
- Database queries now reject non-integer values for the parameters ``Limit`` and ``Start`` before they are added to SQL.
- Fixed permission checks when using dynamic fields of type Webservice. Thanks to `@kta1kri <https://github.com/kta1kri>`_ for reporting.
- Form drafts could be loaded or deleted through a ticket they do not belong to, the draft deletion in the agent ticket zoom had no challenge token check, and the challenge token check accepted tokens of other session types with the same user ID. Thanks to Timotej Doležal for reporting.
- The activity notification bell rendered titles and texts of ticket and appointment notifications as HTML (stored XSS via entity-encoded email subject). Thanks to Timotej Doležal (ESET) for reporting.
- The activity frontend module did not check the challenge token and stored and rendered the activity state and link unvalidated and unescaped (stored XSS in the notification bell). Thanks to Timotej Doležal (ESET) for reporting.
- The "Note to linked ticket" dialog no longer writes to tickets that are not linked or that the agent may not use, and no longer shows linked tickets the agent may not see.
- The agent ticket bulk action now requires write permission on the merge target and the link target.
- Reading, creating and moving appointments now requires the matching calendar permission.
- Adding and editing statistics now requires a challenge token, and stored time scale values are HTML-escaped when shown. Thanks to Timotej Doležal (ESET) for reporting.
- S/MIME certificate and private key filenames are confined to their directories, and the admin read and download actions require a challenge token.
- The import of example processes in process management now rejects files outside of the examples directory.
- The unit test helper and the FS article storage no longer create files and directories outside of their allowed paths. Thanks to Tim Püttmanns (maxence) for reporting.
- The SAML user sync now only uses attributes of the signed assertion. Thanks to Timotej Doležal (ESET) for reporting.
- Customer self-registration no longer accepts ``UserLogin``, ``UserCustomerID`` or any field outside of ``CustomerPanelCreateAccount::AllowedFields``. The login and the customer ID are taken from the email address, and registrations are rate-limited per IP address. **Customer self-registration is now disabled by default.**
- Template names in the admin module for OAuth2 tokens can no longer read YAML files outside of the template directory.

Features
********
- Added support for **AES encrypted passwords** in ``Kernel/Config.pm`` (e.g. database or LDAP bind passwords). Use the new console commands ``Maint::Secret::KeyGenerate`` and ``Maint::Secret::Encrypt``. The optional Perl module ``Crypt::AuthEnc::GCM`` (CryptX) is required for this feature. See :ref:`Encrypted Configuration Secrets <PageNavigation standardoperations_configsecrets_index>`.
- Added **queue and service navigation layouts**: hierarchical navigation bar with hover submenus, and a sidebar tree per agent. See :ref:`View by Queue <PageNavigation agentinterface_overviews_agentticketqueueview_navlayout>`.
- Added the config option ``TemplateGenerator::EmptyValueReplacement`` to choose the text shown for missing values of placeholders in templates.
- Added an event module to reset the responsible of a ticket on queue change.
- Added support for ``ZNUNY_*`` response tags alongside ``OTRS_*`` in the generic interface invoker ``Ticket::Generic``.
- Added the admin module **Authentication** to configure SAML 2.0 authentication for agents and customers in the admin interface, including a setup wizard, SP metadata download and attribute, group and role sync. See :ref:`Authentication Management <PageAdminSAMLConfigurationAdminModule>`.
- Integrated the packages **Znuny-AdvancedAttachments** and **Znuny-ZoomArticlePDFPreview**: attachment preview, attachments widget and menu item in the ticket zoom, embedded PDF preview, and reuse of attachments of other articles in agent ticket dialogs without downloading and uploading them again. See :ref:`Attachments <PageNavigation ticketviews_agentticketzoom_attachments>` and :ref:`Reuse Attachments of Other Articles <PageNavigation ticketviews_agentticketactioncommon_reuseattachments>`.
- Added optional **one-click process dialogs**: activity dialogs can be submitted directly from the activity button without a popup if no input is needed. See :ref:`Activity Dialogs <PageNavigation processmanagement_activitiydialogs>`.
- Process management: Added cloning of processes, activities, activity dialogs, transitions and transition actions. Activity dialogs can be cloned from the *Edit Activity* screen, transition actions from the *Edit Path* screen.
- Added a content filter to the article filter dialog of the agent ticket zoom. Article dynamic fields can be added to the filter with ``Ticket::Frontend::TicketArticleFilterDynamicField``.
- Added multiselect column filters to the linked tickets table (complex view) of the agent ticket zoom.
- Services can be assigned to customer companies. Ticket dialogs offer the services of the selected customer company. Integrated the package **Znuny-CustomerCompanyService**. See :ref:`Services <PageNavigation admin_servicemanagement_services_index>`.

Changes
*******
- The default session cookie names are now ``ZnunyAgentInterface`` and ``ZnunyCustomerInterface``. Unchanged values of the system configuration settings ``SessionName`` and ``CustomerPanelSessionName`` are migrated during the update; the legacy OTRS cookie names are still accepted during the transition.
- The system configuration setting ``OTRSTimeZone`` has been renamed to ``ZnunyTimeZone``. The value is migrated during the update.
- The package repository index file is now ``packages.xml``; ``otrs.xml`` is no longer requested or served. Package downloads now log the URL if the request returns no content.
- The statistics XML export now uses the root element ``znuny_stats``. The import still accepts ``otrs_stats``.
- The REST transport of the generic interface was refactored to support both OTRS and Znuny aliases.
- The URL parameter ``RequestedURL`` can now also be used within existing sessions.
- Removed the console commands ``Dev::Code::CPANAudit`` and ``Dev::Code::CPANUpdate`` as well as the support data collector check for Perl module audits.
- Improved the date picker calendar handling for non-working days and pending default times. With ``TimePendingSkipUnavailableDays`` (and ``TimePendingSkipUnavailableDays::Calendar1`` to ``9``), the default pending date can skip holidays and days without working hours.
- Excess activity notifications are now cleaned up during the migration.
- Improved the tooltip positioning in the appointment calendar.
- Placeholders (smart tags) and the smart tag help screens now use the prefix ``ZNUNY_``. ``OTRS_`` tags are still accepted. ``ZNUNY_`` tags now also work, in any letter case, in appointment notifications, recipient fields, transition actions, config values, and merge, bounce and next-state tags. See :ref:`Placeholder Tags <PageNavigation annexes_placeholders_index>`.
- The PostMaster headers ``X-OTRS-*`` have been renamed to ``X-Znuny-*``. ``X-OTRS-*`` headers still work. The related system configuration settings and PostMaster filters are migrated during the update. See :ref:`E-Mail Headers <PageNavigation annexes_headers_index>`.

Bug Fixes
*********
- Fixed the description of the system configuration setting ``SecureMode``: it now states that GenericAgent, Package Manager and SQL Box are disabled when ``SecureMode`` is not enabled. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting. (`#715 <https://github.com/znuny/Znuny/issues/715>`_)
- Fixed the user search with option ``PostMasterSearch``: it now also searches the login for a matching email address as a fallback to the email address stored in the user preferences.
- Fixed linked tickets being removed when moving or resizing an appointment via drag and drop in the calendar or resource overview.
- Fixed SAML login failing in Chrome and Edge when the authentication at the identity provider took too long.
- Fixed the SAML IdP metadata download not using the ``WebUserAgent`` config options.
- Fixed the date picker not being initialized for date fields added via attribute selection in the ``AgentTicketSearch`` dialog.
- Fixed calendar appointments failing to create a ticket if the relative period was zero. Thanks to `@Fawkespami <https://github.com/Fawkespami>`_ for reporting. (`#821 <https://github.com/znuny/Znuny/issues/821>`_)
- Fixed the PostMaster filter ``ExternalTicketNumberRecognition`` ignoring Cc.
- Fixed customers already selected on a ticket still appearing as selectable in the customer user address book.
- Fixed the console commands to export/import dynamic field configurations using a different format than the GUI.
- Fixed form validation being disabled after closing the "add draft" dialog via the header X, a click outside the dialog or Escape, so that the ticket action could be submitted without required fields.
- Fixed select drop-downs being rendered at a wrong position when specific position criteria were met.
- Fixed uninitialized values in ``Kernel/System/ACL/DB/ACL.pm``.
- Fixed the "Back" button doing nothing in the ticket details dialog in the mobile view.
- Fixed the process transition action ``DynamicFieldSet`` not saving multiple values for all multiselect-type dynamic fields (e.g. ``ConfigItemMultiselect``, ``WebserviceMultiselect``).
- Fixed ``UsedSpace`` being calculated too early in ``Core.UI.js``. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting. (`#604 <https://github.com/znuny/Znuny/issues/604>`_)
- Fixed Date and DateTime dynamic fields ignoring the user time zone when restricting dates to the past or the future.
- Fixed recipients listed on folded To and Cc lines being sent as Bcc by the MSGraph backend and missing from the received message.
- Fixed a use of uninitialized value when minifying the RTE content CSS. Thanks to `@devdog1 <https://github.com/devdog1>`_ for reporting. (`#868 <https://github.com/znuny/Znuny/issues/868>`_)
- Fixed the import of a web service with an invalid configuration showing a success notice although nothing was stored. Thanks to `@natanaraujo3001-crypto <https://github.com/natanaraujo3001-crypto>`_ for reporting. (`#870 <https://github.com/znuny/Znuny/issues/870>`_)
- Fixed a follow-up on a closed ticket locking the ticket to the last owner when the state is kept or stays closed.
- Fixed the ticket reply (``AgentTicketCompose``) quoting the last customer article as plain text instead of the selected article if the template also had the type *Note*.
- Fixed a process not advancing to the next activity when a transition action changed a dynamic field in the same request, e.g. with the result of a web service invoker. The new config option ``Process::Transition::MaxTransitionsPerRequest`` (default ``1``) limits the transitions evaluated per request.
- Fixed the help text of the REST invoker controller mapping: placeholders are replaced from the outgoing data after the mapping, and nested fields use a dot (e.g. ``:Ticket.TicketID``). Thanks to `@killermoehre <https://github.com/killermoehre>`_ for reporting. (`#804 <https://github.com/znuny/Znuny/issues/804>`_)
- Fixed removing sessions by user login also removing the sessions of the other user type if an agent and a customer user had the same login.
- Fixed the uniqueness check of customer user email addresses: it now covers all customer user backends.
- Fixed a performance problem in the PostMaster module ``DestQueue`` caused by too many communication log entries.

Developer Information
*********************
- ``Kernel::System::DateTime::OTRSTimeZoneGet()`` has been renamed to ``ZnunyTimeZoneGet()``. Use ``$ConfigObject->Get('ZnunyTimeZone')`` instead of ``OTRSTimeZone``.
- The root tag of an SOPM file can now also be ``package`` instead of ``otrs_package``.
- The root tag of the package repository index is now ``package_list`` instead of ``otrs_package_list``, and the index file is named ``packages.xml`` instead of ``otrs.xml``. Self-hosted package repositories have to provide ``packages.xml``.
- The statistics XML export uses the root element ``znuny_stats`` instead of ``otrs_stats``.
- Code that relies on the session cookie names ``OTRSAgentInterface`` or ``OTRSCustomerInterface`` should read the names from ``SessionName`` and ``CustomerPanelSessionName`` instead.
- New module ``Kernel::System::Crypt::Secret`` to encrypt and decrypt secrets with AES-256.
- Migration tasks of ``scripts/MigrateToZnuny7_5.pl`` are located in ``scripts/Migration/``.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_5_1/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_5_1>`_ for a list of all changes.
