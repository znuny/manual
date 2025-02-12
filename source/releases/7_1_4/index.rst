Znuny 7.1.4
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 12-FEB-2025                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel with security fixes                               |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.1.4.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_1_4>`_           |
+---------------------+--------------------------------------------------------------+

Security Vulnerabilities Fixed
******************************
- No logging of decrypted content of S/MIME emails in the communication log.
- Fixed access control when updating the ticket state via the Generic Interface.
- Restricted the excution of the backup.pl and restore.pl scripts to the application user to prevent privilege escalation.
- Added and changed HTTP headers after some finding during a penetration test.
- Fixed the missing HttpOnly flag for a cookie not set in certain situations.

Changes
*******
- Updated bundled libraries jstree, nunjuckjs and MIME::Decoder::QuotedPrint.
- Increased the size of the columns profile_key and profile_value of database table search_profile.
- Added a filter when exporting Dynamic Fields.
- Added configurable InputFields::ModernizedSelection::MaxNumberOfOptions. Thanks to `@itweserems <https://github.com/itweserems>`_. `Pull request #576 <https://github.com/znuny/Znuny/pull/576>`_
- S/MIME verification: Added fallback option to disable verification of the signer's certificate after initial verification failed. Activated by new config option SMIME::NoVerify.

.. important:: Verify if you perform the update with the bundled backup.pl script. Starting with this version, it has to be executed by the application user, typically znuny. The same restriction now applies to the restore.pl script.


Fixed Issues
************
- Fixed event check of the event module TicketDynamicFieldDefault.
- ProcessManagament: fixed the error handling in activity dialogues for owner fields. Thanks to Daylton Rodrigues (`@dayltonr <https://github.com/dayltonr>`_) for reporting. `Issue #627 <https://github.com/znuny/Znuny/issues/627>`_
- Sector Nord AG: Fixed module check for calendar plugin. Thanks to Sector Nord AG (`@jsinagowitz <https://github.com/jsinagowitz>`_). `Pull request #623 <https://github.com/znuny/Znuny/pull/623>`_
- The system configuration option SendmailEncodingForce is now a selection instead of a text field.
- Fixed "From" and "To" not being expandable for an article in ticket zoom. Thanks to Oliver Freyermuth (`@olifre <https://github.com/olifre>`) for reporting. `Issue #605 <https://github.com/znuny/Znuny/issues/605>`_
- Fixed multiple ticket notifications being sent for empty process tickets for the event NotificationNewTicket.
- The check modules command now lists the require Perl Module Hash::Merge as mandatory.
- Fixed user cache being cleared for all users whenever a user logs in/out.
- Fixed Bug - Added missing template toolkit translations. Translate the ticket state in PDF search result (AgentTicketSearch|CustomerTicketSearch). Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting the issue. `Issue #615 <https://github.com/znuny/Znuny/issues/615>`_
- Fixed uninitialized value in AdminSelectBox. Thanks to Sector Nord AG (`@jsinagowitz <https://github.com/jsinagowitz>`_). `Pull request #611 <https://github.com/znuny/Znuny/issues/611>`_
- Fixed link in INSTALL.md / UPDATING.md. Thanks to `@Sidpatchy <https://github.com/Sidpatchy>`. `Pull request #589 <https://github.com/znuny/Znuny/pull/589>`_
- Sector Nord AG: Fixed #571 AgentTicketProcess Mobile-View is not showing all elements of ActivityDialog. Thanks to Lukas Bröring (`@LuBroering <https://github.com/LuBroering>`_). `Pull request #553 <https://github.com/znuny/Znuny/pull/553>`_
- Add-on names are no longer translated.


Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_1_4/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_1_4>`_ for a list of all changes.
