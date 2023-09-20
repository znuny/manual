Process Quick Start (Ready2Adopt)
#################################
.. _PageNavigation processmanagement_readytoadopt_index:

To help you start with processes, the framework and other add-ons may include Ready2Adopt processes. These processes can be installed with the click of a button and bring all the necessary elements to run out-of-the-gate. You can start using the process (adopt) with minimal adaptation. Let's look into how to do this.


Application for Leave
*********************

.. image:: images/application_for_leave_process_map.png
    :alt: Application for Leave Process Map

Installing this process will deliver the following dynamic fields and settings:

Pre-Requisites
==============

You must activate ``Ticket::Responsible`` to use the process as designed.

Automatic Configuration Changes
===============================

**Dynamic Fields:**

+----------------------------+----------------------+------------+----------------------------------------------------------------+
| Name                       | Label                | Field type | Comment                                                        |
+============================+======================+============+================================================================+
| PreProcApplicationRecorded | Application Recorded | Text       | A date field for date the application was recorded by          |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcDaysRemaining       | Days Remaining       | Text       | The total days remaining.                                      |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcVacationStart       | Vacation Start       | Date       | The date requested for the start of Vacation                   |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcVacationEnd         | Vacation End         | Date       | The date requested to end vacation.                            |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcDaysUsed            | Days Used            | Text       | The total vacation days used.                                  |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcEmergencyTelephone  | Emergency Telephone  | Text       | The emergency contact telephone number.                        |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcRepresentationBy    | Representation By    | Text       | The person to represent the employee during absence.           |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcProcessStatus       | Process Status       | Text       | A hdiden field to help control the workflow of the pocess.     |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcApprovedSuperior    | Approved Superior    | Dropdown   | The decision of the supervisor.                                |
+----------------------------+----------------------+------------+----------------------------------------------------------------+
| PreProcVacationInfo        | Vacation Info        | TextArea   | A free text area to add additional information to the request. |
+----------------------------+----------------------+------------+----------------------------------------------------------------+

**Settings Changed:**

The process modifies the following setting ``Ticket::Frontend::AgentTicketZoom###ProcessWidgetDynamicFieldGroups``.

*Group Name:*

Application for Leave - Approval and HR data

*Visible Fields:*

- PreProcApprovedSuperior
- PreProcApplicationRecorded
- PreProcVacationInfo

*Group Name:*

Application for Leave - Request Data

*Visible Fields:*

- PreProcVacationStart
- PreProcVacationEnd
- PreProcDaysUsed
- PreProcDaysRemaining
- PreProcEmergencyTelephone
- PreProcApprovedSuperior
- PreProcVacationInfo

- Ticket::Frontend::AgentTicketZoom###ProcessWidgetDynamicField

Process description
===================

An agent or customer can start this process. If started by an agent, the customer must be chosen by the agent. If started as a customer, the customer is the logged-in user.

The process collects data about the leave request and assigns it to a supervisor. The ticket will automatically message the supervisor and is set to pending for twenty-four hours. After that, reminder emails will be sent to the supervisor. When denied, the process will end. When approved, the process will set the ticket back to pending seven days and await further action. After that, messages will be sent as a reminder. After the vacation is recorded as filed, the ticket will close.

Adaptation
==========

We recommend the following adaptations.

**Notifications:**

The application goes through some different states which can be used to configure notifications. Set up a ticket notification based on the event ``TicketDynamicFieldUpdate_<FIELDNAME>``.

+-----------------------------------------+-----------------------------------------------+-----------------------------------------+
| Value                                   | Recommended Recipient                         |                                         |
+=========================================+===============================================+=========================================+
| Values filled                           | Application is recorded and awaiting approval | Agent who is responsible for the ticket |
+-----------------------------------------+-----------------------------------------------+-----------------------------------------+
| yes                                     | Application is approved.                      |                                         |
+-----------------------------------------+-----------------------------------------------+-----------------------------------------+
|                                         | Application denied                            |                                         |
+-----------------------------------------+-----------------------------------------------+-----------------------------------------+
| DynamicField_PreProcApplicationRecorded | yes                                           |                                         |
+-----------------------------------------+-----------------------------------------------+-----------------------------------------+

**Transition Actions:**

It is recommended to create a transition action to set specific ticket data like:

Mandatory:

- Queue

Optional:

- Type
- Priority

**Activities and Activity dialogs:**

You may want to add, remove, or change visibility on some dialogs. You are welcome to do this, or expand on the process using your own activities and activity dialogs.
