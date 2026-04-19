.. meta::
   :description: Use the TicketQueueSet transition action in Znuny to move a ticket to a new queue by queue name or ID from within a process workflow.
   :keywords: ticketqueueset, znuny transition action, move ticket, change queue, queueid, ticket routing, process queue, ticket queue

.. _TransitionAction TicketQueueSet:

Set a Ticket Queue
###################

Summary
********

With this module you can set the queue a ticket.

The name of the transition action is :ref:`TicketQueueSet <TransitionAction TicketQueueSet>`

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+---------+---------------+-------------------------+-----------------------------------------+
| Key     | Example Value | Description             | Mandatory                               |
+=========+===============+=========================+=========================================+
| Queue   | 3 normal      | A valid ticket queue    | yes, or QueueID                         |
+---------+---------------+-------------------------+-----------------------------------------+
| QueueID | 3             | A valid ticket queue ID | no. if Queue is used                    |
+---------+---------------+-------------------------+-----------------------------------------+
| UserID  | 123           | A valid user id         | no, will override the logged in user id |
+---------+---------------+-------------------------+-----------------------------------------+
