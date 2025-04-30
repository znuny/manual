.. _PageNavigation annexes_entity_type_reference_index:

Entity Type Reference
#####################

**What are Entity Types**

Entity types define and categorize different entities in the system. In Znuny, entity types are used to organize:

- **Auto-response** - Defines which response should be sent and limits selection in Queues <-> Auto-responses.

.. seealso::

    :ref:`pagenavigation admin_communication_autoresponses_types_index` 

- **Communication channel** - Indicates via which channel received the message.
- **LockType** - Determines Which lock type is applied.
- **SenderType** - Indicates the sender who initiated the communication.
- **StateType** - Indicates where in the system should the state be used.

.. seealso:: 

    :ref:`pagenavigation concepts_states_index` 

- **TemplateType** - Limits the selection of the template based on the front-end component.

.. seealso:: 

    :ref:`pagenavigation admin_communication_templates_index` 


Communication channels
**********************

In **Znuny**, communication channels are an essential part of the **ticketing system**. 
They define how customers and agents interact, ensuring efficient **message routing, tracking, and processing**. 

**What Are Communication Channels in Znuny?**

Communication channels are the **different ways** a ticket can be created, updated, or managed. These include:  

- **Email** - The most common channel.  
- **Internal (Customer Portal)** - Customers and Agent interaction with the portal, in the form of notes.
- **Phone** - Agents log calls as tickets for tracking.

**Where are the channels used**

Znuny is highly configurable, but the default channel usages is as follows.

+-----------------------+----------------------+-----------------------------------------------------------------+
| Communication Channel | Default: Sender Type | Remarks                                                         |
+=======================+======================+=================================================================+
| E-Mail                | Agent                | Used in AgentTicketForward                                      |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       |                      | Used in AgentTicketEmailOutbound                                |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       |                      | Used in AgentTicketCompose                                      |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       |                      | Used in AgentTicketEmail                                        |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       |                      | Used in AgentTicketBounce                                       |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       | System               | Used by the auto-response                                       |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       | Customer             | Used for follow-up mails.                                       |
+-----------------------+----------------------+-----------------------------------------------------------------+
| Phone                 | Customer             | AgentTicketPhone                                                |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       |                      | AgentTicketPhoneInbound                                         |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       | Agent                | AgentTicketPhoneOutbound                                        |
+-----------------------+----------------------+-----------------------------------------------------------------+
| Internal              | Customer             | CustomerTicketMessage                                           |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       |                      | CustomerTicketProcess                                           |
+-----------------------+----------------------+-----------------------------------------------------------------+
|                       | Agent                | AgentTicketActionCommon (All other masks where a Body is used.) |
+-----------------------+----------------------+-----------------------------------------------------------------+

Lock Types
***********
+-----------+---------+----------------------------------------------------------------+
| lock type | Used by | Used in                                                        |
+===========+=========+================================================================+
| lock      | Agent   | AgentTicketLock, AgentTicketBulk and screens requiring a lock. |
+-----------+---------+----------------------------------------------------------------+
| tmp_lock  | System  |                                                                |
+-----------+---------+----------------------------------------------------------------+
| unlock    | Agent   | AgentTicketLock, AgentTicketBulk and screens requiring a lock. |
+-----------+---------+----------------------------------------------------------------+


Sender Type
***********
+-------------+---------------------------------------------------------------------------------------------------------------------------------+
| Sender Type | Used in                                                                                                                         |
+=============+=================================================================================================================================+
| agent       | AgentTicketPhoneOutbound, AgentTicketEmail, AgentTIcketEmailOutbond, AgentTicketForward, AgentTicketCompose, AgentTicketProcess |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+
| system      | Auto-replies, Notifications und Web Services (depending on configuration)                                                       |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+
| customer    | AgentTicketPhone, AgentTicketPhoneInbound, CustomerTicketZoom, CustomerTicketMessage, CustomerTicketProcess                     |
+-------------+---------------------------------------------------------------------------------------------------------------------------------+
