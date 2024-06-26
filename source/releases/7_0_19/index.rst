Znuny 7.0.19
############

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 26-JUN-2024                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.0.19.tar.gz>`_ |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_0_19>`_          |
+---------------------+--------------------------------------------------------------+

Changes
*******
- The invoker Ticket::Generic provides the date and time parts of UntilTime.
- A new console command exports the modified system configuration settings.
- A daemon task that deletes orphaned sessions.
- The Generic Interface operations TicketCreate and TicketUpdate now support multiple articles.

Fixed Issues
************
- The AdminSystemFiles modules now work correctly when the application directory is a symbolic link.
- Fixed CSS problem with displaying articles in the ticket details view. 
- Improved regular expression to reduce long parsing times on complex emails.
- Fixed caching when a queue is updated.
- Fixed value used for owner lookup in AgentTicketProcess. Thanks to Falko Saller (`@falkos <https://github.com/falkos>`_). `#556 <https://github.com/znuny/Znuny/pull/556>`_

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_19/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_19>`_ for a list of all changes.
