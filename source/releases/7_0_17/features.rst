Overview
########

Welcome to Znuny version 7.0.17

Security Vulnerabilities Fixed
******************************

- Fixed security issue with JavaScript in body of article being executed in customer ticket zoom (`CVE-2024-32492 <https://www.cve.org/CVERecord?id=CVE-2024-32492>`_). Thanks to Martino Spagnuolo for reporting the issue.
- Fixed security issue with uploaded files that could be used for remote code execution (`CVE-2024-32491 <https://www.cve.org/CVERecord?id=CVE-2024-32491>`_). Thanks to Martino Spagnuolo for reporting and providing the fix.
- Fixed SQL injection issue when using the draft functionality (`CVE-2024-32493 <https://www.cve.org/CVERecord?id=CVE-2024-32493>`_). Thanks to Martino Spagnuolo for reporting the issue.

Issues Fixed
************

- Fixed session handling when saving user preferences.
- Fixed usage of multiple database objects in customer and customer user database backend. (`#540 <https://github.com/znuny/Znuny/issues/540>`_)

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_17/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_17>`_ for a list of all changes.

