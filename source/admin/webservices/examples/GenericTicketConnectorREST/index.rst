.. meta::
   :description: Install and use the Znuny GenericTicketConnectorREST web service - manage sessions and tickets via REST, including calling it as a customer user.
   :keywords: generictticketconnectorrest, znuny rest api, ticket create api, ticket search api, session api, ticket update api, ticket history api, customer rest api

.. _Example Web Service GenericTicketConnectorREST:

GenericTicketConnectorREST
##########################

This document explains how to install the Ready2Adopt GenericTicketConnectorREST web service and how to use it, including calling it as a customer user rather than an agent. The GenericTicketConnectorREST provides RESTful API endpoints to interact with tickets and sessions.

Installing The Web Service
***************************

The web service definition ships with every Znuny installation, ready to import, at:

``var/webservices/examples/GenericTicketConnectorREST.yml``

To import it through the admin interface, follow :ref:`Web Service Quick Start (Ready2Adopt)` and pick **GenericTicketConnectorREST** from the template list. No further transport configuration is required afterwards; the file already wires every operation below to a REST route.

To import it from the command line instead, which is easier to repeat across environments:

.. code-block:: console

    bin/znuny.Console.pl Admin::WebService::Add \
      --name GenericTicketConnectorREST \
      --source-path var/webservices/examples/GenericTicketConnectorREST.yml

Run ``bin/znuny.Console.pl Admin::WebService::Add --help`` for all options, and see :ref:`PageNavigation console_index` for general console usage.

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

Calling It As A Customer User
******************************

Every operation below accepts one of two ways to authenticate: pass ``UserLogin``/``CustomerUserLogin`` and ``Password`` on each call, or create a session once with :ref:`create_session_operation` and reuse the returned ``SessionID``. This works the same way for a customer as it does for an agent - the difference is only which login field you send, and it is the same account the customer already uses to sign in to the customer portal, nothing separate to provision.

Once authenticated as a customer, three things follow automatically, without any extra parameters:

- :ref:`tickets_search_operation` only ever returns tickets that customer owns, even with no filters at all.
- :ref:`ticket_get_operation` returns ``TicketGet.AccessDenied`` if the ticket belongs to a different customer.
- :ref:`ticket_create_operation` and :ref:`ticket_update_operation` also accept a customer session; the ticket is written under the system's configured ``CustomerPanelUserID``, while permission checks still apply against the calling customer.

Not every operation is available to a customer. :ref:`ticket_history_get_operation` rejects a customer session outright with ``TicketHistoryGet: User needs to an Agent!`` - use an agent login for that one.

.. caution::

    :ref:`get_session_operation` returns the full session record for whichever account is logged in. For a customer session this includes the hashed password (``UserPassword``) and the complete customer/company field mapping; for an agent session the password hash is filtered out. Treat access to that operation the same way you would treat access to the login credentials themselves, and do not expose it to end users beyond what an integration genuinely needs.

.. _create_session_operation:

SessionCreate
*************

Create a *Session* for use with other operations. Provide either ``UserLogin`` (agent) or ``CustomerUserLogin`` (customer) together with ``Password``.

**Example Request (customer)**:

.. code-block:: http

    POST /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Session HTTP/1.1
    Host: localhost
    Content-Type: application/json
    Accept: application/json

    {
        "CustomerUserLogin": "customer_login",
        "Password": "customer_password"
    }

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "SessionID": "your_session_id"
    }

An agent session is created the same way, with ``UserLogin`` in place of ``CustomerUserLogin``.

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

Retrieve Session Data. See the caution note above before exposing this operation to anything but a trusted backend.

**Example Request**:

.. code-block:: http

    GET /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Session/<your_session_id> HTTP/1.1
    Host: localhost
    Accept: application/json

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "SessionData": [
            {
                "Key": "UserLogin",
                "Value": "customer_login"
            },
            {
                "Key": "UserType",
                "Value": "Customer"
            }
            // Full session record: name/address fields, UserPassword (hashed),
            // company config, timestamps, and everything else Znuny attaches
            // to that session
        ]
    }


.. _ticket_create_operation:

TicketCreate
************

Create a Ticket. A customer session may call this too; the ticket is then created under the system's configured ``CustomerPanelUserID`` rather than the customer's own agent-side user.

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
        }
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
          "TicketID": 1,
          "TicketNumber": "2025000001",
          "Title": "Test",
          "State": "new",
          "StateType": "new",
          "Queue": "Postmaster",
          "Priority": "3 normal",
          "Owner": "admin",
          "CustomerID": "",
          "CustomerUserID": "user@example.com",
          "Created": "2025-09-11 05:52:20",
          "Changed": "2025-09-16 14:08:17",
          "Age": 1052507
          // ...remaining ticket fields
        }
      ]
    }

Requesting a ticket that does not belong to the calling customer, when authenticated as a customer, returns an error instead of ticket data:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "Error": {
            "ErrorCode": "TicketGet.AccessDenied",
            "ErrorMessage": "TicketGet: User does not have access to the ticket!"
        }
    }

.. _ticket_history_get_operation:

TicketHistoryGet
****************

Retrieve Ticket History. Agent login required - a customer session is rejected with ``TicketHistoryGet: User needs to an Agent!``, regardless of whether the customer owns the ticket.

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

Search for Tickets. Called with a customer session, results are always limited to that customer's own tickets, whether or not any filters are given.

**Example Request**:

.. code-block:: http

    POST /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket/Search  HTTP/1.1
    Host: localhost
    Accept: application/json

    {
        "SessionID": "<your_session_id>"
    }

**Example Response**:

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "TicketID": [
            "1",
            "4",
            "7"
        ]
    }

Add any of the usual search fields (``States``, ``Queues``, ``Priorities``, ``TicketCreateTimeNewerDate``, ``DynamicField_*``, and so on) to narrow the result. They combine with the automatic customer scope; they never widen past it.

.. _ticket_update_operation:

TicketUpdate
************

Update a Ticket. A customer session may call this too, subject to the same ownership check as :ref:`ticket_get_operation`.

**Example Request**:

.. code-block:: http

    PATCH /znuny/nph-genericinterface.pl/Webservice/GenericTicketConnectorREST/Ticket/<ticket_id> HTTP/1.1
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
        "TicketID": "1",
        "TicketNumber": "2025000001"
    }

Common Errors
*************

Every operation returns its own ``<Operation>.AuthFail`` and, where an ownership check applies, ``<Operation>.AccessDenied`` - the prefix always names the call that failed, which is useful when logging integration errors.

.. list-table::
    :header-rows: 1

    * - Situation
      - ErrorCode
      - ErrorMessage
    * - Wrong login or password
      - ``SessionCreate.AuthFail``
      - Authorization failing!
    * - Expired or invalid SessionID
      - ``<Operation>.AuthFail`` (``SessionGet.SessionInvalid`` for SessionGet)
      - Authorization failing!
    * - Ticket belongs to a different customer
      - ``TicketGet.AccessDenied`` / ``TicketUpdate.AccessDenied``
      - User does not have access to the ticket!
    * - Customer session calling an agent-only operation
      - ``TicketHistoryGet.AuthFail``
      - User needs to an Agent!

.. note::

    A ``SessionID`` follows the normal Znuny session timeout (``SessionMaxTime`` / ``SessionMaxIdleTime``), the same clock a browser login runs on. An integration that runs longer than that should call :ref:`create_session_operation` again rather than assume a ``SessionID`` is permanent.

    Always call this web service over HTTPS in production - credentials and ``SessionID`` travel in plain request bodies and query strings.
