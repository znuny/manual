Processing External Ticket Numbers
##################################

By default, it's only possible to parse the ticket number in the format provided by the software: ticket hook, ticket hook divider, and then, based on your number generator, the appropriate number. In some special cases, you should recognize external ticket numbers and connect them to your own tickets. This will allow your customer users to use either ticket numbers when communicating with your service team. This makes it much easier for your users and also allows you to connect to external service desks and record both ticket numbers in the same ticket.

You'll first have to identify where the emails are coming from. That helps in the case of obtaining external ticket numbers from a service desk or any other known email address. It is also possible to form a regular expression to parse all incoming emails as well. Once you've identified this, you'll have to determine the ticket number because you'll need a regular expression to parse the number. Once you have both items, we can continue with the system configuration and configure the system to parse the emails for this ticket number.

See :ref:`pagenavigation admin_system_configuration_index`.

Configure Your System
*********************

It is possible to have up to six external ticket number recognition filters. Here we will configure the first one by activating the module that allows us to look for follow ups and configuring the first external ticket number recognition filter.

- Create a dynamic field to store the external ticket number.

See :ref:`pagenavigation admin_dynamicfields_index`

.. tip:: 

   If the external system has a web interface you can create a link in the dynamic field configuration. 

- Search for the following setting and activate it: **PostMaster::CheckFollowUpModule###0600-ExternalTicketNumberRecognition**
This filter will check for the external ticket number and add the email to an existing ticket if there is a match.

- Search for the following setting and configure it appropriately. Here is an example: **PostMaster::PreFilterModule###000-ExternalTicketNumberRecognition1**
The settings define which email should be processed and where to look for the external ticket number.

.. code-block:: 

    DynamicFieldName => ISPTicketNumber
    FromAddressRegExp => suppport@isp.example.com
    IsVisibleForCustomer => 1
    Module => Kernel::System::PostMaster::Filter::ExternalTicketNumberRecognition
    Name => ISP Ticket Numeber
    NumberRegExp => \s*Incident-(\d.*)\s*
    SearchInBody => 1
    SearchInSubject => 1
    SenderType => system
    TicketStateTypes => new;open

- Deploy the system configuration settings and your system is now ready for use.

The values are important:

DynamicFieldName
    The name, not the label, of the dynamic field to store the ticket number.
FromAddressRegExp
    A regular expression to check the sender email adress. A match is needed to have this filter running.
IsVisibleForCustomer
    Indicates with a 1 that the incoming communication should be visible in the customer user front end. A 0 will make the incoming communication not visible to the customer user.
Module
    Please do not change this setting. This is the module that's used.
Name
    The name of the filter which will appear in the communication log.
NumberRegExp
    The regular expression used to determine the ticket number from the body and/or subject.
SearchInBody
    Set this to 1 if the number should be searched in the body of the email.
SearchInSubject
    Set this to 1 if the number should be searched in the subject of the email.
SenderType
    The sender type for email that are recognized by this filter.
TicketStateTypes
    The state types allowed when searching for a ticket to match the ticket number. This setting is optional.

How it works
************

There are two basic options that you can now use to work with external ticket numbers:

1. You can manually add an external ticket number to the dynamic field. Dynamic fields can be made available in any mask within the system. When an email is received, the system looks first to find a matching internal number and then for an external ticket number. This will then match the ticket with the external ticket number, regardless of whether the communication has no internal ticket number.

2. The second way is automatic. When a new ticket is created, and no internal or external number is found, the application generates an internal ticket number. It automatically fills the dynamic field with the external ticket number found in the new communication.
