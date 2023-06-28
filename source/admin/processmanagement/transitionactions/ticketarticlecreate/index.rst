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

+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| Key                  | Example value                     | Description                                           | Mandatory                               |
+======================+===================================+=======================================================+=========================================+
| Body                 | Some text                         | Plain text or HTML text based on content type.        | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| Charset              | utf-8                             | Only utf=8 should be used.                            | no                                      |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| CommunicationChannel | Internal                          | Defines the channel of communication.                 | no                                      |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| ContentType          | text/html; charset=utf-8          | The content Type of the communication.                | yes, if no MimeType and Charset is used |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| DynamicField_NameX   | value                             | Add a dynamic field of object article to the article. | no                                      |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| From                 | Some Agent <email@example.com>    | The sender.                                           | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| HistoryComment       | Added Note                        | A free text comment.                                  | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| HistoryType          | AddNote                           | The type of the history entry. Must be a valid type.  | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| IsVisibleForCustomer | 1                                 | Defines visibility.                                   | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| MimeType             | text/html                         | The MIME Type of the communication.                   | no                                      |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| SenderType           | agent                             | Defines the sender type.                              | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| Subject              | Internal                          | Defines the channel of communication.                 | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| To                   | Some customer <email@example.com> | The recipient.                                        | yes                                     |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| UserID               | 1                                 | The user ID one is used.                              | no, will override the logged in user id |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+
| UnlockOnAway         | 1                                 | Unlocks ticket when owner is away.                    | no                                      |
+----------------------+-----------------------------------+-------------------------------------------------------+-----------------------------------------+

.. versionadded:: 7.0.7

    Add a dynamic field when creating an article. ``DynamicField_NameX``

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
