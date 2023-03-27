.. _TransitionAction TicketPrioritySet:

Set a Ticket Priority
######################

Summary
********

With this module you can set the priority a ticket.

The name of the transition action is :ref:`TicketPrioritySet <TransitionAction TicketPrioritySet>.

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+------------+---------------+----------------------------+-----------------------------------------+
| Key        | Example Value | Description                | Mandatory                               |
+============+===============+============================+=========================================+
| Priority   | 3 normal      | A valid ticket priority    | yes, or PriorityID                      |
+------------+---------------+----------------------------+-----------------------------------------+
| PriorityID | 3             | A valid ticket priority id | no. if Priority is used                 |
+------------+---------------+----------------------------+-----------------------------------------+
| UserID     | 123           | A valid user id            | no, will override the logged in user id |
+------------+---------------+----------------------------+-----------------------------------------+
