What are States
###############

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

State types are important. They are the foundation of states and define a state's technical behaviour. Often they allow the states to be selectively filtered and displayed where they are needed. For example, when closing a ticket, only states of state type closed appear.

.. list-table:: Overview of State Types
   :widths: 30 70
   :header-rows: 1

   * - State Type
     - Description
   * - new
     - Typically only automatically set for new tickets and indicates thta no agent has work on a ticket with this state type.
   * - open
     - Tickets with a states that have this state type are typically in progress by an agents. Also indicates the last contact/article came from the customer.
   * - pending reminder
     - Defines states that are able to create a pending reminder notifcation.
   * - pending auto
     - A state of this state type can change the state after the pending time has been reached.
   * - closed
     - This state type defines states where the ticket's processing is finished. 

.. tip::

    Use the state types to match your business's use case. E.g., “pending order,”, type pending reminder, when you send a quote to a customer. Or “closed wo/ customer feedback”, type closed, to record when you closed a ticket where the customer’s feedback is missing. 

