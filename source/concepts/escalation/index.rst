.. _PageNavigation concepts_escalation_index:

Ticket Escalation
#################

Ticket escalation refers to the process of ensuring that tickets receive attention and resolution
within predefined service levels. Escalations are typically configured as part of **service-level agreements (SLAs)**
or as default **queue escalation times** to maintain consistent and efficient support.

Here’s how ticket escalation works in Znuny:

.. _PageNavication section_escalation_types:

Components of Escalation
************************

Escalation times
================

There are three escalations types in Znuny:

- **First Response Time**: The time within which the first response to a ticket should be provided.
- **Update Time**: The maximum allowed time between updates or replies.
- **Solution Time**: The total time allowed to resolve the ticket.

These are set within the service level agreement or in the :ref:`queue settings <pagenavigation admin_queues_index>` directly.

Escalation Events
==================

Escalation events are used by automations within the system like:

- Notifications
- Web Services
- Proceses
- Generic Agents
- Event Modules (hard coded perl modules)

The events are:

- Escalation<Type>NotifyBefore
- Escalation<Type>TimeStart
- Escalation<Type>TimeStop

.. seealso:: Further Information

    :ref:`pagenavication section_escalation_types`

Escalation Priority
*******************
Escalation rules are applied first for the queue. If a service level agreement is assagined, this will override any queue times.


Escalation Monitoring
*********************

An **Escalation View** as well as dashboard widgets for viewing escalated tickets. This helps prioritize urgent tickets and avoid breaches.

Escalation Dashboards Widgets
=============================

Agent Dashhboard
    Shows all tickets for which a user has rw permissions.
  
Customer User Information Center
    Shows all tickets for which a user has ro permissions.
  
Customer Information Center
    Shows all tickets for which a user has ro permissions.

Escalation Notifications
========================

When tickets approach or breach escalation thresholds, notifications are sent to recipients. By default:

- All agents with write permissions to the queeue
- All agents subscribed to the queue

.. seealso:: Further Information

    :ref:`ticket-notification configuration`


Escalation Workflow
********************

1. **Ticket Creation**: A new ticket is assigned to a queue or service with escalation settings.
2. **Timer Starts**: Escalation timers begin based on the ticket's creation or update time.
3. **Monitoring**: Agents and supervisors track tickets in the escalation view.
4. **Notifications**: If no action is taken, Znuny triggers notifications based on configured rules.
5. **Answer**: A first response is sent, stopping this timer.
6. **Update**: An update is sent, resetting this timer.
7. **Resolution**: The ticket is closed, stopping the escalation update timers.

.. mermaid:: 

    graph TD
        Start((Start))
        A[Answer]
        B[Update]
        C[Resolution]
        End((End))
       Start --> A
       A --> B
       B --> C
       C --> End

Tips for Effective Escalation Management
****************************************
- **Queue Response Time**: Define a first response time for each queue of entry.
- **Define SLAs Clearly**: Ensure escalation thresholds align with your team's response and resolution capabilities.