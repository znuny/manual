.. _TransitionAction TicketTypeSet:

Set a Ticket Type
##################

Summary
********

With this module you can set the ticket type.

The name of the transition action is :ref:`TicketTypeSet <TransitionAction TicketTypeSet>`.

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+--------+---------------+------------------------+-----------------------------------------+
| Key    | Example Value | Description            | Mandatory                               |
+========+===============+========================+=========================================+
| Type   | A title       | A valid ticket type    | yes, or TypeID                          |
+--------+---------------+------------------------+-----------------------------------------+
| TypeID | 1             | A valid ticket type id | no, if Type is set                      |
+--------+---------------+------------------------+-----------------------------------------+
| UserID | 123           | A valid user ID        | no, will override the logged in user id |
+--------+---------------+------------------------+-----------------------------------------+

.. hint:: 

   The setting Ticket::Type must be enabled in the system configuration.
