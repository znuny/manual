.. meta::
   :description: Ticket priorities in Znuny — five default priority levels from very low to very high, their colors, how they interact with SLA escalations and how to customize them.
   :keywords: znuny priorities, ticket priority, priority levels, priority color, sla priority, ticket urgency

.. _PageNavigation concepts_priorities_index:

Priorities in Znuny
###################

In **Znuny**, **priorities** determine the urgency and importance of a ticket. 
They aid agents enhancing the ticket with a visual cue (color) about critical issues.

**Features of the Priorities**

- Defines the level of **urgency** for an issues.
- Act an an enhancement to the assigned **SLA (Service Level Agreements) enforcement**, or queue assigned **escalation times**.
- Each ticket has **one priority** at a time, but it can be changed by agents based on circumstances.

Default Priorities
*******************

Priorities can be added or modified as needed. 
As usual it's not possible to remove this type of entity for auditing pur.

Znuny comes with **five default priorities**:

+-------------------+-------------------------------------------------------+--------------------+
| **Priority Name** | **Description**                                       | **Standard Color** |
+===================+=======================================================+====================+
| **1 very low**    | Non-urgent, informational tickets.                    | #03C4F0            |
+-------------------+-------------------------------------------------------+--------------------+
| **2 low**         | Minor issues, feature requests.                       | #83BFC8            |
+-------------------+-------------------------------------------------------+--------------------+
| **3 normal**      | Standard customer requests (default).                 | #CDCDCD            |
+-------------------+-------------------------------------------------------+--------------------+
| **4 high**        | Urgent issues that need quick attention.              | #FFAAAA            |
+-------------------+-------------------------------------------------------+--------------------+
| **5 very high**   | Critical incidents that must be resolved immediately. | #FF505E            |
+-------------------+-------------------------------------------------------+--------------------+

.. note::
 
 These priorities can be **renamed, reordered, or customized** based on business needs.

Affect Ticket Processing
************************

**Sorting and Filtering**

- Agents can **sort tickets by priority** in overviews.
- Agents can **search for tickets by priority**.

**Workflow Automation**

- Administrators can **trigger events**, based on specific priorities.
  - Priority change
  - Notifications
  - Web service events

Changing Priorities in Znuny
****************************

1. Manually by Agents

- Select *Priority* from the ticket action menu.
- Select the priority in at ticket creation or in any other screen where configured.

2. Automatically via Triggers

- Generic Agents
- Web Service Request or Invoker Responses
- Process Management Activity Dialogs
