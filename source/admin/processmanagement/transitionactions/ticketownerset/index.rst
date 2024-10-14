.. _TransitionAction TicketOwnerSet:

Set a Ticket Owner
########################

Summary
********

With this module you can set the Owner for a ticket.

The name of the transition action is :ref:`TicketOwnerSet <TransitionAction TicketOwnerSet>`

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+---------------+---------------+-----------------+-----------------------------------------+
| Key           | Example Value | Description     | Mandatory                               |
+===============+===============+=================+=========================================+
| Owner   | agent         | A valid user    | yes, or OwnerID                   |
+---------------+---------------+-----------------+-----------------------------------------+
| OwnerID | 1             | A valid user id | no. if Owner is used              |
+---------------+---------------+-----------------+-----------------------------------------+
| UserID        | 123           | A valid user id | no, will override the logged in user id |
+---------------+---------------+-----------------+-----------------------------------------+
