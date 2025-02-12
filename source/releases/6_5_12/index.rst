Znuny LTS 6.5.12
################

**Release Information:**

+--------------+--------------------------------------------------------------+
| Release Date | 12-FEB-2025                                                  |
+--------------+--------------------------------------------------------------+
| Release Type | Patchlevel with security fixes                               |
+--------------+--------------------------------------------------------------+
| Download     | `<https://download.znuny.org/releases/znuny-6.5.12.tar.gz>`_ |
+--------------+--------------------------------------------------------------+
| GitHub       | `<https://github.com/znuny/Znuny/tree/rel-6_5_12>`_          |
+--------------+--------------------------------------------------------------+


Security Vulnerabilities Fixed
******************************
- No logging of decrypted content of S/MIME emails in the communication log.
- Fixed access control when updating the ticket state via the Generic Interface.
- Restricted the excution of the backup.pl and restore.pl scripts to the application user to prevent privilege escalation.
- Added and changed HTTP headers after some finding during a penetration test.
- Fixed the missing HttpOnly flag for a cookie that was not set in certain situations.


Changes
*******
- Updated bundled libraries jstree, nunjuckjs and MIME::Decoder::QuotedPrint.
- Increased the size of the columns profile_key and profile_value of database table search_profile.
	

.. important:: Verify if you perform the update with the bundled backup.pl script. Starting with this version, it has to be executed by the application user, typically otrs. The same restriction now applies to the restore.pl script.


Fixed Issues
************
- The check modules command now lists the require Perl Module Hash::Merge as mandatory.
- Fixed time zone handling for cron events to honor daylight saving time.
- The system configuration option SendmailEncodingForce is now a selection instead of a text field.
- Fixed multiple ticket notifications being sent for empty process tickets for the event NotificationNewTicket.
- Fixed user cache being cleared for all users whenever a user logs in/out.
- ProcessManagament: fixed the error handling in activity dialogues for owner fields. Thanks to Daylton Rodrigues (`@dayltonr <https://github.com/dayltonr>`_) for reporting. `Issue #627 <https://github.com/znuny/Znuny/issues/627>`_
- Ticket state in the PDF search results for agents and customer users are now translated. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting the issue. `Issue #615 <https://github.com/znuny/Znuny/issues/615>`_
- Fixed 'Use of uninitialized value' warning when building custom package and there is no permission to write to the target directory. Thanks to `@BuilderNSV <https://github.com/BuilderNSV>`_ for reporting the issue. `Issue #610 <https://github.com/znuny/Znuny/issues/610>`_
- Fixed uninitialized value in AdminSelectBox. Thanks to Sector Nord AG (`@jsinagowitz <https://github.com/jsinagowitz>`_). `Pull request #611 <https://github.com/znuny/Znuny/issues/611>`_



Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_12/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_12>`_ for a list of all changes.