.. _PageNavigation concepts_locking_index:

Ticket Lock
############


What is Ticket Locking
**********************

Znuny uses a locking mechanism to ensure that only one agent works on a ticket at a time. When an agent is handling a ticket, the ticket is "locked" to that agent - no other agent can respond to it, move it, or change its priority until the lock is released.

How it Works
************
Locking a ticket makes you the **owner** of that ticket, signaling that you're responsible for it and no one else needs to take action on it. Znuny automatically locks tickets in common scenarios - for example, as soon as you open a reply or phone call screen to communicate with the customer, the system will lock the ticket to you Similarly, if you assign a ticket to yourself (changing ownership), the system can lock it for you immediately. This lock remains in place until you or the system unlocks it. You can also lock or unlock a ticket manually at any time using the *Lock/Unlock* option in the ticket's menu.

Lock States
***********

A ticket can be in one of two main lock states:

- "locked"
- "unlocked" 

.. note::

  A *tmp_lock* state also can be used briefly during certain operations, but agents don't interact with that
  
**Definition of Lock States**

locked
    The ticket is currently being worked on by the **owner**. 
unlocked
    The ticket is available and needs attention.
    
.. important::

    Regardless of **ownership** an **unlocked** ticket requires attention and should not be ignored even when the ticket data still shows an **owner**. 
    
Viewing the Lock State
**********************

Ticket Details
    In Znuny's ticket detail view (AgentTicketZoom), the **Ticket Information** panel shows the lock status and owner.
Ticket Dashboard
    In Znuny's dashboard elements, the column for lock can be assigned to the list of elements. (see :ref:`pagenavigation agentinterface_dashboards_widget_settigs` )
Ticket Overview Small
    In Znuny's overview settings for the small overview (see :ref:`pagenavigation agentinterface_overviews_column_settings` ), the column for lock can be assigned to the list of elements.


Purpose of Locking
******************

Ticket locking

- prevents collisions and confusion
- provides clarity
- manages expectations
- updates accountability
- streamlines workflows

Configuration
*************

Administrators can tailor the locking behavior to fit the team's needs. By default, Znuny requires a lock on critical actions like replying to emails or moving a ticket between queues. However, which screens/actions require a lock is configurable in the system settings. 

**An example**

An admin can decide that setting a ticket's priority or adding a note should also lock the ticket. These settings (`Ticket::Frontend::<Action>###RequiredLock`) fine-tune when a ticket lock is required, ensuring the mechanism aligns with your processes.

## Best Practices for Ticket Locking

.. important::

    Using ticket locking effectively will improve your team's efficiency and avoid conflicts. 
    
Best Practices for Ticket Locking
**********************************

- **Lock tickets when working on them:** Whenever you begin working on a ticket, make sure you've locked it.

- **Don't leave tickets unnecessarily locked:** If you realize you won't be able to continue working on an issue, **unlock the ticket** so that others can pick it up.

- **Use auto-unlock features:** Leverage Znuny's configuration to automatically unlock tickets in appropriate scenarios. Admins can set an **unlock timeout** for queues (e.g. tickets unlock after X minutes/hours of inactivity) or have tickets auto-unlock when certain events occur.

- **Monitor your locked tickets:** Keep an eye on the tickets you have locked. Znuny provides a "My Locked Tickets" view and dashboard indicators that show how many tickets you currently have locked. If you find a ticket locked to you that you're not actively working on, consider unlocking it to let others assist. This practice helps balance workload and keeps tickets from slipping through the cracks.

