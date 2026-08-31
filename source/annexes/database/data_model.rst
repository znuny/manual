.. meta::
   :description: Znuny data model overview — the four core entities and their relationships for reporting and BI.
   :keywords: znuny data model, znuny entity relationship, znuny schema overview

.. _PageNavigation annexes_database_data_model:

Data Model Overview
###################

The Znuny data model is built around four core entities. Understanding their relationships is the foundation for every useful query.

The Four Pillars
****************

**Ticket**
    The central entity. Every support request, task, or case is a ticket. All other entities either belong to a ticket or are referenced by one.

**Article**
    A communication record attached to a ticket — an email in or out, a phone call note, an internal note, a chat message. One ticket has zero or more articles.

**Queue**
    The organizational unit that owns tickets. Queues control routing, escalation times, signatures, and email addresses. Every ticket belongs to exactly one queue at any given time.

**User / Customer**
    Two separate identity hierarchies. *Agents* (``users`` table) are the staff who work tickets. *Customers* are the people and organizations who raise them — stored in ``customer_user`` (contacts) and ``customer_company`` (organizations).

Entity Diagram
**************

.. code-block:: text

                    ┌─────────────────────┐
                    │       queue         │
                    │  id, name, group_id │
                    └──────────┬──────────┘
                               │ queue_id
                               ▼
    ┌──────────┐   ┌───────────────────────────────┐   ┌──────────────────┐
    │  users   │◄──│            ticket             │──►│  customer_user   │
    │ (agents) │   │  id, tn, title, queue_id,     │   │ (contacts)       │
    └──────────┘   │  user_id, ticket_state_id,    │   └──────────────────┘
         ▲         │  ticket_priority_id, type_id, │          │
         │         │  customer_id, customer_user_id│   customer_id
         owner_id  └───────────┬───────────────────┘          ▼
                               │                    ┌──────────────────┐
              ┌────────────────┼────────────────┐   │ customer_company │
              │                │                │   │ (organizations)  │
              ▼                ▼                ▼   └──────────────────┘
    ┌──────────────┐  ┌──────────────┐  ┌─────────────────────┐
    │ticket_history│  │   article    │  │  dynamic_field      │
    │(audit trail) │  │  id,         │  │  _value (EAV)       │
    └──────────────┘  │  ticket_id,  │  └─────────────────────┘
                      │  channel...  │
                      └──────┬───────┘
                             │ article_id
                             ▼
                    ┌─────────────────────┐
                    │  article_data_mime  │
                    │  (subject, body,    │
                    │   from, to, cc...)  │
                    └─────────────────────┘

Key Relationships
*****************

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - From
     - To
     - Join condition
   * - ``ticket``
     - ``queue``
     - ``ticket.queue_id = queue.id``
   * - ``ticket``
     - ``users`` (owner)
     - ``ticket.user_id = users.id``
   * - ``ticket``
     - ``users`` (responsible)
     - ``ticket.responsible_user_id = users.id``
   * - ``ticket``
     - ``customer_user``
     - ``ticket.customer_user_id = customer_user.login``
   * - ``ticket``
     - ``customer_company``
     - ``ticket.customer_id = customer_company.customer_id``
   * - ``article``
     - ``ticket``
     - ``article.ticket_id = ticket.id``
   * - ``article_data_mime``
     - ``article``
     - ``article_data_mime.article_id = article.id``
   * - ``ticket_history``
     - ``ticket``
     - ``ticket_history.ticket_id = ticket.id``
   * - ``dynamic_field_value``
     - ``ticket``
     - ``dynamic_field_value.object_id = ticket.id`` (when ``object_type = 'Ticket'``)

.. note::

    ``ticket.customer_user_id`` is a **string** (the login name), not an integer foreign key. Join it to ``customer_user.login``, not ``customer_user.id``. Similarly, ``ticket.customer_id`` joins to ``customer_company.customer_id``, which is also a string primary key.

Starting Point for Any Report
******************************

Almost every useful report begins with the ``ticket`` table and joins outward:

.. code-block:: sql

    SELECT
        t.tn                          AS ticket_number,
        t.title,
        ts.name                       AS state,
        tp.name                       AS priority,
        q.name                        AS queue,
        CONCAT(u.first_name, ' ', u.last_name) AS owner,
        t.create_time,
        t.change_time
    FROM ticket t
    JOIN ticket_state    ts ON ts.id = t.ticket_state_id
    JOIN ticket_priority tp ON tp.id = t.ticket_priority_id
    JOIN queue            q ON  q.id = t.queue_id
    JOIN users            u ON  u.id = t.user_id
    WHERE t.archive_flag = 0
    ORDER BY t.create_time DESC
    LIMIT 50;
