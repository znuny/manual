Znuny LTS 6.5.24
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 19-AUG-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.24.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_24>`_          |
+---------------+--------------------------------------------------------------+


Changes & Improvements
**********************
- The REST transport module now keeps query parameters that don't contain placeholders.
- Cc and Bcc are now also set when only an article is created instead of sent in the generic interface operation ``TicketCreate``.

Security Fixes
**************
- **CVE-2025-25977:** Fixed a prototype pollution vulnerability in the bundled JavaScript library canvg by updating from version 1.5 to 4.0.3.

Bug Fixes
*********
- Fixed ``AgentTicketEmailResend`` not reverting the ticket owner to the previous owner when the user who cancelled the resend was not the actual ticket owner before the resend was initiated.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_24/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_24>`_ for a list of all changes.
