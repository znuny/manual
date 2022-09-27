Event Reference
################
.. _PageNavigation annexes_event_reference_index_event_reference:

In this annex, you find a list of all events recorded by the system. These events appear in multiple areas of the software as a dropdown selection field, including but not limited to generic agents and a . As these.Events are not usable in all areas of the software, they are listed according to their functionality.

Table of Events
***************

The table of events is for a default installation. Other events may be included by extensions (Packages) added to the system such as ITSM Configuration Management.

+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| Event Name                          | Event Description                                                                                         | Usable in                                                       |
+=====================================+===========================================================================================================+=================================================================+
|| ArticleBounce                      || When an article is bounced.                                                                              || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleCreate                      || Every time an article is created.                                                                        || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| ArticleCustomerNotification         | Every time a customer notification is sent.                                                               | :ref:`b <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>`  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleUpdate                      || Not usable by an administrator.                                                                          || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleSend                        || Every time an article send event is triggered, regardless of the recipient.                              || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleAutoResponse                || Every time an auto response is sent.                                                                     || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleFlagSet                     || Every time an flag is set.                                                                               || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleFlagDelete                  || Every time an article flag is unset.                                                                     || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleEmailSendingQueued          || Every time an email is queued for sending.                                                               || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleEmailSendingSent            || Every time a queued mail is sent successfully.                                                           || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleEmailSendingError           || Every time sending a mail fails.                                                                         || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| ArticleCreateTransmissionError      | Whan email transmission fails during an article create.                                                   | :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>`  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| ArticleUpdateTransmissionError      | When email transmission fails during an article update.                                                   | :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>`  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| ArticleDynamicFieldUpdate          || When a dynamic field of type article is set to a new value.                                              || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| ArticleAgentNotification            | When an agent notification is triggered.                                                                  | :ref:`b <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketCreate                       || Every time a ticket is created.                                                                          || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketDelete                       || When a ticket is deleted. Ticket deletion can only be performed via CLI or using the Generic Agent.      || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketTitleUpdate                  || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketUnlockTimeoutUpdate          || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketQueueUpdate                  || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketTypeUpdate                   || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketServiceUpdate                || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketSLAUpdate                    || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketCustomerUpdate               || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketPendingTimeUpdate            || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketLockUpdate                   || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketArchiveFlagUpdate            || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketStateUpdate                  || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketOwnerUpdate                  || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketResponsibleUpdate            || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketPriorityUpdate               || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| HistoryAdd                         || Every time a history entry is made. Never use this, as a history entry is always made.                   || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| HistoryDelete                      || Every time a history entry is deleted.                                                                   || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Not usable by an administrator.                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketAccountTime                  || Every time an agent enters a time unit.                                                                  || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketMerge                        || Every time a ticket is merged.                                                                           || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketSubscribe                    || Every time a user subscribes to a ticket.                                                                || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketUnsubscribe                  || Every time a user un-subscribes to a ticket.                                                             || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketFlagSet                      || Ever time a ticket flag is set.                                                                          || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketFlagDelete                   || Every time a ticket flag is unset.                                                                       || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Should only be used with extreme caution, as this can cause a loopback and/or mail flood.                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationResponseTimeNotifyBefore || Every time a ticket has reached its first response warning time.                                         || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationUpdateTimeNotifyBefore   || Every time a ticket has reached its update warning time.                                                 || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationSolutionTimeNotifyBefore || Every time a ticket has reached its solution warning time.                                               || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationResponseTimeStart        || Every time a ticket has breached its first response time.                                                || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationUpdateTimeStart          || Every time a ticket has breached its update time.                                                        || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationSolutionTimeStart        || Every time a ticket has breached its solution time.                                                      || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationResponseTimeStop         || Every time the escalation has stopped.                                                                   || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationUpdateTimeStop           || Every time the escalation has stopped.                                                                   || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| EscalationSolutionTimeStop         || Every time the escalation has stopped.                                                                   || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Set on a queue or service level basis accounting for working hours.                                      ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationNewTicket              || Every time a new ticket notification is triggered.                                                       || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationFollowUp               || Every time a ticket receives a follow-up.                                                                || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationLockTimeout            || Every time a ticket is unlocked because of overdue.                                                      || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || This time is in minutes per queue setting.                                                               ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationOwnerUpdate            || Every time an owner is updated.                                                                          || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationResponsibleUpdate      || Every time a responsible is updated.                                                                     || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Activate ``Ticket::Responsible``                                                                         ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationAddNote                || Every time a note is added.                                                                              || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Collides with ArticleCreate.                                                                             ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationMove                   || Every time the queue is changed.                                                                         || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationPendingReminder        || Every time a ticket reaches it's pending time.                                                           || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationEscalation             || Every time an escalation notification is triggered.                                                      || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationEscalationNotifyBefore || Every time a escalation warning is triggered.                                                            || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| NotificationServiceUpdate          || When the ticket attribute is updated.                                                                    || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    ||                                                                                                          ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketAllChildrenClosed            || When all children of a ticket are marked as closed.                                                      || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || Configurable in the system configuration.                                                                ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|| TicketDynamicFieldUpdate_*         || Every time a specific dynamic field is updated.                                                          || :ref:`a <EventIndex FrontEnd>`, :ref:`b <EventIndex FrontEnd>` |
||                                    || All dynamic fields will automatically be listed in the event list.                                       ||                                                                |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| AppointmentCreate                   | When an appointment is created.                                                                           | :ref:`c <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| AppointmentUpdate                   | When an calendar appointment is updated.                                                                  | :ref:`c <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| AppointmentDelete                   | When an appointment is deleted.                                                                           | :ref:`c <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| AppointmentNotification             | When an appointment notifications is sent.                                                                | :ref:`c <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| CalendarCreate                      | When a calendar is created.                                                                               | :ref:`c <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| CalendarUpdate                      | When a calendar is updated. An update is not creating an appointment, but changing the calendar settings. | :ref:`c <EventIndex FrontEnd>`                                  |
+-------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+


Graphical User interface Reference
**********************************
.. _EventIndex FrontEnd:

List of where the event is an available trigger:

a. Ticket Notifications
b. Generic agents
c. Appointment Notifications
