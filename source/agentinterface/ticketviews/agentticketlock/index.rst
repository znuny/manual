Lock/Unlock a Ticket
####################
.. _PageNavigation ticketviews_agentticketlock:

Locking a ticket makes you the owner of the ticket. This ownership and lock state indicates that no other agent needs take action.

.. important::

    Ticket locking is automatic when accessing communication screens or when ownership is changed. Ticket locking is configurable by the administrator.

Select *Lock* or *Unlock* from the :ref:`ticket menu <PageNavigation ticketviews_agentticketzoom_ticketmenu>`. This action is immediate.

Lock states
***********

Distinct lock states indicate the different stages of the locking mechanism. These states are *lock*, *unlock*, and *tmp_lock*.

Lock
    This state indicates that ticket processing is in progress by the assigned agent. It prevents actions from taking place without the actor taking ownership of the ticket.

Unlock
    This state indicates that the owner stated on the ticket is the last actor. Any person with write permissions on this ticket can now take action.

tmp_lock
    This state indicates to the system that the current owner of the ticket should not be changed. This state prevents other users from locking the ticket during critical operations by another user. This state is neither visible nor can it be selected by the user.
