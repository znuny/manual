Znuny 7.1.3
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 02-OCT-2024                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel with security fixes                               |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.1.3.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_1_3>`_           |
+---------------------+--------------------------------------------------------------+

Security Vulnerabilities Fixed
******************************
- Added HTML filter to prevent XSS in the SLA description field of Process Management Activity Dialogues. Thanks for reporting to Tim Püttmanns, Maxcence.
- Mitigating a ReDos via email when parsing HTML of Microsoft Word. Thanks for reporting to Emin Yazi (@eyazi), Efflux.

Changes
*******
- Improvement for MySQL/MariaDB user for the bundler backup script backup.pl by using the  --single-transaction.
- Updated the CKEditor to 4.25.1-znuny.
- Improved error logging and visibility for OAuth2 token requests.

Fixed Issues
************
- Fixed overflow of dynamic field groups in AgentTicketZoom process widget. Thanks to Sector Nord AG (@jsinagowitz). `#553 <https://github.com/znuny/Znuny/issues/553>`
- Improved Dark skin. `#584 <https://github.com/znuny/Znuny/issues/584>`
- Fixed the console command to import PostMaster Filter. Existing filters will now be updated instead of creating a new. Thanks to @meisterheister for reporting the issue. `#527 <https://github.com/znuny/Znuny/issues/527>`
- Fixed a bug in ArticleStorageSwitch to prevent wrong file names during export.
- Fixed the console command to add services that failed to work when ITSMCore is installed.
- Fixed duplicate database record insert attempts for ticket flags. Thanks to @lukasdebaum for reporting. `#5531 <https://github.com/znuny/Znuny/issues/531>`

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_1_3/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_1_3>`_ for a list of all changes.
