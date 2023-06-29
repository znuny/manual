Changes
#######

Security Vulnerabilities Fixed
******************************

- Added removal of protocol-relative URLs to Kernel::System::HTMLUtils::Safety. 
- Added security relevant check for the content type of articles and attachments to generic interface operations TicketCreate and TicketUpdate.

Issues Fixed
************

- Fixed not correct shown priority and state colors `#443 <https://github.com/znuny/Znuny/issues/443>`_.
- Added missing scope filter for transition actions in the process management.
- Updated bundled CPAN library Sisimai to version 4.25.16 `#391 <https://github.com/znuny/Znuny/issues/391>`_.
- Fixed event handling for DBCRUD history entries.
- Updated article action "Note to linked ticket" to be only available in the agent ticket detail view (AgentTicketZoom).

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_6/CHANGES.md>`_. For the complete list of all changes, see the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_6>`_.
