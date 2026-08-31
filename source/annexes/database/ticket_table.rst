.. meta::
   :description: Complete column reference for the Znuny ticket table — for reporting, BI, and SQL queries.
   :keywords: znuny ticket table, znuny ticket schema, znuny ticket columns

.. _PageNavigation annexes_database_ticket_table:

The Ticket Table
################

The ``ticket`` table is the starting point for almost every report. This page explains every column with a focus on what it means for queries and aggregations.

Column Reference
****************

Identity
========

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``id``
     - BIGINT
     - Internal numeric primary key. Use this for joins (e.g. to ``article``, ``ticket_history``, ``dynamic_field_value``).
   * - ``tn``
     - VARCHAR(50)
     - The human-readable ticket number shown in the UI (e.g. ``2024011234567890``). This is what users refer to. Unique.
   * - ``title``
     - VARCHAR(255)
     - The ticket subject/title.

Classification
==============

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``queue_id``
     - INTEGER
     - The queue currently owning this ticket. Joins to ``queue.id``.
   * - ``ticket_lock_id``
     - SMALLINT
     - Whether the ticket is locked. ``1`` = unlocked, ``2`` = locked. Joins to ``ticket_lock_type.id``.
   * - ``type_id``
     - SMALLINT
     - Ticket type (e.g. Incident, Request). NULL if types are not enabled. Joins to ``ticket_type.id``.
   * - ``service_id``
     - INTEGER
     - Associated service. NULL if not set. Joins to ``service.id``.
   * - ``sla_id``
     - INTEGER
     - Associated SLA. NULL if not set. Joins to ``sla.id``.
   * - ``ticket_priority_id``
     - SMALLINT
     - Priority. Joins to ``ticket_priority.id``.
   * - ``ticket_state_id``
     - SMALLINT
     - Current state (open, closed, pending…). Joins to ``ticket_state.id``.

People
======

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``user_id``
     - INTEGER
     - The agent currently assigned as owner. Joins to ``users.id``.
   * - ``responsible_user_id``
     - INTEGER
     - The agent responsible for the ticket (may differ from owner). Joins to ``users.id``. Defaults to ``user_id`` when no separate responsible agent is set.
   * - ``customer_id``
     - VARCHAR(150)
     - The customer organization. Joins to ``customer_company.customer_id`` (a string key, not an integer).
   * - ``customer_user_id``
     - VARCHAR(250)
     - The customer contact's login name. Joins to ``customer_user.login`` (also a string, not an integer).

Timing
======

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``timeout``
     - INTEGER
     - Unix epoch of when the lock will automatically release. ``0`` when not locked.
   * - ``until_time``
     - INTEGER
     - Unix epoch of the pending-until time for pending states. ``0`` when not pending. Convert with ``FROM_UNIXTIME(until_time)``.
   * - ``escalation_time``
     - INTEGER
     - Unix epoch of the nearest upcoming escalation (whichever of the three escalation clocks fires first). ``0`` means no active escalation.
   * - ``escalation_response_time``
     - INTEGER
     - Unix epoch of the first-response escalation deadline. ``0`` means the clock is not running.
   * - ``escalation_update_time``
     - INTEGER
     - Unix epoch of the update escalation deadline. ``0`` means the clock is not running.
   * - ``escalation_solution_time``
     - INTEGER
     - Unix epoch of the solution escalation deadline. ``0`` means the clock is not running.

.. tip::

    All four escalation columns store Unix epoch seconds. Use ``FROM_UNIXTIME()`` to convert to a readable datetime, or compare directly to ``UNIX_TIMESTAMP(NOW())`` to find currently-escalated tickets:

    .. code-block:: sql

        SELECT tn, title, FROM_UNIXTIME(escalation_time) AS escalates_at
        FROM   ticket
        WHERE  escalation_time > 0
        AND    escalation_time < UNIX_TIMESTAMP(NOW())
        AND    archive_flag    = 0;

Archive and Audit
=================

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``archive_flag``
     - SMALLINT
     - ``0`` = active ticket, ``1`` = archived. Always filter ``WHERE archive_flag = 0`` unless you specifically need archived tickets. Archived tickets are excluded from most standard views.
   * - ``create_time``
     - DATETIME
     - When the ticket was created.
   * - ``create_by``
     - INTEGER
     - Agent who created the ticket. Joins to ``users.id``.
   * - ``change_time``
     - DATETIME
     - When the ticket was last modified.
   * - ``change_by``
     - INTEGER
     - Agent who last modified the ticket. Joins to ``users.id``.

Common Filters
**************

.. code-block:: sql

    -- Active tickets only (exclude archive)
    WHERE archive_flag = 0

    -- Tickets created in the last 30 days
    WHERE create_time >= DATE_SUB(NOW(), INTERVAL 30 DAY)

    -- Currently escalated tickets
    WHERE escalation_time > 0
      AND escalation_time < UNIX_TIMESTAMP(NOW())

    -- Pending tickets with a future reminder
    WHERE until_time > 0
      AND until_time > UNIX_TIMESTAMP(NOW())
