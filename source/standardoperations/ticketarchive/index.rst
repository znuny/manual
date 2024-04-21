.. _PageNavigation standardoperations_ticketarchive:

The Archive System
##################

Archiving your tickets helps reduce the number of tickets found during a default search. This aids in performance, on large systems, by setting a visibility flag in the database. Ticket searches will not consider archived tickets by default. Tickets can still be found by including them explicitly in searches and statistics. The archive system is not active per default, and requires setup. Activate the archive system via the system configuration.

Configure Archiving
*******************

In the system configuration, you will find the following settings:

Ticket::ArchiveSystem
  Enable or disable archiving.
Ticket::ArchiveSystem::RemoveSeenFlags
  Remove flags from archived tickets.
Ticket::ArchiveSystem::RemoveTicketWatchers
  Remove any watchers from archived tickets.
Ticket::CustomerArchiveSystem
  Enable customer search in archive.
Ticket::EventModulePost###2300-ArchiveRestore
  Un-archive tickets when the state changes to a non-closed state type.
Ticket::SearchIndex::IndexArchivedTickets
  Indexing for archived tickets. (Increases StaticDB Index Size and decreases RuntimeDB performance)

Once active, the agent search, statistic edit and generic agent masks include an archive search filter. If so enabled, the customer search mask also includes this option as well.

.. important:: 
  You will have to accommodate for this when activating this option.

Archiving Tickets
*****************

Archiving tickets requires that a generic agent be configured. Set the search filter (be sure to only search non-archived tickets), and set the option to archive the tickets found. A good practice is to use the filters:

- Create time = more than 1 year ago
- State = closed successful, closed unsuccessful, merged, removed
- Last changed = more than 6 months ago

Set a schedule, then your tickets will begin to archive.

Restoring Tickets
*****************

A ticket will automatically be restored by a change in state. This can happen when

- A generic agent triggers a state change
- A follow-up email is received on a pending or closed ticket
- An agent or customer reopens using the customer interface
