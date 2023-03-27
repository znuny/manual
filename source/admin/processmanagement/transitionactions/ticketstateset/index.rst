.. _TransitionAction TicketStateSet:

Set a Ticket State
##################

Summary
********

With this module you can set the state of a ticket.

The name of the transition action is :ref:`TicketStateSet <TransitionAction TicketStateSet>`.

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+-----------------+---------------------+-----------------------------+---------------------------------------------------------------+
| Key             | Example Value       | Description                 | Mandatory                                                     |
+=================+=====================+=============================+===============================================================+
| State           | open                | A valid ticket state        | yes, or StateID                                               |
+-----------------+---------------------+-----------------------------+---------------------------------------------------------------+
| StateID         | 1                   | A valid ticket state ID     | no. if State is used                                          |
+-----------------+---------------------+-----------------------------+---------------------------------------------------------------+
| PendingTime     | 2022-11-01 00:00:00 | A valid ISO date time stamp | yes, if pending auto or pending reminder state type is chosen |
+-----------------+---------------------+-----------------------------+---------------------------------------------------------------+
| PendingTimeDiff | 1400                | A unit in minutes from now  | no, if PendingTime is used                                    |
+-----------------+---------------------+-----------------------------+---------------------------------------------------------------+
| UserID          | 123                 | A valid user ID             | no, will override the logged in user id                       |
+-----------------+---------------------+-----------------------------+---------------------------------------------------------------+
