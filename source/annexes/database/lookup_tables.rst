.. meta::
   :description: Znuny lookup table join cheat-sheet — resolve ticket state, priority, type, queue, agent, and validity IDs to names.
   :keywords: znuny lookup tables, znuny join cheat-sheet, znuny ticket state table, znuny priority table

.. _PageNavigation annexes_database_lookup_tables:

Lookup Tables
#############

Every ID column in the ``ticket`` table resolves to a name in a small lookup table. This page is a quick-reference join cheat-sheet.

State
*****

``ticket_state`` — resolves ``ticket.ticket_state_id``

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - SMALLINT
     - Primary key. Referenced by ``ticket.ticket_state_id``.
   * - ``name``
     - VARCHAR(200)
     - State name shown in the UI (e.g. ``open``, ``closed successful``).
   * - ``type_id``
     - SMALLINT
     - The state's behavioral category. Joins to ``ticket_state_type.id``.
   * - ``color``
     - VARCHAR(25)
     - Hex color used for this state in the UI.
   * - ``valid_id``
     - SMALLINT
     - ``1`` = valid/active. Joins to ``valid.id``.

``ticket_state_type`` — resolves ``ticket_state.type_id``

The state type controls system behavior regardless of the state's display name:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Type name
     - Behavior
   * - ``new``
     - Ticket has not yet been worked on.
   * - ``open``
     - Ticket is being actively worked on.
   * - ``closed``
     - Ticket is resolved and no longer active.
   * - ``pending reminder``
     - Ticket is waiting; a reminder fires at the pending time.
   * - ``pending auto``
     - Ticket transitions to another state automatically at the pending time.
   * - ``removed``
     - Ticket is archived and hidden from normal views.
   * - ``merged``
     - Ticket has been merged into another ticket.

Join pattern:

.. code-block:: sql

    JOIN ticket_state     ts  ON ts.id  = t.ticket_state_id
    JOIN ticket_state_type tst ON tst.id = ts.type_id

Priority
********

``ticket_priority`` — resolves ``ticket.ticket_priority_id``

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - SMALLINT
     - Primary key. Referenced by ``ticket.ticket_priority_id``.
   * - ``name``
     - VARCHAR(200)
     - Priority name (e.g. ``3 normal``, ``5 very high``).
   * - ``color``
     - VARCHAR(25)
     - Hex color used for this priority in the UI.
   * - ``valid_id``
     - SMALLINT
     - ``1`` = valid/active. Joins to ``valid.id``.

Type
****

``ticket_type`` — resolves ``ticket.type_id``

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - SMALLINT
     - Primary key. Referenced by ``ticket.type_id``.
   * - ``name``
     - VARCHAR(200)
     - Type name (e.g. ``Incident``, ``Service Request``).
   * - ``valid_id``
     - SMALLINT
     - ``1`` = valid/active. Joins to ``valid.id``.

Queue
*****

``queue`` — resolves ``ticket.queue_id``

Key columns for reporting:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - INTEGER
     - Primary key. Referenced by ``ticket.queue_id``.
   * - ``name``
     - VARCHAR(200)
     - Full queue name, including parent path separated by ``::`` (e.g. ``Support::Level 2``).
   * - ``group_id``
     - INTEGER
     - The permission group that controls access to this queue. Joins to ``permission_groups.id``.
   * - ``first_response_time``
     - INTEGER
     - Default first-response SLA time in minutes (NULL = none).
   * - ``update_time``
     - INTEGER
     - Default update SLA time in minutes (NULL = none).
   * - ``solution_time``
     - INTEGER
     - Default solution SLA time in minutes (NULL = none).
   * - ``valid_id``
     - SMALLINT
     - ``1`` = valid/active. Joins to ``valid.id``.

Agents
******

``users`` — resolves ``ticket.user_id`` and ``ticket.responsible_user_id``

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - INTEGER
     - Primary key. Referenced by ``ticket.user_id``, ``ticket.responsible_user_id``, and ``*.create_by``/``*.change_by`` on most tables.
   * - ``login``
     - VARCHAR(200)
     - Agent username. Unique.
   * - ``first_name``
     - VARCHAR(100)
     - First name.
   * - ``last_name``
     - VARCHAR(100)
     - Last name.
   * - ``valid_id``
     - SMALLINT
     - ``1`` = valid/active. Joins to ``valid.id``.

Join pattern for owner name:

.. code-block:: sql

    JOIN users u ON u.id = t.user_id
    -- then use: CONCAT(u.first_name, ' ', u.last_name)

Validity
********

``valid`` — the validity flag table referenced by most configuration tables

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - SMALLINT
     - Primary key (``1`` = valid, ``2`` = invalid, ``3`` = temporarily invalid).
   * - ``name``
     - VARCHAR(200)
     - Human-readable name: ``valid``, ``invalid``, ``invalid-temporarily``.

For reporting you almost always want to filter on ``valid_id = 1`` when joining lookup tables to exclude deactivated states, queues, priorities, or agents.

Master Join Template
********************

A template that resolves the most common ID columns in one query:

.. code-block:: sql

    SELECT
        t.tn,
        t.title,
        ts.name                              AS state,
        tst.name                             AS state_type,
        tp.name                              AS priority,
        tt.name                              AS ticket_type,
        q.name                               AS queue,
        CONCAT(u.first_name, ' ', u.last_name)  AS owner,
        t.create_time,
        t.change_time
    FROM   ticket t
    JOIN   ticket_state      ts  ON ts.id  = t.ticket_state_id
    JOIN   ticket_state_type tst ON tst.id = ts.type_id
    JOIN   ticket_priority   tp  ON tp.id  = t.ticket_priority_id
    LEFT JOIN ticket_type    tt  ON tt.id  = t.type_id
    JOIN   queue             q   ON  q.id  = t.queue_id
    JOIN   users             u   ON  u.id  = t.user_id
    WHERE  t.archive_flag = 0;
