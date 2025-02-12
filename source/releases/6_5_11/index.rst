Znuny LTS 6.5.11
################

**Release Information:**

+--------------+--------------------------------------------------------------+
| Release Date | 02-OCT-2024                                                  |
+--------------+--------------------------------------------------------------+
| Release Type | Patchlevel with security fixes                               |
+--------------+--------------------------------------------------------------+
| Download     | `<https://download.znuny.org/releases/znuny-6.5.11.tar.gz>`_ |
+--------------+--------------------------------------------------------------+
| GitHub       | `<https://github.com/znuny/Znuny/tree/rel-6_5_11>`_          |
+--------------+--------------------------------------------------------------+

Security Vulnerabilities Fixed
******************************
- Fixed regular expression to prevent DoS when parsing specific HTML emails. Thanks for reporting to Emin Yazi (`@eyazi <https://github.com/eyazi>`_), Efflux.
- Added HTML filter to ProcessManagement/SLA template to prevent XSS attacks. Thanks to Tim Püttmanns (`@tipue-dev <https://github.com/tipue-dev>`_), maxence.

Changes
*******
- Updated CKEditor to version 4.25.1-znuny
- Translated dropdown list are now correct sorted.
- Improved error logging when using OAuth2 token.
- Console command Admin::PostMasterFilter::Import now will also update existing filters instead of only create new ones. Thanks to `@meisterheister <https://github.com/meisterheister>`_ for reporting. `Issue #527 <https://github.com/znuny/Znuny/issues/527>`_

Fixed Issues
************
- Fixed bug in the article storage switch command to prevent duplicate file names with an additional file extension '-1'.
- Fixed console command Admin::Service::Add to work with installed ITSMCore add-on. 
- Fixed duplicate database record insert attempts for ticket flags. Thanks to `@lukasdebaum <https://github.com/lukasdebaum>`_ for reporting. `Issue #531 <https://github.com/znuny/Znuny/issues/531>`_

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_11/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_11>`_ for a list of all changes.