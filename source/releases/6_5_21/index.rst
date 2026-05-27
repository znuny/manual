Znuny LTS 6.5.21
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 27-MAY-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.21.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_21>`_          |
+---------------+--------------------------------------------------------------+


Security Vulnerabilities Fixed
******************************
- CVE-2025-26843: Fixed infinite loop when replacing tags in the template generator.
- CVE-2025-59490: Follow-up fix for scrambled script tags.
- Fixed XSS via JavaScript in URL parameters in the communication log admin view.
- Fixed XSS in user preferences DB.


Changes
*******
- Changed the name of the user with ID 1.


Fixed Issues
************
- Fixed package manager not using the user ID for package operations.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_21/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_21>`_ for a list of all changes.
