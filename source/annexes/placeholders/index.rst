Placeholder Tags
################
.. _PageNavigation annexes_placeholders_index:

Placeholders can be used in many parts of the system to represent the use-case-specific information retrieved from respective ticket data.

* :ref:`Auto Responses <PageNavigation admin_communication_index>`
* :ref:`Appointment Notifications <PageNavigation admin_communication_index>`
* :ref:`Salutations <PageNavigation admin_communication_index>`
* :ref:`Signatures <PageNavigation admin_communication_index>`
* :ref:`Ticket Notifications <PageNavigation admin_communication_index>`
* :ref:`Ticket Templates <PageNavigation admin_communication_index>`
* :ref:`Process Management Transition Actions <PageNavigation admin_processmanagement_index>`
* :ref:`Web Service Transport <PageNavigation admin_webservices_index>`
* :ref:`Web Service Mapping <PageNavigation admin_webservices_index>`

Ticket Attributes
******************

Ticket attributes are used with the placeholder <OTRS\_TICKET\_\*>. Replace "*" with the term of the desired attribute from the list below.

Age
    Age of ticket in seconds
Changed
    The timestamp of the last ticket changed
ChangedBy
    The ID of the agent who changed the ticket the last
CreateBy
    The ID of the agent who created the ticket
Created
    Timestamp when the ticket was created
CustomerID
    The ID of the customer/customer company
CustomerUserID
    The ID of the customer user
Lock
    Value of the ticket lock
Owner
    Login of the ticket’s owner
OwnerID
    The ID of the owner
Priority
    Priority name
Queue
    Name of the current queue
Responsible
    Name of the responsible
Service
    Name of the service
SLA
    Name of the Service Level Agreement
State
    Name of the state
StateType
    Name of the state type
TicketID
    Ticket ID
TicketNumber
    Ticket number
Title
    Title
Type
    Ticket type

.. note::

    For the most attributes it is also possible to access their ID like TicketID, StateID, PriorityID, LockID, QueueID, TypeID, SLAID, etc.

Dynamic Fields
**************

<OTRS_TICKET_DynamicField\_\*>
    Returns the value of a field, for fields with key/value pairs like dropdown, the key is returned.
<OTRS_TICKET_DynamicField\_\*_Value>
    Returns the value for fields with key/value pairs, e.g. for dropdown fields.

Escalations
***********

Escalation details are used like ticket attributes with the placeholder <OTRS_TICKET\_\*> Attributes with the term WorkingTime are calculated with considering the assigned calendar.


EscalationDestinationIn
    Time until the ticket escalates

.. note::

    Example:
    1h 4m

EscalationDestinationDate
    Timestamp when the ticket escalates

.. note::

    Example:
    2009-02-14 18:00:00 (PST)

EscalationTimeWorkingTime
    Working time in seconds until the escalation
EscalationTime
    Seconds until the escalation of the next escalation type – first response, update, or solution time
FirstResponseTimeDestinationDate
    Date of the first response

.. note::

    Example:
    2019-04-12 14:25 (CEST)

FirstResponseTimeWorkingTime
    Working time in seconds until the first response escalation
FirstResponseTime
    Seconds until the first response
UpdateTimeDestinationDate
    Date of the update escalation

.. note::

    Example:
    2017-12-23 09:42 (Europe/Berlin)

UpdateTimeWorkingTime
    Working time in seconds until the update escalation
UpdateTime
    Seconds until the update escalations
SolutionTimeDestinationDate
    Date of the solution escalation

.. note::

    Example:
    2018-07-12 22:00 (UTC)

SolutionTimeWorkingTime
    Working time in seconds until the solution escalation
SolutionTime
    Seconds until the solution escalation

Article Attributes
*******************

These placeholders are available for the last article of an agent or customer user. Replace the "*" with AGENT or CUSTOMER.

<OTRS\_\*_From>
    The sender of the article
<OTRS\_\*_To>
    Recipient(s) of the article
