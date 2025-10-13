.. _Example Web Service GenericTicketConnectorREST:

GenericTicketConnectorREST
##########################

This document provides examples of how to use the Ready2Adopt GenericTicketConnectorREST web service in Znuny. The GenericTicketConnectorREST provides RESTful API endpoints to interact with tickets and sessions.

**Default Operations**:

:ref:`create_session_operation`
    Create a Session
:ref:`delete_session_operation`
    Delete a Session
:ref:`get_session_operation`
    Retrieve Session Data
:ref:`ticket_create_operation`
    Create a Ticket
:ref:`ticket_get_operation`
    Retrieve Ticket Data
:ref:`ticket_history_get_operation`
    Retrieve Ticket History
:ref:`tickets_search_operation`
    Search for Tickets
:ref:`ticket_update_operation`
    Update a Ticket

.. note:: 
    
    All examples assume that the web service is hosted at `http://localhost/znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/`.

    You may need to adjust the URL based on your Znuny installation and configuration.


.. seealso:: 

    API Documentation:

    - `Session Operations <https://doc.znuny.org/znuny-dev-api/API/Kernel/GenericInterface/Operation/Session/index.html>`_
    - `Ticket Operations <https://doc.znuny.org/znuny-dev-api/API/Kernel/GenericInterface/Operation/Ticket/index.html>`_

.. important::
    
    To keep the documentation short, and readable: Response and Request Examples may not contain all data fields. Please refer to the API documentation for a complete list of fields and their descriptions.

.. _create_session_operation:

SessionCreate
*************

Create a *Session* for use with other operations.

**Example Request**:

.. code-block:: http

    POST /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Session HTTP/1.1
    Host: localhost
    Content-Type: application/json
    Accept: application/json

    {
        "UserLogin": "admin",
        "Password": "admin_password"
    }

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "SessionID": "your_session_id"
    }

.. _delete_session_operation:

SessionDelete
*************

Delete a Session

**Example Request**:

.. code-block:: http

    DELETE /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Session/<your_session_id> HTTP/1.1
    Host: localhost
    Content-Type: application/json
    Accept: application/json


**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "Success": 1
    }

.. _get_session_operation:

SessionGet
***********

Retrieve Session Data

**Example Request**:

.. code-block:: http

    GET /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Session/SessionID=<your_session_id> HTTP/1.1
    Host: localhost
    Accept: application/json

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "SessionData": [
            {
                "Key": "AdminCommunicationLogPageShown",
                "Value": "25"
            },
            {
                "Key": "AdminDynamicFieldsOverviewPageShown",
                "Value": "25"
            }
            // More session data fields
        ]
    }


.. _ticket_create_operation:

TicketCreate
************

Create a Ticket

**Example Request**:

.. code-block:: http

    POST /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket HTTP/1.1
    Host: localhost
    Content-Type: application/json
    Accept: application/json
    
    {
        "UserLogin": "admin",
        "Password": "admin_password",
        "Ticket": 
            {
                "Queue": "Postmaster",
                "StateID": "1",
                "OwnerID": "1",
                "TypeID": "1",
                "PriorityID": "3",
                "Title": "Test",
                "CustomerUser": "user@example.com",
                "Lock": "unlock"
            },
        "Article": {
            "CommunicationChannel": "Internal",
            "SenderType": "agent",
            "Subject": "Initial Request",
            "Body": "Test Body",
            "From": "user@example.com",
            "To": "user@znuny.exapmle.com",
            "VisibleForCustomer": "0",
            "ContentType": "text/plain; charset=utf8"
        },
    }

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "TicketID": "1",
        "TicketNumber": "2025000001",
        "ArticleID": "1"
    }

.. _ticket_get_operation:

TicketGet
*********

Retrieve Ticket Data

**Example Request**:

.. code-block:: http

    GET /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket/<ticket_id>?SessionID=<your_session_id> HTTP/1.1
    Host: localhost
    Accept: application/json

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "Ticket": [
        {
          "Age": 1052507,
          "ArchiveFlag": "n",
          "ChangeBy": 1,
          "Changed": "2025-09-16 14:08:17",
          "CreateBy": 1,
          "Created": "2025-09-11 05:52:20",
          "CustomerID": "",
      ]
    }

.. _ticket_history_get_operation:

TicketHistoryGet
****************

Retrieve Ticket History

**Example Request**:

.. code-block:: http

    GET /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket/History/<ticket_id>?SessionID=<your_session_id> HTTP/1.1
    Host: localhost
    Accept: application/json

**Example Response**:

.. code-block:: http
    
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
        "History": [
            {
                "HistoryType": "ArticleCreate",
                "CreateBy": 1,
                "Created": "2025-09-11 05:52:20",
                "Content": "Article (ID=456) created.",
                "UserID": 1,
                "UserLogin": "admin"
            },
            {
                "HistoryType": "StateUpdate",
                "CreateBy": 1,
                "Created": "2025-09-11 06:00:00",
                "Content": "State changed from 'new' to 'open'.",
                "UserID": 1,
                "UserLogin": "admin"
            }
        ]
    }
    

.. _tickets_search_operation:

TicketSearch
*************

Search for Tickets

**Example Request**:

.. code-block:: http

    POST /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket/Search  HTTP/1.1
    Host: localhost
    Accept: application/json

    {
        "SessionID": "<your_session_id>",
        "QueueIDs": [1, 2, 3],
    }

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "TicketIDs": [
            1,
            2,
            3,
            4,
            5
        ]
    }


.. _ticket_update_operation:

TicketUpdate
************

Update a Ticket

**Example Request**:

.. code-block:: http

    PATH /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket/<ticket_id> HTTP/1.1
    Host: localhost
    Content-Type: application/json
    Accept: application/json

    {
        "SessionID": "<your_session_id>",

        "Ticket": 
            {
                "StateID": "2",
                "PriorityID": "2",
                "OwnerID": "2",
                "Title": "Updated Test Title"
            }
    }

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "Success": 1
    }