Overview
########

Welcome to Znuny LTS version 6.5.8

Security Vulnerabilities Fixed
******************************

- Fixed security issue with uploaded files that could be used for remote code execution (`CVE-2024-32491 <https://www.cve.org/CVERecord?id=CVE-2024-32491>`_). Thanks to Martino Spagnuolo for reporting and providing the fix.
- Fixed SQL injection issue when using the draft functinality (`CVE-2024-32493 <https://www.cve.org/CVERecord?id=CVE-2024-32493>`_). Thanks to Martino Spagnuolo for reporting the issue.

Issues Fixed
************

- Fixed session handling when saving user preferences.
- Fixed usage of multiple database objects in customer and customer user database backend. (`#540 <https://github.com/znuny/Znuny/issues/540>`_)

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_8/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_8>`_ for a list of all changes.

