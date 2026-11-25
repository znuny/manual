.. meta::
   :description: Znuny LTS 6.5.27 release notes — security fixes including CVE-2026-78357, customer self-registration disabled by default, and bug fixes, released 25 November 2026.
   :keywords: znuny 6.5.27, znuny lts 6.5, znuny release notes, znuny security fixes, cve-2026-78357, znuny patchlevel, znuny changelog

Znuny LTS 6.5.27
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 25-NOV-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.27.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_27>`_          |
+---------------+--------------------------------------------------------------+

.. important::

    **Customer self-registration is now disabled by default.** If your customers register themselves in the customer interface, enable ``CustomerPanelCreateAccount`` in the system configuration after the update. The registration only accepts the fields listed in ``CustomerPanelCreateAccount::AllowedFields`` (default: title, first name, last name and email address). The login and the customer ID are taken from the email address. Registrations are rate-limited per IP address (``CustomerPanelCreateAccount::RateLimitMaxAttempts``, ``CustomerPanelCreateAccount::RateLimitWindow``).

Security Fixes
**************
- **CVE-2026-78357:** Sessions are now removed when a customer user is invalidated or renamed in the admin interface (as already done for agents), and when the password of an agent or customer user is changed. The session used to change the own password via the personal preferences is kept.
- Customer self-registration no longer accepts ``UserLogin``, ``UserCustomerID`` or any field outside of ``CustomerPanelCreateAccount::AllowedFields``. The login and the customer ID are taken from the email address, and registrations are rate-limited per IP address. Customer self-registration is now disabled by default.
- Fixed SQL injection via ticket link keys in the link cleanup of ticket merges on MySQL/MariaDB. Thanks to Timotej Doležal (ESET) for reporting.
- Fixed access to articles of tickets without permission on PostgreSQL 16+ by rejecting non-numeric article IDs. Thanks to Timotej Doležal (ESET) for reporting.
- Fixed XSS via the URL parameter ``Action`` in the installer. Thanks to Elisa Popowicz (AWARE7) for reporting.
- Fixed permission checks when using dynamic fields of type Webservice. Thanks to `@kta1kri <https://github.com/kta1kri>`_ for reporting.
- Inline file responses of ``PictureUpload`` now send the same sandbox Content-Security-Policy as other attachment downloads. Attachment responses now also send ``X-Content-Type-Options: nosniff``. Thanks to `@kta1kri <https://github.com/kta1kri>`_ for reporting.
- The XSLT mapping of the generic interface no longer evaluates regex replacements as Perl code and restricts file, network and write access. Thanks to Gabriel Rodrigues and João Pedro Gonçalves (Hakai Offensive Security, hakaisecurity.io) for reporting.
- The generic interface operations ``TicketCreate`` and ``TicketUpdate`` no longer let a customer user set an agent article sender or other agent-related ticket fields.
- Form drafts could be loaded or deleted through a ticket they do not belong to, the draft deletion in the agent ticket zoom had no challenge token check, and the challenge token check accepted tokens of other session types with the same user ID. Thanks to Timotej Doležal for reporting.
- The "Note to linked ticket" dialog no longer writes to tickets that are not linked or that the agent may not use, and no longer shows linked tickets the agent may not see.
- The agent ticket bulk action now requires write permission on the merge target and the link target.
- Splitting a process ticket now requires read permission on the source ticket before its data is used or shown.
- Reading, creating and moving appointments now requires the matching calendar permission.
- Adding and editing statistics now requires a challenge token, and stored time scale values are HTML-escaped when shown. Thanks to Timotej Doležal (ESET) for reporting.
- Database queries now reject non-integer values for the parameters ``Limit`` and ``Start`` before they are added to SQL.
- S/MIME certificate and private key filenames are confined to their directories, and the admin read and download actions require a challenge token.
- The import of example processes in process management now rejects files outside of the examples directory.
- Template names in the admin module for OAuth2 tokens can no longer read YAML files outside of the template directory.
- The unit test helper and the FS article storage no longer create files and directories outside of their allowed paths. Thanks to Tim Püttmanns (maxence) for reporting.

Changes
*******
- Improved the date picker calendar handling for non-working days and pending default times. With ``TimePendingSkipUnavailableDays`` (and ``TimePendingSkipUnavailableDays::Calendar1`` to ``9``), the default pending date can skip holidays and days without working hours.
- The URL parameter ``RequestedURL`` can now also be used within existing sessions.

Bug Fixes
*********
- Fixed the support bundle generation hanging because the Perl module audit walked the home directory.
- Fixed ``UsedSpace`` being calculated too early in ``Core.UI.js``. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting. (`#604 <https://github.com/znuny/Znuny/issues/604>`_)
- Fixed a follow-up on a closed ticket locking the ticket to the last owner when the state is kept or stays closed.
- Fixed the user search with option ``PostMasterSearch``: it now also searches the login for a matching email address as a fallback to the email address stored in the user preferences.
- Fixed the import of a web service with an invalid configuration showing a success notice although nothing was stored. Thanks to `@natanaraujo3001-crypto <https://github.com/natanaraujo3001-crypto>`_ for reporting. (`#870 <https://github.com/znuny/Znuny/issues/870>`_)
- Fixed linked tickets being removed when moving or resizing an appointment via drag and drop in the calendar or resource overview.
- Fixed the uniqueness check of customer user email addresses: it now covers all customer user backends.
- Fixed calendar appointments failing to create a ticket if the relative period was zero. Thanks to `@Fawkespami <https://github.com/Fawkespami>`_ for reporting. (`#821 <https://github.com/znuny/Znuny/issues/821>`_)
- Fixed removing sessions by user login also removing the sessions of the other user type if an agent and a customer user had the same login.
- Fixed the PostMaster filter ``ExternalTicketNumberRecognition`` ignoring Cc.
- Fixed the console commands to export/import dynamic field configurations using a different format than the GUI.
- Fixed uninitialized values in ``Kernel/System/ACL/DB/ACL.pm``.
- Fixed the help text of the REST invoker controller mapping: placeholders are replaced from the outgoing data after the mapping, and nested fields use a dot (e.g. ``:Ticket.TicketID``). Thanks to `@killermoehre <https://github.com/killermoehre>`_ for reporting. (`#804 <https://github.com/znuny/Znuny/issues/804>`_)
- Fixed the process transition action ``DynamicFieldSet`` not saving multiple values for all multiselect-type dynamic fields (e.g. ``ConfigItemMultiselect``, ``WebserviceMultiselect``).
- Fixed a performance problem in the PostMaster module ``DestQueue`` caused by too many communication log entries.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_27/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_27>`_ for a list of all changes.
