.. _TransitionAction TicketResponsibleSet:

Set a Ticket Responsible
########################

Summary
********

With this module you can set the responsible for a ticket.

The name of the transition action is :ref:`TicketResponsibleSet <TransitionAction TicketResponsibleSet>`

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+---------------+---------------+-----------------+-----------------------------------------+
| Key           | Example Value | Description     | Mandatory                               |
+===============+===============+=================+=========================================+
| Responsible   | agent         | A valid user    | yes, or ResponsibleID                   |
+---------------+---------------+-----------------+-----------------------------------------+
| ResponsibleID | 1             | A valid user id | no. if Responsible is used              |
+---------------+---------------+-----------------+-----------------------------------------+
| UserID        | 123           | A valid user id | no, will override the logged in user id |
+---------------+---------------+-----------------+-----------------------------------------+
