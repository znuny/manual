Znuny LTS 6.5.22
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 24-JUN-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.22.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_22>`_          |
+---------------+--------------------------------------------------------------+


Security Vulnerabilities Fixed
******************************
- Fixed missing HTML output filters in template AgentTicketEmailResend.tt (XSS).


Features
********
- Agent and customer error pages now show a configurable link for the next action.


Bug Fixes
*********
- Fixed sorting by dynamic field columns in dashboard ticket widgets falling back to age; process tickets without articles could be hidden. Thanks to `@sergiykhan <https://github.com/sergiykhan>`_ for reporting. (`#811 <https://github.com/znuny/Znuny/issues/811>`_)
- Fixed AgentTicketEmailResend throwing a JavaScript error for missing Bcc input field values.
- Fixed process tickets without articles not being displayed in the dashboard widget "Running Process Tickets".
- Fixed system configuration hash key duplication for keys containing ###. Thanks to `@FloFaber <https://github.com/FloFaber>`_ (Flo Faber) for reporting. (`#789 <https://github.com/znuny/Znuny/issues/789>`_)
- Fixed issue with mentioning out-of-office users via group mention.
- Fixed attachments being assignable to Snippet templates in AdminTemplateAttachment.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_22/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_22>`_ for a list of all changes.
