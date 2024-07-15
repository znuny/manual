.. _PageNavigation admin_queues_index:

Adding a Team (Queue)
#####################

Queues are the basis for working with teams in Znuny. Queues contain tickets and build the permissions, in combination with groups and roles, for access to tickets. We’ve added groups, roles, and users and customer users to our system. Now it’s time to consider the queues which will contain our tickets. To add a new queue or manage a queue:

1. Navigate to Admin
2. Filter for or scroll to Queues
3. Click Add Queue
4. Set a name
5. Assign a parent queue (optional)
6. Set the group that is required to have access to the queue
7. Set an unlock time (optional)
8. Set the escalation first response time (optional)
9. Set the escalation update time (optional)
10. Set the escalation solution time (optional)
11. Set the follow-up options 
12. Define the ticket lock after follow-up (optional)
13. Choose the system address for outbound emails 
14. Choose the default signing key (optional)
15. Choose the standard salutation
16. Choose the standard signature 
17. Select the system calendar for escalation calculation (see ``TimeWorkingHours``)
18. Set the valid state
19. Add a comment (optional)
20. Save changes (optional)

Queue settings
**************


Notify before
    The notified before time is a percentage of time that is reached before a pre-notification event has been triggered. Upon triggering this pre notification event, a notification can be sent to anyone using the ticket notification system. Generally speaking, this notification will be sent to agents or managers.
Follow-up Option
    The follow-up option dictates what sh....e are three possible options *possible*, *reject* and *new ticket*. Possible, allows the ticket to be reopened. Reject denies the ticket to be reopened. The setting new ticket creates a new ticket and links the old ticket to the new ticket. Further follow-ups will always create a new ticket.
Ticket lock after follow up:
    This setting determines whether the ticket should be locked to the last known owner of the ticket, if a follow-up is received on a closed ticket and follow-ups are allowed.
System address
    The registered system address, which will be used as the sender within the queue.
Default sign key
    If PGP or S/MIME is active within the system, this will be the key that is chosen as the default signature key for this queue.
Salutation
    Salutation to be used with this queue When creating an email ticket, a new email outbound, or responding to or forwarding a ticket.
Signature
    Signature to be used with this queue When creating an email ticket, a new email outbound, or responding to or forwarding a ticket.
Calendar
    The system calendar to be used for calculation of escalation times. These calendars are configured within the system configuration tool. :ref:`pagenavigation admin_index_systemconfiguration` 
Validity
    If a queue is to be valid for selection within the front end.
Comment
    Additional comments for the administrator.


Parent Queue
    The parent queue and its permissions have no relevance to the new or updated queue. Setting a sub-queue is just a visual representation of a subordinate.
Group
    Only one group can be assigned to the queue. The user must have read-write permissions in this queue to see the queue within the queue view and other overviews.
Escalation times
    Escalation times are used to calculate the requirements based on your team’s commitment to service. The first response time is the time required to send the first external communication to the customer. The first response can be an external note, a phone call out or inbound, or an email. The communication must be marked as visible to the customer. The update time is the time between each contact with the customer. The solution time is the time between ticket creation and the first closing of the ticket.
Notify before
    The notified before time is a percentage of time reached before a pre-notification event has been triggered. Upon triggering this pre-notification event, a notification can be sent to anyone using the ticket notification system. Generally speaking, this notification will be sent to agents or managers.
Follow-up Option
    The follow-up option dictates which of the three options is possible: reject and new ticket. Possible, allows the ticket to be reopened. Reject denies the ticket to be reopened. The setting new ticket creates a new ticket and links the old ticket to the new ticket. Further follow-ups will always create a new ticket.
Ticket lock after follow-up:
    This setting determines whether the ticket should be locked to the last known owner of the ticket if a follow-up is received on a closed ticket and follow-ups are allowed.
System address
    The registered system address will be used as the sender for the queue.
Default sign key
    If PGP or S/MIME is active within the system, this will be the key chosen as the default signature for this queue.
Salutation
    Salutation to be used with this queue when creating an email ticket, a new email outbound, or responding to or forwarding a ticket.
Signature
    Signature to be used with this queue when creating an email ticket, a new email outbound, or responding to or forwarding a ticket.
Calendar
    The system calendar is used for the calculation of escalation times. These calendars are configured within the system configuration tool. System Configuration
Validity
    If a queue is to be valid for selection within the front end.
Comment
    Additional comments for the administrator.