.. _PageNavigation concepts_states_index:

Ticket States
#############

Ticket states are a way to manage the workflow of tickets. Ticket states can be used to indicate the status of a ticket, such as new, open, closed, pending, etc. Ticket states can also be customized to suit different business needs and scenarios. For example, you can create ticket states for escalation, approval, feedback, or any other process that you want to track. States are typed within the system, which gives the system the capability of displaying multiple state names based on their type in different parts of the system or different purposes. A typical ticket Lifecycle would contain the following state changes:

.. mermaid::
    
    graph TD
        new --> open
        open <--> pa[pending auto]
        pa[pending auto] <--> cs[closed successful]
        open  <-->  pr[pending reminder]
        open <--> cs[closed successful]
        pr[pending reminder] <--> cs[closed successful]

State Types
***********

State types are important. They are the foundation of states and define a state's technical behavior. Often they allow the states to be selectively filtered and displayed where they are needed. For example, when closing a ticket, only states of state type closed appear.

+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| State Type       | Description                                                                                                                                             |
+==================+=========================================================================================================================================================+
| new              | Typically only automatically set for new tickets.                                                                                                       |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| open             | Tickets with a states that have this state type are typically in progress by an agents. Also indicates the last contact/article came from the customer. |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| pending reminder | Defines states that are able to create a pending reminder notification.                                                                                 |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| pending auto     | A state of this state type can change the state after the pending time has been reached                                                                 |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| closed           | This state type defines states where the ticket's processing is finished.                                                                               |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| merged           | Internal use, reserved.                                                                                                                                 |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| removed          | Not used, required for backward compatibility.                                                                                                          |
+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

.. tip::

    Use the state types to match your business's use case. E.g., “pending order,”, type pending reminder, when you send a quote to a customer. Or “closed wo/ customer feedback”, type closed, to record when you closed a ticket where the customer’s feedback is missing. 


.. important:: 
  
  States of state type new will not be selectable by the users. As soon as a communication with the customer has been made, the state will change to a non-new state type. This change is forced in:

  - Taking a phone call with the customer user (AgentTicketPhoneInbound)
  - Making a phone call with the customer user (AgentTicketPhoneOutbound)
  - Writing a new outbound e-mail (AgentTicketEmailOutbound)
  - Replying to an e-mail article (AgentTicketCompose)
  - Bouncing  the ticket (AgentTicketBounce)
  - Forwarding an article of the ticket (AgentTicketForward)
  - Merging the ticket to another ticket (AgentTicketMerge)
  - Setting the ticket pending (AgentTicketPending)
  - Closing the ticket (AgentTicketClose)

  In other screens, the state can be added, with a default state i. e. `Ticket::Frontend::AgentTicketBulk###StateDefault`. 
  This will also force a state change to a state of a non-new state type.
