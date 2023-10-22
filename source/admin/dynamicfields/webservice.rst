Web Service
###########

This dynamic field retrieves information from web services. **Web service (Text)** is used to store a single value, **Web service (Multiselect)**  saves one or more values from the result of the web service.

Requirements
************

You need a web service with two different requester invoker: one handles the request for searching and the other retrieves the data for a specific entry. Using the invoker Generic::Tunnel is sufficient.

Invoker Types
**************

Read more about :ref:`pagenavigation admin_webservices_invoker_index`. If you require ticket data, use ``Ticket::Generic``, if you only need form data in your requests, feel free to use ``Generic::Tunnel``.

Ticket\:\:Generic Example Outgoing Data
=======================================

.. code-block:: json

  {
    "Event": {
        "SearchTerms": "***",
        "UserID": "3",
        "TicketID": "1",
        "Agent": {
            "UserLastLogin": "1697611805",
            "UserEmail": "shawn.beasley@znuny.com",
            "AdminDynamicFieldsOverviewPageShown": "25",
            "UserTicketOverviewMediumPageShown": "20",
            "UserRefreshTime": "0",
            "UserCreateNextMask": "",
            "ChangeTime": "2023-10-18 06:50:05",
            "UserTicketOverviewAgentTicketStatusView": "Small",
            "UserFirstname": "Shawn",
            "UserLastname": "Beasley",
            "UserTicketOverviewSmallPageShown": "25",
            "UserLoginFailed": "0",
            "UserLastViewsLimit": "5",
            "AdminCommunicationLogPageShown": "25",
            "UserLogin": "sbeasley",
            "UserLastViewsPosition": "Avatar",
            "CreateTime": "2023-10-18 06:50:05",
            "UserFullname": "Shawn Beasley",
            "ValidID": 1,
            "UserTitle": null,
            "UserTicketOverviewPreviewPageShown": "15",
            "UserStoredFilterColumns-AgentTicketStatusView": "{}",
            "UserID": 3,
            "UserLastLoginTimestamp": "2023-10-18 06:50:05"
        }
    },
    "Ticket": {
        "TypeData": {
            "ID": 1,
            "Name": "Unclassified",
            "CreateBy": 1,
            "CreateTime": "2023-10-17 18:02:10",
            "ChangeBy": 1,
            "ValidID": 1,
            "ChangeTime": "2023-10-17 18:02:10"
        },
        "TypeID": 1,
        "CustomerUserID": null,
        "DynamicField_ProcessManagementAttachment": null,
        "Priority": "3 normal",
        "UntilTime": 0,
        "Owner": "root@localhost",
        "Changed": "2023-10-17 18:02:10",
        "Queue": "Raw",
        "SLAID": "",
        "StateID": 1,
        "EscalationSolutionTime": 0,
        "CustomerUser": {},
        "TicketID": 1,
        "Age": 46491,
        "ServiceID": "",
        "ChangeBy": 1,
        "CustomerID": null,
        "DynamicField_DFTunnel": null,
        "Type": "Unclassified",
        "DynamicField_TicketCalendarEndTime": null,
        "PriorityData": {
            "ValidID": 1,
            "ChangeBy": 1,
            "ChangeTime": "2023-10-17 18:02:10",
            "ID": 3,
            "Name": "3 normal",
            "CreateBy": 1,
            "CreateTime": "2023-10-17 18:02:10"
        },
        "ResponsibleID": 1,
        "PriorityID": 3,
        "UnlockTimeout": 0,
        "RealTillTimeNotUsed": 0,
        "TicketNumber": "2021012710123456",
        "ArchiveFlag": "n",
        "EscalationTime": 0,
        "EscalationResponseTime": 0,
        "OwnerID": 1,
        "DynamicField_TicketCalendarStartTime": null,
        "LockID": 1,
        "TimeUnit": 0,
        "QueueID": 2,
        "DynamicField_ProcessManagementProcessID": null,
        "State": "new",
        "CreateBy": 1,
        "DynamicField_DFTicket": null,
        "SLAData": {},
        "DynamicField_Test": null,
        "Title": "Znuny says hi!",
        "CreateByData": {
            "UserTicketOverviewMediumPageShown": "20",
            "CreateTime": "2023-10-17 18:02:10",
            "UserLastViewsPosition": "Avatar",
            "UserLogin": "root@localhost",
            "AdminDynamicFieldsOverviewPageShown": "25",
            "UserRefreshTime": "0",
            "UserEmail": "root@localhost",
            "AdminCommunicationLogPageShown": "25",
            "UserLastViewsLimit": "5",
            "UserID": 1,
            "UserCreateNextMask": "",
            "ChangeTime": "2023-10-17 18:02:10",
            "ValidID": 1,
            "UserFullname": "Admin OTRS",
            "UserTitle": null,
            "UserTicketOverviewSmallPageShown": "25",
            "UserTicketOverviewPreviewPageShown": "15",
            "UserFirstname": "Admin",
            "UserLastname": "OTRS"
        },
        "OwnerData": {
            "UserLastViewsLimit": "5",
            "UserID": 1,
            "ValidID": 1,
            "UserFullname": "Admin OTRS",
            "ChangeTime": "2023-10-17 18:02:10",
            "UserCreateNextMask": "",
            "UserFirstname": "Admin",
            "UserLastname": "OTRS",
            "UserTicketOverviewSmallPageShown": "25",
            "UserTitle": null,
            "UserTicketOverviewPreviewPageShown": "15",
            "UserLogin": "root@localhost",
            "AdminDynamicFieldsOverviewPageShown": "25",
            "CreateTime": "2023-10-17 18:02:10",
            "UserTicketOverviewMediumPageShown": "20",
            "UserLastViewsPosition": "Avatar",
            "UserRefreshTime": "0",
            "UserEmail": "root@localhost",
            "AdminCommunicationLogPageShown": "25"
        },
        "GroupID": 1,
        "Article": {
            "MessageID": "<007@localhost>",
            "CreateBy": 1,
            "Subject": "Znuny says hi!",
            "ArticleID": 1,
            "Charset": "",
            "To": "Your Znuny service desk <znuny@localhost>",
            "MimeType": "",
            "SenderType": "customer",
            "ChangeTime": "2023-10-17 18:02:10",
            "InReplyTo": null,
            "Bcc": null,
            "CommunicationChannelID": 1,
            "ToRealname": "Your Znuny service desk",
            "From": "Znuny <hello@znuny.org>",
            "References": null,
            "IncomingTime": 1611745200,
            "ContentCharset": "",
            "ContentType": null,
            "ReplyTo": null,
            "CreateTime": "2023-10-17 18:02:10",
            "ArticleNumber": 1,
            "IsVisibleForCustomer": 1,
            "FromRealname": "Znuny",
            "Body": "We welcome you to Znuny, our ticketing solution based on the well-known OTRS ((Community Edition)) which we forked to make things different.\n\nWe are focused on delivering a stable and community influenced software. So if you have something to contribute, whether bug reports, solutions or enhancements, let us know. We will be happy about your participation.\n\nYou can get additional information here:\n\nCommunity forum: https://community.znuny.org/\n\nDocumentation: https://doc.znuny.org/\n\nGitHub: https://github.com/znuny/Znuny\n\nHave fun and enjoy it.\n\nYour Znuny Team\n",
            "ChangeBy": 1,
            "SenderTypeID": "3",
            "Cc": null,
            "TicketID": 1
        },
        "StateType": "new",
        "ResponsibleData": {
            "AdminDynamicFieldsOverviewPageShown": "25",
            "UserLogin": "root@localhost",
            "CreateTime": "2023-10-17 18:02:10",
            "UserTicketOverviewMediumPageShown": "20",
            "UserLastViewsPosition": "Avatar",
            "UserRefreshTime": "0",
            "AdminCommunicationLogPageShown": "25",
            "UserEmail": "root@localhost",
            "UserID": 1,
            "UserLastViewsLimit": "5",
            "UserFullname": "Admin OTRS",
            "ValidID": 1,
            "ChangeTime": "2023-10-17 18:02:10",
            "UserCreateNextMask": "",
            "UserLastname": "OTRS",
            "UserFirstname": "Admin",
            "UserTitle": null,
            "UserTicketOverviewSmallPageShown": "25",
            "UserTicketOverviewPreviewPageShown": "15"
        },
        "Created": "2023-10-17 18:02:10",
        "ServiceData": {},
        "Responsible": "root@localhost",
        "QueueData": {
            "SystemAddressID": 1,
            "Comment": "All default incoming tickets.",
            "SignatureID": 1,
            "UpdateNotify": null,
            "CreateTime": "2023-10-17 18:02:10",
            "UnlockTimeout": 0,
            "FollowUpLock": 0,
            "DefaultSignKey": null,
            "ValidID": 1,
            "SolutionNotify": null,
            "UpdateTime": null,
            "SalutationID": 1,
            "GroupID": 1,
            "Email": "vz117@demo2.znuny.com",
            "FirstResponseNotify": null,
            "FirstResponseTime": null,
            "QueueID": 2,
            "SolutionTime": null,
            "Name": "Raw",
            "ChangeTime": "2023-10-17 18:02:10",
            "RealName": "Znuny System",
            "FollowUpID": 1,
            "Calendar": ""
        },
        "Lock": "unlock",
        "DynamicField_ProcessManagementActivityID": null,
        "CustomerCompany": {},
        "Articles": [
            {
            "ReplyTo": null,
            "ContentType": null,
            "Body": "We welcome you to Znuny, our ticketing solution based on the well-known OTRS ((Community Edition)) which we forked to make things different.\n\nWe are focused on delivering a stable and community influenced software. So if you have something to contribute, whether bug reports, solutions or enhancements, let us know. We will be happy about your participation.\n\nYou can get additional information here:\n\nCommunity forum: https://community.znuny.org/\n\nDocumentation: https://doc.znuny.org/\n\nGitHub: https://github.com/znuny/Znuny\n\nHave fun and enjoy it.\n\nYour Znuny Team\n",
            "FromRealname": "Znuny",
            "IsVisibleForCustomer": 1,
            "CreateTime": "2023-10-17 18:02:10",
            "ArticleNumber": 1,
            "TicketID": 1,
            "Cc": null,
            "SenderTypeID": "3",
            "ChangeBy": 1,
            "MessageID": "<007@localhost>",
            "To": "Your Znuny service desk <znuny@localhost>",
            "Charset": "",
            "ArticleID": 1,
            "Subject": "Znuny says hi!",
            "CreateBy": 1,
            "Bcc": null,
            "InReplyTo": null,
            "ChangeTime": "2023-10-17 18:02:10",
            "SenderType": "customer",
            "MimeType": "",
            "ContentCharset": "",
            "IncomingTime": 1611745200,
            "From": "Znuny <hello@znuny.org>",
            "References": null,
            "ToRealname": "Your Znuny service desk",
            "CommunicationChannelID": 1
            }
        ],
        "EscalationUpdateTime": 0
    }
    }

