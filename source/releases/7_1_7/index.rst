Znuny 7.1.7
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 30-APR-2025                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel with security fixes                               |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.1.7.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_1_7>`_           |
+---------------------+--------------------------------------------------------------+

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
- GenericAgent can now search for archived tickets.
- Improved performance by fixing the cache key for linked objects.
- Disabled date fields have valid input elements. Thanks for reporting to @BuilderNSV. `#649 <https://github.com/znuny/Znuny/issues/649>`_
- Page selector was not available in mobile view. Thanks for reporting to @MIPMHannes. `#617 <https://github.com/znuny/Znuny/issues/617>`_
- Memory overflow in calendar event when displayed in the ticket detail view.Thanks to @DonMarlowne. `PR#652 <https://github.com/znuny/Znuny/pull/652>`_
- Admin can now create AppointmentCalendars for all groups.
- Several changes to CSS and templates.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_1_7/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_1_7>`_ for a list of all changes.
