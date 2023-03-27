.. _TransitionAction TicketArticleCreate:

Create an Article
#################

Summary
*******

This module allows you to create a ticket article.

The name of the transition action is :ref:`TicketArticleCreate <TransitionAction TicketArticleCreate>`

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

Base Configuration
===================

+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| Key                  | Example value                     | Description                                          | Mandatory                               |
+======================+===================================+======================================================+=========================================+
| SenderType           | agent                             | Defines the sender type.                             | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| IsVisibleForCustomer | 1                                 | Defines visibility.                                  | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| CommunicationChannel | Internal                          | Defines the channel of communication.                | no                                      |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| UserID               | 1                                 | The user ID one is used.                             | no, will override the logged in user id |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| ContentType          | text/html; charset=utf-8          | The content Type of the communication.               | yes, if no MimeType and Charset is used |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| MimeType             | text/html                         | The MIME Type of the communication.                  | no                                      |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| Charset              | utf-8                             | Only utf=8 should be used.                           | no                                      |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| HistoryType          | AddNote                           | The type of the history entry. Must be a valid type. | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| HistoryComment       | Added Note                        | A free text comment.                                 | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| From                 | Some Agent <email@example.com>    | The sender.                                          | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| To                   | Some customer <email@example.com> | The recipient.                                       | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| Subject              | Internal                          | Defines the channel of communication.                | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+
| Body                 | Some text                         | Plain text or HTML text based on content type.       | yes                                     |
+----------------------+-----------------------------------+------------------------------------------------------+-----------------------------------------+

Optional Choices
=================

Possible Sender Types
======================

* agent
* customer
* system

Possible Communication Channels
================================

* Internal
* Email
* Phone

Possible HistoryTypes
~~~~~~~~~~~~~~~~~~~~~

This is list of default valid types. Valid types are found in the database table ``ticket_history_types``

* NewTicket
* FollowUp
* SendAutoReject
* SendAutoReply
* SendAutoFollowUp
* Forward
* Bounce
* SendAnswer
* SendAgentNotification
* SendCustomerNotification
* EmailAgent
* EmailCustomer
* PhoneCallAgent
* PhoneCallCustomer
* AddNote
* Move
* Lock
* Unlock
* Remove
* TimeAccounting
* CustomerUpdate
* PriorityUpdate
* OwnerUpdate
* LoopProtection
* Misc
* SetPendingTime
* StateUpdate
* TicketDynamicFieldUpdate
* WebRequestCustomer
* TicketLinkAdd
* TicketLinkDelete
* SystemRequest
* Merged
* ResponsibleUpdate
* Subscribe
* Unsubscribe
* TypeUpdate
* ServiceUpdate
* SLAUpdate
* ArchiveFlagUpdate
* EscalationSolutionTimeStop
* EscalationResponseTimeStart
* EscalationUpdateTimeStart
* EscalationSolutionTimeStart
* EscalationResponseTimeNotifyBefore
* EscalationUpdateTimeNotifyBefore
* EscalationSolutionTimeNotifyBefore
* EscalationResponseTimeStop
* EscalationUpdateTimeStop
* TitleUpdate
* EmailResend