<OTRS\_\*_Cc>
    Recipients (CC) of the article
<OTRS\_\*_Subject>
    Subject
<OTRS\_\*_Subject\[20\]
    Subject, limited to a specific number of character
<OTRS\_\*_Body>
    Body of the article
<OTRS\_\*_Body\[5\]
    Specific amount of lines of the article’s body

.. note::

    Remove the [n] to get all lines or characters of the body or subject.

<OTRS\_CUSTOMER\_REALNAME>
    To get the name of the ticket's customer user (if given).

User (Agent)
**************

This placeholder may vary for every single instance. Replace the "*" with one of these values: UserFirstname, UserLastname, UserEmail, UserLogin, UserID, UserFullname. More attributes are possible and can be found in the session data from agents.

<OTRS_OWNER\_\*>
    Values of the owner <OTRS_OWNER_UserFullname>
<OTRS_CURRENT\_\*>
    Value of the agent who performed the current action <OTRS_CURRENT_UserLogin>
<OTRS_RESPONSIBLE\_\*>
    Value of the responsible <OTRS_RESPONSIBLE_UserFirstname>

Customer User and Customer
***************************

These placeholders may also differ for every instance. Possible values for * in the placeholder <OTRS_CUSTOMER_DATA\_\*> can be found in the first column of the CustomerUser and CustomerCompany mapping. If needed contact the support for help. The table shows only some examples:

<OTRS_CUSTOMER_DATA_UserLastname>
    The last name of the customer user
<OTRS_CUSTOMER_DATA_UserPhone>
    Phone number
<OTRS_CUSTOMER_DATA_DynamicField_Extra>
    Example for a dynamic field with the identifier Extra
<OTRS_CUSTOMER_DATA_CustomerCompanyName>
    Company name

Automatic Responses
*******************

There are some special tags which you can use especially for automatic responses. These you parse the e-mail and give you some additional tags for use.

<OTRS\_CUSTOMER\_SUBJECT\[20\]>
    To get the first 20 character of the subject.
<OTRS\_CUSTOMER\_EMAIL\[5\]>
    To get the first 5 lines of the email.
<OTRS\_CUSTOMER\_REALNAME>
    To get the name of the ticket's customer user (if given).
<OTRS\_CUSTOMER\_\*>
    To get the article attribute ( e. g. <OTRS\_CUSTOMER\_From>, <OTRS\_CUSTOMER\_To>, <OTRS\_CUSTOMER\_Cc>, <OTRS\_CUSTOMER\_Subject>, <OTRS\_CUSTOMER\_BODY>).

System Configuration
*********************

It doesn't make sense to use all possible configuration settings in templates, but they can also be used. These are the most useful.

<OTRS\_CONFIG\_FQDN>
    FQDN of your instance

.. note::

    Example:
    test.example.com

<OTRS\_CONFIG\_HttpType>
    Type of HTTP connection

.. note::

    Example:
    https

<OTRS\_CONFIG\_TicketHook>
    The ticket hook.

Appointment Calendar
********************

These placeholders are available for calendar notification.

<OTRS\_APPOINTMENT\_TITLE>
    Title of the appointment, limitation with [xx] is possible

<OTRS\_APPOINTMENT\_STARTTIME>
    Start of the appointment

<OTRS\_APPOINTMENT\_DESCRIPTION>
    Appointment description

<OTRS\_APPOINTMENT\_CALENDARNAME>
    Calendar name

<OTRS\_APPOINTMENT\_COLOR>
    HTML color code of the calendar

.. important::

    When using templates of the type Create, not every attribute can be used. The reason is that there is still no ticket created. Instead of e.g. <OTRS_OWNER_FullName> use <OTRS_CURRENT_Fullname>. Placeholders from the System Configuration are always available.

Placeholder Translation
***********************

If the user language is known, and there is a translation available for the string, then the values are translated.

Dates and Time
**************

If the time zone of the recipient is known, then dates and date/times are converted into the correct time zone.
