New Features
############

In Release 6.2 we have a mix from external Pull Requests and the integration of existing packages.

.. _Framework features 6.2:

Framework
*********

An event is now triggered when all children tickets of a parent are closed (``TicketAllChildrenClosedEvent``). This event can be used to, among other things, trigger a generic agent.
A simple generic agent can then be configured to close a ticket, when all of it's children are closed.


.. _Integrated features 6.2:

Packages Integrated
*********************
 
.. note:: If your setup depends on those add-ons, please note that you can remove them from your dependencies if you target 6.2 .


- :ref:`Znuny4OTRS-TicketAttributeRelations`
- :ref:`Znuny4OTRS-NotifyOnEmptyProcessTickets`
- :ref:`Znuny4OTRS-AdvancedProcessManagement`



.. _Znuny4OTRS-TicketAttributeRelations:

Znuny4OTRS-TicketAttributeRelations
====================================

This feature enables Znuny users to create and manage relations between all kind of Ticket objects.
The dependencies are managed via CSV/XLSX files and can be used to create relations/dependencies
between the following objects:

- Queue - Name of the queue
- DynamicField_xxx - Dropdown and Multiselect dynamic field, only for object type ticket
- State - state
- Priority - priority
- Type - ticket typ
- Lock - lock
- CustomerID - customer id
- CustomerUserID - customer user id
- Owner - login name of the owner
- Responsible - login name of the responsible
- Service - service
- SLA - service level agreement

It is now possible to create a relation between a Queue and the content of a Dynamic Field,
without the hassle of the ACL module. 
It is possible to create chained dependencies like:

``Queue->DynamicField_1->DynamicField_2->State``

All dependencies can be managed via Excel Sheets. An admin user does not need to maintain 
large lists of ACL rules anymore. Users can send their updated sheets to the admin
which than just uploads them, to update the rules.

More details can be found in :doc:`../../admin/ticketattributerelations/index`.

.. _Znuny4OTRS-NotifyOnEmptyProcessTickets:

Znuny4OTRS-NotifyOnEmptyProcessTickets
======================================

In Znuny no notifications are sent for process tickets that are created without an article.
This feature enables Znuny to send a Notification to the agents. The 'NotificationNewTicket' event is executed, which can be used as trigger for ticket-notifications or Generic Agent jobs.


.. _Znuny4OTRS-AdvancedProcessManagement:

Znuny4OTRS-AdvancedProcessManagement
====================================

The package AdvancedProcessManagement extends Znuny with additional functions in the process management module
and has been fully integrated in version 6.2. 

Included are new transition modules. These new modules allow the creation of complex processes and to work together with other components, such as the the calendar or config items.

More details can be found in :doc:`../../admin/processmanagement/index`.


Feature Contributions
*********************

Contributed by Sector Nord AG:

- Attachments to TransitionAction "TicketCreate"
- Optional check condition in Transition Actions
- Transition Action parameter placeholder
- Ticket event module TicketAllChildrenClosed
  

Contributed by Kevin Janssen:

- Generic Interface operation SessionRemove

Contributed by Renée Bäcker:

- SysConfig option to enable week numbers in the datepicker widget
  
Contributed by maxence:

- Added new autocomplete values (New Password, OTP Token) to input fields


