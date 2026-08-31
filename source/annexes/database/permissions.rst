.. meta::
   :description: Znuny roles, groups, and permissions database schema — how to query agent and customer access rights from the database.
   :keywords: znuny permissions database, znuny roles groups, znuny group_user, znuny group_role, znuny permission query

.. _PageNavigation annexes_database_permissions:

Roles, Groups, and Permissions
################################

Znuny's access control system is built on three layers: **groups** define what can be accessed, **roles** bundle group permissions together, and **users** (agents) are granted access either directly to groups or via roles. Customers have their own parallel path through ``group_customer`` and ``group_customer_user``.

Understanding this model lets you answer questions like "which agents can work tickets in queue X?", "what groups does this user have?", or "which roles grant access to this group?"

The Permission Model
********************

.. code-block:: text

    Agent permissions — two paths to a group:

    users ──► group_user ──────────────────────────────► permission_groups
    users ──► role_user ──► roles ──► group_role ──────► permission_groups

    Customer permissions:

    customer_company  ──► group_customer      ──────────► permission_groups
    customer_user     ──► group_customer_user ──────────► permission_groups

Permission Keys
***************

Every row in the assignment tables carries a ``permission_key`` that specifies the level of access being granted.

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Key
     - What it allows
   * - ``ro``
     - Read-only access — view tickets and articles in the group's queues.
   * - ``move_into``
     - Move tickets into queues that belong to the group.
   * - ``create``
     - Create new tickets in the group's queues.
   * - ``note``
     - Add notes to tickets in the group's queues.
   * - ``owner``
     - Become the owner of tickets in the group's queues.
   * - ``priority``
     - Change the priority of tickets in the group's queues.
   * - ``rw``
     - Full read-write access. When ``rw`` is granted, all other keys are implied. The system stores only ``rw`` and removes the individual keys.

For ``group_role`` the presence of a permission is controlled by ``permission_value``: ``1`` = enabled, ``0`` = disabled (explicitly withdrawn).

The Tables
**********

``permission_groups`` — group definitions
==========================================

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - INTEGER
     - Primary key. Referenced by all assignment tables as ``group_id``.
   * - ``name``
     - VARCHAR(200)
     - Group name (e.g. ``users``, ``stats``, ``admin``). Unique.
   * - ``comments``
     - VARCHAR(250)
     - Optional description.
   * - ``valid_id``
     - SMALLINT
     - ``1`` = active. Joins to ``valid.id``.

``roles`` — role definitions
==============================

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``id``
     - INTEGER
     - Primary key. Referenced by ``role_user.role_id`` and ``group_role.role_id``.
   * - ``name``
     - VARCHAR(200)
     - Role name. Unique.
   * - ``comments``
     - VARCHAR(250)
     - Optional description.
   * - ``valid_id``
     - SMALLINT
     - ``1`` = active.

``group_user`` — direct agent → group assignment
=================================================

Agents assigned directly to a group (without a role). One row per user/group/permission_key combination.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``user_id``
     - INTEGER
     - Joins to ``users.id``.
   * - ``group_id``
     - INTEGER
     - Joins to ``permission_groups.id``.
   * - ``permission_key``
     - VARCHAR(20)
     - The permission level: ``ro``, ``move_into``, ``create``, ``note``, ``owner``, ``priority``, or ``rw``.

``role_user`` — agent → role membership
========================================

Associates agents with roles. Contains no permission key — the permissions come from ``group_role``.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Column
     - Type
     - Description
   * - ``user_id``
     - INTEGER
     - Joins to ``users.id``.
   * - ``role_id``
     - INTEGER
     - Joins to ``roles.id``.

``group_role`` — role → group permission assignment
====================================================

Associates roles with groups and permission keys. One row per role/group/permission_key combination.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``role_id``
     - INTEGER
     - Joins to ``roles.id``.
   * - ``group_id``
     - INTEGER
     - Joins to ``permission_groups.id``.
   * - ``permission_key``
     - VARCHAR(20)
     - The permission type (see keys above).
   * - ``permission_value``
     - SMALLINT
     - ``1`` = permission granted, ``0`` = permission explicitly withdrawn.

``group_customer`` — customer company → group
=============================================

Grants a customer company (organization) access to a group.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``customer_id``
     - VARCHAR(150)
     - Joins to ``customer_company.customer_id``.
   * - ``group_id``
     - INTEGER
     - Joins to ``permission_groups.id``.
   * - ``permission_key``
     - VARCHAR(20)
     - Permission type.
   * - ``permission_value``
     - SMALLINT
     - ``1`` = granted, ``0`` = withdrawn.
   * - ``permission_context``
     - VARCHAR(100)
     - Context for the permission (e.g. ``Customer::Self`` or ``Customer::Other``).

``group_customer_user`` — customer contact → group
===================================================

