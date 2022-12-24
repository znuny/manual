How Ticket Escalation Works
###########################
.. _PageNavication generalinformation_ticketescalation_index:

The requirements for ticket escalation are built into the software and connected to values within the system configuration. Calculation is based upon the working hours and holidays found in the calendars. Escalation events can trigger different things within the system, and here we will learn about all of them.

Escalation times will also be shown in different parts of the system.

* overviews if the column is configured 
* ticket detail view (AgentTicketZoom)
* statistics output

Every five minutes per default the system will check for the escalation events and trigger them as necessary. ``Daemon::SchedulerCronTaskManager::Task###EscalationCheck``.

Basic Escalation Flow
*********************

.. mermaid::

    graph TD
        A[EscalationCheck] --> B{Escalation Time Reached?}
        B --> |First Response Time Reached| C[Escalation]
        B ==> |Update Time Reached| D{Last Response From Customer?}
        B ==> |Solution Time Reached| E{Is or was the ticket previously closed?}
        D --> |No| H[No Escalation]
        D --> |Yes| I[Escalation]
        E --> |Yes| J[No Escalation]
        E --> |No| K[Escalation]

Escalation Types
****************

There are three types of escalations.Each of these three types of escalations.

First Response Time
    A new or open ticket containing no external communication for the customer from an agent. By default, the only type of communication which can stop this escalation is a phone or email communication which is visible to the customer and where the sender is the agent.
Update Time
    The update time is triggered if the last message is from the customer and the update time has been reached.
Solution Time
    The solution time escalation begins only if the ticket is not and has never previously been closed and the solution time has been reached.

Escalation Stages
*****************

The escalation stages listed below determine when notifications should be sent for example. However these events can also be used in different parts of the system.

Escalation Before
    Event is triggered at a certain percentage of time before escalation.

Escalation Stop
    Event is triggered at the exact escalation start time based on the escalation time.

Escalation Stop
    Event is triggered via a TicketUpdate event.

Escalation Calculation
**********************

Escalation index is calculated by default after:

* TicketSLAUpdate
* TicketQueueUpdate
* TicketStateUpdate
* TicketCreate
* ArticleCreate
* TicketDynamicFieldUpdate
* TicketTypeUpdate
* TicketServiceUpdate
* TicketCustomerUpdate
* TicketPriorityUpdate
* TicketMerge

Calculation is based upon the assigned service level agreement, or queue settings when no service level agreement is assigned. Escalation events are only triggered during working hours.

.. seealso::

    More on :ref:`working hours <PageNavigation generalinformation_workinghours_index>`.

Reporting on Escalations
************************

To generate statistics about escalations, see more in the chapter on :ref:`Reporting <PageNavigation agentinterface_statistics_index>`.