Overview
########

Welcome to Znuny LTS version 6.5.3

Security Vulnerabilities Fixed
******************************

- Added removal of protocol-relative URLs to Kernel::System::HTMLUtils::Safety. 
- Added security relevant check for the content type of articles and attachments to generic interface operations TicketCreate and TicketUpdate.

Issues Fixed
************

- The selected value in a dynamic field web service dropdown field can now be removed with the 'x' button.
- Fixed HTML element id of forward templates in the ticket detail view (AgentTicketZoom). `#351 <https://github.com/znuny/Znuny/issues/351>`_.
- Added missing scope filter for transition actions in the process management.
- Updated bundled CPAN library Sisimai to version 4.25.16 `#391 <https://github.com/znuny/Znuny/issues/391>`_.
- Fixed event handling for DBCRUD history entries.
- Updated article action "Note to linked ticket" to be only available in the agent ticket detail view (AgentTicketZoom).

Read about all changes in the `CHANGES.md <https://github.com/znuny/Znuny/blob/rel-6_5_3/CHANGES.md>`_. For the complete list of all changes, see the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_3>`_.