- **Team awareness and backup:** If an agent with locked tickets will be unavailable (due to vacation, illness, etc.), have a plan to handle their tickets. Supervisors or admins can use overviews to find all locked tickets (including those locked by other agents.

- **Educate agents about locking:** Ensure your team is trained on what the lock states mean and how to use them. Every agent should know that a "locked" ticket is being handled by someone, and an "unlocked" ticket is open for action. They should also know **how to lock** a ticket (by taking ownership or using reply) and **how to unlock** (via the Unlock action or finishing the workflow) when appropriate. By sharing the purpose behind ticket locking and the agreed team protocols, you avoid misunderstandings like two people accidentally working the same ticket or tickets being left in limbo.

- **Use the "Responsible" feature (** *if needed* **):** Znuny has an optional concept of *responsible* agent separate from the lock/owner. If configured, you can assign a responsible person in addition to the owner, which allows that person to oversee or contribute to the ticket without breaking the lock. This can be useful for mentorship or complex issues where one agent leads but another is supervising. Use this feature judiciously - it doesn't replace locking, but rather adds flexibility for teamwork (essentially giving a ticket two designated people: one primary owner (locked) and one responsible backup).


.. important:: 
    
    **Avoid disabling locking entirely** - While Znuny allows tickets to be unlocked and even has settings to view unlocked vs locked tickets, it's usually best to keep the locking system in place rather than trying to work with everything unlocked. Locking exists to protect your workflow.

Typical Workflow
****************

This workflow shows how a ticket moves through being unlocked (in the queue), to locked (while an agent works on it), and back to unlocked (when released or handed over), until it's finally resolved. Every step of the way, Znuny's ticket locking ensures **clear ownership and smooth transitions** between team members.

1. **Ticket arrives (unlocked):** A new customer inquiry comes into the system, creating a ticket. Initially, this ticket is **unlocked** and visible to the support team in the queue. The initial owner is OwnerID(1) or the agent who created the ticket via Email or Telephone Ticket. The unlocked ticket shows up in views so that agents know it needs attention.

**Scenario 1**
    Suppose *Agent A* decides to handle this ticket. Agent A opens the ticket and clicks "Pending" to reserve the ticket and adds a note and a date when the issue will be handled. The moment Agent A begins this action, Znuny automatically **locks the ticket to Agent A**. At this point, Agent A becomes the owner of the ticket, and the ticket's status changes to "locked." Agent A can see on the ticket info panel that it's locked to them, and other agents will see that the ticket is now owned and locked by Agent A.

**Scenario 2**
    Suppose Agent A writes a response via the *Reply* or *Reply all* function. The ticket is still locked to Agent A after sending the reply (by default, sending a reply doesn't immediately unlock it). Agent A might set the ticket's state to "closed" or "pending" depending on the situation. Throughout, the lock remains, indicating Agent A is still the one handling it.

.. important::
    
    If Agent A had instead decided not to send a reply and canceled the action, Znuny would have unlocked the ticket again so that it returns to the open pool with its previous owner or OwnerID(1).

1. **Deciding to keep or release the lock:** 

**Scenario 1**
    For example, if the ticket is now waiting for the customer's reply (perhaps set to a "Pending customer" state), Agent A may keep the ticket locked to themselves. They remain the owner and will follow up when the customer responds. The ticket stays out of the general queue of unlocked tickets (so other agents won't pick it up), since Agent A is taking responsibility for the next steps.

**Scenario 2** 
    Agent A can **unlock the ticket** so that it becomes available to others. This might be done manually by clicking "Unlock" (maybe after setting the ticket to a workable state like "open" if waiting on someone else), or automatically: for instance, if Agent A moves the ticket to a different queue or to another agent, Znuny can auto-unlock it as part of that move. 

3. **Another agent takes over (if unlocked):** Now that the ticket is unlocked, *Agent B* sees it as a new item needing attention. Agent B opens the ticket and, by doing so, locks it to themselves (Agent B becomes the new owner). Agent B can now work on the ticket (e.g., provide the expert help needed). From this point, the locking cycle repeats: as long as Agent B has it locked, others won't interfere. When Agent B is done, they might close the ticket or unlock it again if further actions are needed by someone else. Throughout the process, the ticket's history will record these lock/unlock events and owner changes (e.g., "Lock - Agent A", "Unlock - Agent A", "Lock - Agent B", etc., along with timestamps).

4. **Resolution and finish:** Once the ticket is solved and marked closed, it usually will unlock. At this stage, all agents can see and search for the ticket.

