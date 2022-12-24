Managing Service Level Agreements
#################################
.. _PageNavigation admin_servicemanagement_servicelevels_index:

Service level agreements (SLA) give your services meaning by alarming users about thresholds for request processing and informing users and customers about the timely processing of requests.

Configure an SLA
****************

An SLA can be configured or edited under Admin > Service Level Agreements. Once a ticket has a service, an SLA can be applied where configured here. A service can be assigned to multiple SLAs. This makes escalations based on queue times obsolete. The SLA is applied to the ticket regardless of the queue. An SLA consists of:

Name
    The name of the SLA.
Service
    The SLAs assigned services.
Escalation First Response Time
    The time in minutes before the first response time is required. Additionally ,you can trigger a notification warning event at a certain percentage of the remaining escalation time.
Escalation Update Time
    The time in minutes before an update to the customer is needed. Additionally, you can trigger a notification warning event at a certain percentage of the remaining escalation time.
Escalation Solution Time
    The time in minutes before the solution is required (this can only be fullfilled by closing . Additionally, you can trigger a notification warning event at a certain percentage of the remaining escalation time.
Calendar
    The :ref:`working calendar <PageNavigation generalinformation_workinghours_index>` which is used for time calculations.
Comments
    Comments for the administrator.

.. note::

    SLA validation can delete an SLA when just the service is updated via a web service TicketUpdate operation, if the current SLA of the ticket does not contain the service updated by the web service.

.. important::

    If no calendar is set, no calendar is applied by the escalation calculation. This results in a 24*7*365 calendar.
