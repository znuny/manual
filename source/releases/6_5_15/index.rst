Znuny LTS 6.5.15
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 30-APR-2025                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.15.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_15>`_          |
+---------------+--------------------------------------------------------------+

Security Vulnerabilities Fixed
******************************
- CVE-2025-26847: Fixed masking of passwords in support bundle generator for modified settings YAML file.
- CVE-2025-43926: Agent preferences updated via AJAX requests can now only be updated based on a list (AgentPreferences::AJAXUpdate::AllowedKeys). Thanks to Tim Püttmanns (maxence) for reporting the issue.

Changes
*******
- Added the parameter ToAddressRegExp and CcAddressRegExp to the PostMaster filter ExternalTicketNumberRecognition.
- Updated Net::IMAP::Simple to latest version from GitHub. Thanks to @dandanpena. `PR#155 <https://github.com/znuny/Znuny/pull/155>`_
- GenericInterface: Additional parameter for the operations TicketCreate and TicketUpdate to control if a signature should be added to an article.
- Added configurable limit to number of watched tickets per user.

Fixed Issues
************
- Improved performance by fixing the cache key for linked objects.
- Disabled date fields have valid input elements. Thanks for reporting to @BuilderNSV. `#649 <https://github.com/znuny/Znuny/issues/649>`_
- Memory overflow in calendar event when displayed in the ticket detail view.Thanks to @DonMarlowne. `PR#652 <https://github.com/znuny/Znuny/pull/652>`_
- Admin can now create AppointmentCalendars for all groups.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_15/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_15>`_ for a list of all changes.