Grants an individual customer user access to a group. ``user_id`` here is the customer login (a string), not an integer.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``user_id``
     - VARCHAR(100)
     - Joins to ``customer_user.login``.
   * - ``group_id``
     - INTEGER
     - Joins to ``permission_groups.id``.
   * - ``permission_key``
     - VARCHAR(20)
     - Permission type.
   * - ``permission_value``
     - SMALLINT
     - ``1`` = granted, ``0`` = withdrawn.

Permission Queries
******************

All groups an agent belongs to (direct + via role):

.. code-block:: sql

    -- Direct group memberships
    SELECT
        u.login,
        CONCAT(u.first_name, ' ', u.last_name)  AS agent,
        pg.name                                  AS group_name,
        gu.permission_key,
        'direct'                                 AS source
    FROM   group_user        gu
    JOIN   users             u  ON  u.id = gu.user_id
    JOIN   permission_groups pg ON pg.id = gu.group_id
    WHERE  u.login = 'agent.login'

    UNION ALL

    -- Via role
    SELECT
        u.login,
        CONCAT(u.first_name, ' ', u.last_name)  AS agent,
        pg.name                                  AS group_name,
        gr.permission_key,
        CONCAT('role:', r.name)                  AS source
    FROM   role_user         ru
    JOIN   users             u  ON  u.id  = ru.user_id
    JOIN   roles             r  ON  r.id  = ru.role_id
    JOIN   group_role        gr ON gr.role_id = ru.role_id AND gr.permission_value = 1
    JOIN   permission_groups pg ON pg.id = gr.group_id
    WHERE  u.login = 'agent.login'

    ORDER BY group_name, permission_key;

All agents who have rw access to a specific group:

.. code-block:: sql

    SELECT DISTINCT
        u.login,
        CONCAT(u.first_name, ' ', u.last_name)  AS agent,
        src.source
    FROM (
        -- Direct rw
        SELECT gu.user_id, 'direct' AS source
        FROM   group_user        gu
        JOIN   permission_groups pg ON pg.id = gu.group_id
        WHERE  pg.name            = 'admin'
        AND    gu.permission_key  = 'rw'

        UNION

        -- Via role rw
        SELECT ru.user_id, CONCAT('role:', r.name) AS source
        FROM   role_user         ru
        JOIN   roles             r  ON  r.id = ru.role_id
        JOIN   group_role        gr ON gr.role_id = ru.role_id
        JOIN   permission_groups pg ON pg.id = gr.group_id
        WHERE  pg.name            = 'admin'
        AND    gr.permission_key  = 'rw'
        AND    gr.permission_value = 1
    ) src
    JOIN users u ON u.id = src.user_id
    WHERE u.valid_id = 1
    ORDER BY agent;

All roles and their group permissions (full permission matrix):

.. code-block:: sql

    SELECT
        r.name                   AS role,
        pg.name                  AS group_name,
        gr.permission_key,
        gr.permission_value
    FROM   group_role        gr
    JOIN   roles             r  ON  r.id = gr.role_id
    JOIN   permission_groups pg ON pg.id = gr.group_id
    WHERE  r.valid_id = 1
    ORDER BY r.name, pg.name, gr.permission_key;

All permissions for one agent (flat view — direct and role-based combined):

.. code-block:: sql

    SELECT DISTINCT
        pg.name             AS group_name,
        perm.permission_key,
        perm.source
    FROM (
        SELECT gu.group_id, gu.permission_key, 'direct' AS source
        FROM   group_user gu
        JOIN   users u ON u.id = gu.user_id
        WHERE  u.login = 'agent.login'

        UNION

        SELECT gr.group_id, gr.permission_key,
               CONCAT('role:', r.name) AS source
        FROM   role_user  ru
        JOIN   users      u  ON  u.id  = ru.user_id
        JOIN   roles      r  ON  r.id  = ru.role_id
        JOIN   group_role gr ON gr.role_id = ru.role_id
        WHERE  u.login            = 'agent.login'
        AND    gr.permission_value = 1
    ) perm
    JOIN permission_groups pg ON pg.id = perm.group_id
    ORDER BY pg.name, perm.permission_key;

Agents with no group or role assignments (orphaned users):

.. code-block:: sql

    SELECT u.login, CONCAT(u.first_name, ' ', u.last_name) AS agent
    FROM   users u
    WHERE  u.valid_id = 1
    AND    u.id NOT IN (SELECT user_id FROM group_user)
    AND    u.id NOT IN (SELECT user_id FROM role_user)
    ORDER BY u.last_name;

Customer company group access:

.. code-block:: sql

    SELECT
        cc.name                AS company,
        pg.name                AS group_name,
        gc.permission_key,
        gc.permission_context
    FROM   group_customer    gc
    JOIN   customer_company  cc ON cc.customer_id = gc.customer_id
    JOIN   permission_groups pg ON pg.id = gc.group_id
    WHERE  gc.permission_value = 1
    ORDER BY cc.name, pg.name;
