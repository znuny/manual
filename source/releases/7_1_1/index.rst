Znuny 7.1.1
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 24-JUL-2024                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Minor version release                                        |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.1.1.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_1_1>`_           |
+---------------------+--------------------------------------------------------------+

Changes
*******
- GenericInterface: TicketCreate and TicketUpdate operations now accept multiple articles.
- GenericInterface: Omitted fields now apply to the whole data passed through invokers.
- Standard templates can now belong to multiple template types.
- Database character set and collation for MySQL and MariaDB is now utf8mb4.
- Outgoing emails can have the X-Priority header.
- The agent's displayname in mentions follows now the setting FirstnameLastnameOrder.
- Improved medium and preview overviews when using S/MIME and GPG.
- Bulk action for the ticket watch feature.
- Integration of the add-on MarkTicketSeenUnseen.
- The favicon can be configured via system configuration.
- Added a dark skin.
- Added start and end log messages to the Znuny daemon. Thanks to Paweł Bogusławski (@pboguslawski). `#392 <https://github.com/znuny/Znuny/pull/392>`_
- Added display hint when a draft for the same action already exists.
- PostMaster now support also IDs for state, priority, ticket type, service, queue, and SLA headers.
- New console command to export only the changed system configuration settings.
- Added configurable timeout for DNS resolver queries. Thanks to Paweł Bogusławski (@pboguslawski). `#390 <https://github.com/znuny/Znuny/pull/390>`_
- New backend (DBJSON) for user preferences to improve performance on large systems.
- All table have now primary keys.

Fixed Issues
************
- Fixed filtering of columns on the agent dashboard and in ticket overviews. `#510 <https://github.com/znuny/Znuny/issues/510>`_ and `#555 <https://github.com/znuny/Znuny/issues/555>`_
- Improved and fixed links to the CustomerUser and Customer Information Center in several views.
- Fixed missing translations on title hovers on the generic dashboard.
- Updated JavaScript dependencies Moment.js and jQueryUI.
- Fixed event registration regular expressions in the system configuration Thanks to Paweł Bogusławski (@pboguslawski) for reporting. `#440 <https://github.com/znuny/Znuny/issues/440>`_
- Fixed unwanted logout when some personal settigs are saved.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_1_1/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_1_1>`_ for a list of all changes.