Generic\:\:Tunnel Example Outgoing Data
=======================================

.. code-block:: json

    {
      "Ticket": {},
      "Event": {
      "UserID": "3",
      "SearchTerms": "***",
      "Agent": {
          "UserTicketOverviewAgentTicketStatusView": "Small",
          "UserTicketOverviewMediumPageShown": "20",
          "UserTicketOverviewPreviewPageShown": "15",
          "UserLastLogin": "1697611805",
          "UserTicketOverviewSmallPageShown": "25",
          "UserID": 3,
          "UserLogin": "sbeasley",
          "UserLastLoginTimestamp": "2023-10-18 06:50:05",
          "UserEmail": "shawn.beasley@znuny.com",
          "UserFirstname": "Shawn",
          "UserCreateNextMask": "",
          "UserStoredFilterColumns-AgentTicketStatusView": "{}",
          "UserRefreshTime": "0",
          "UserFullname": "Shawn Beasley",
          "UserLastViewsLimit": "5",
          "UserLastViewsPosition": "Avatar",
          "UserTitle": null,
          "AdminDynamicFieldsOverviewPageShown": "25",
          "CreateTime": "2023-10-18 06:50:05",
          "ChangeTime": "2023-10-18 06:50:05",
          "UserLastname": "Beasley",
          "ValidID": 1,
          "AdminCommunicationLogPageShown": "25",
          "UserLoginFailed": "0"
      }
    }

Specific Event Data
*******************

`SearchTerms` contains the search entered by the user when the search invoker is called. When the get invoker is called it's the stored identifier of the record which should be retrieved.

Use the outbound mapping to transform this data as needed.

Return Value Mapping
********************

If your service provider 

**ResponseValues**: Returns an information about the response and an array with objects.

.. code-block:: json

    {
    "response": {
      "returncode": "200",
      "returnmessage": "Success"
    },
    "values": [
      {
      "ID": "1",
      "Name": "John",
      "City": "Berlin"
      },
      {
      "ID": "2",
      "Name": "Jane",
      "City": "Coronado"
      }
    ]
    }

**DirectRequest**: Return a simple key/value structure.

.. code-block:: json

    [
      {
          "Key": "1",
          "Value": "John"
      },
      {
          "Key": "2",
          "Value": "Jane"
      },
    ]


Configuration
*************

Select the web service, both invoker and the backend to the values which matches your preparations described in the previous block.

.. figure:: images/DynamicFieldWebservice-Multiselect-Configuration.png
    :alt: DynamicFieldWebservice Multiselect Configuration

    Dynamic Field Configuration

- **Key for search** : the keys to search in, only used in the frontend, this has not affect on the web service.
- **Key for stored value**: the key which is stored to retrieve entries later with the get invoker. Usually, some ID.

.. note:: If the get invoker cannot retrieve data, this value is displayed. You might use the function Additional dynamic field storage to have a persistent display value available.

- **Key to display**: Which key(s) should be displayed.

- **Template Type**: Only for Multiselect available. This setting defines how multiple values are separated. Available are **Default** comma separated, **Separator** one or more characters can be defined as a separator, **Word Wrap** creates line breaks and **List** displays a list.

- **Separator to display between multi-key values**: Belongs to **Template Type**, this setting applies when **Separator** is used.

- **Limit**: Limit for the displayed entries when the search result is displayed.

- **Autocomplete min. input length**: The search is only started when the characters entered by the user has this length reached.

- **Query delay**: Number of milliseconds after the input is entered until the search is started. This setting is evaluated every time the search input changes.

- **Additional dynamic field storage**: Enables you to populate data into other fields, useful when the backend setting is **ResponseValues**. You select a dynamic field, the key from the search result object and how the value should be stored: `Backend` save the value of the key in the selected dynamic field, `Frontend` writes the value into the field if it's available in the current screen without saving, `Frontend and Backend` does both. For the Multiselect field, the results are stored comma-separated in the field.

- **Default Value**: Always set when the field is shown. It does not initiate a search and therefore no results list.

- **Default search term**: Specifies a default search term which is used when the user clicks into the search field.
 
- **Initial default search term**: Search term which is used to start a search without any user interaction when the screen is shown.

- **Attributes**: Add attributes from the form.

.. figure:: images/DynamicFieldWebservice-Additional_dynamicField.png
    :alt: DynamicFieldWebservice Additional dynamic field

    Additional Attributes


.. important::
    
    The fields must be visible. The form data will be used as a part of the event making it easier to cascade form elements.
