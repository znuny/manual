.. _PageNavigation concepts_priorities_index:

Ticket Priorities
#################

The ticket priority is one of the default and required ticket properties which:

- **Defines the level of urgency for a ticket** in the system.
- Augments **SLA (Service Level Agreements)** and and queue **escalation times**.
- Each ticket has **one priority** at a time, but it can be changed by agents based on circumstances.


Default Priorities
******************

Znuny comes with **five default priorities**:

+-------------------+------------------------------------------+-------------------+
| **Priority Name** | **Description**                          | **Default Color** |
+-------------------+------------------------------------------+-------------------+
| **1 very low**    | Non-urgent, informational tickets.       | #03C4F0           |
+-------------------+------------------------------------------+-------------------+
| **2 low**         | Minor issues, feature requests.          | #83BFC8           |
+-------------------+------------------------------------------+-------------------+
| **3 normal**      | Standard customer requests (default).    | #CDCDCD           |
+-------------------+------------------------------------------+-------------------+
| **4 high**        | Urgent issues that need quick attention. | #FFAAAA           |
+-------------------+------------------------------------------+-------------------+


**How Priorities Affect Ticket Processing**

1. **Sorting and Filtering**

- Agents can **sort tickets by priority** in overviews.
- Agents can **search or filter statistics** based on priorities.
  
2. **Workflow Automation**

- Generic agents, Web Service Requests or Responses and Transition Actions can **make priority adjustments**

Customizing Priorities
**********************

Administrators can **edit or add new priority levels** in the Znuny **Admin Panel**.

.. warning:: 
    
    Changing the name for the standard priority "3 normal" will result in a configuration change, and 
    possibly deployment of some additional addons which attempt to use this during installation as a default.
    Always check the logs and system configuration deployment state after installing an add-on.



Best Practices for Using Priorities
***********************************

- ✔ **Use clear priority definitions** that align with business needs.  
- ✔ **Train agents** on when to escalate or downgrade priorities.  
- ✔ **Automate priority assignments** where possible to reduce manual workload.  
