.. _TransitionAction TicketSLASet:

Set a Ticket SLA
################

Summary
********

With this module you can set the service level agreement (SLA) of a ticket.

The name of the transition action is :ref:`TicketSLASet <TransitionAction TicketSLASet>` and should be used in combination with :ref:`TicketServiceSet <TransitionAction TicketServiceSet>`.

.. image:: images/TicketSLASet.png
    :width: 100%
    :alt: Example transition action

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+--------+---------------+-----------------+-----------------------------------------+
| Key    | Example Value | Description     | Mandatory                               |
+========+===============+=================+=========================================+
| SLA    | Low priority  | A valid SLA     | yes, or SLAID                           |
+--------+---------------+-----------------+-----------------------------------------+
| SLAID  | 1             | A valid SLA ID  | no. if SLA is used                      |
+--------+---------------+-----------------+-----------------------------------------+
| UserID | 123           | A valid user ID | no, will override the logged in user id |
+--------+---------------+-----------------+-----------------------------------------+

.. important:: Services and SLAs

   An SLA can be set, only if the service of the ticket belongs to the SLA. This means you must ensure the ticket has a service
   or combine this transition action with :ref:`TicketServiceSet <TransitionAction TicketServiceSet>`

.. tip:: System Configuration

   The configuration ``Ticket::Service`` must be enabled.
