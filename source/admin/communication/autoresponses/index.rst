.. meta::
   :description: Create Znuny auto responses for ticket events — configure auto-reply, auto follow-up, reject and new-ticket notifications sent to requesters and assigned to queues.
   :keywords: auto response, znuny auto reply, ticket auto response, auto follow-up, queue responses, email auto reply, automated customer response

.. _PageNavigation admin_communication_autoresponses_index:

Automatic Responses
###################

A response can be sent to the requester, as soon as a ticket is:

- Created
- Rejected
- Replied to after closed
- Receives a follow-up

.. note::
 	Reply after close (default reply/new ticket) is based upon the queue's follow-up settings.

Create a Response
******************

To create an auto response.

1. Navigate to Admin
2. Filter for or scroll to Auto Responses
3. Click Add Auto Response
4. Add a name
5. Add a subject
6. Add the body
7. Choose the type
8. Select the sender address
9. Set the validity
10. Add a comment
11. Save

.. _PageNavigation admin_communication_autoresponses_types_index:

Auto Response Types
===================

auto follow up
	When an update is received.
auto reject
	When a queue follow-up is set to reject.
auto remove
	Not used.
auto reply
	When a new mail is received.
auto reply/new ticket
	When a queue follow-up option is set to new ticket.


Assign Responses to Queues
***************************

1. Navigate to Admin
2. Filter for or scroll to Queues <-> Auto Responses
3. Choose a queue from the list of queues
4. Assign a response for one or more types

Manage Exceptions
*****************

In the system configuration, you can and should add exceptions to the rule.

Important system configuration settings are:

AutoResponseForWebTicketsTicket (default: active)
	Deactivate auto responses for tickets created in the frontend.
SendNoAutoResponseRegExp
	Configure which addresses should receive no auto response.

.. hint::
 	Auto-responses are also suppressed if the incoming message contains a loop-prevention header. Some automated emails are designed to skip auto-responses by default. Check the ticket history and communication log if needed.

.. seealso:: 

	:ref:`pagenavigation annexes_entity_management_index` for more information on how to manage entities. There is also information about import and export of entities. 