.. meta::
   :description: Znuny dynamic fields database schema — EAV pattern, dynamic_field, dynamic_field_value, dynamic_field_obj_id_name, join patterns for SQL reporting.
   :keywords: znuny dynamic fields schema, znuny eav pattern, znuny dynamic field sql, znuny dynamic field reporting

.. _PageNavigation annexes_database_dynamic_fields:

Dynamic Fields
##############

Dynamic fields are Znuny's extensible custom-field system. They are stored using the **Entity–Attribute–Value (EAV)** pattern across three tables. This pattern is efficient for a variable number of fields but requires a specific join pattern that differs from ordinary column lookups.

The Three Tables
****************

``dynamic_field`` — field definitions
======================================

One row per configured dynamic field. This table tells you what fields exist and what type they are.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``id``
     - INTEGER
     - Primary key. Referenced by ``dynamic_field_value.field_id``.
   * - ``name``
     - VARCHAR(200)
     - Internal field name (no spaces). This is what you filter on in queries.
   * - ``label``
     - VARCHAR(200)
     - Display label shown in the UI.
   * - ``field_type``
     - VARCHAR(200)
     - The field type: ``Text``, ``TextArea``, ``Date``, ``DateTime``, ``Dropdown``, ``Multiselect``, ``Checkbox``, ``Database``, etc.
   * - ``object_type``
     - VARCHAR(100)
     - Which object type this field is attached to: ``Ticket``, ``Article``, or ``CustomerUser``.
   * - ``field_order``
     - INTEGER
     - Display order in the UI.
   * - ``valid_id``
     - SMALLINT
     - ``1`` = active. Joins to ``valid.id``.

``dynamic_field_value`` — stored values
========================================

One row per field value per object. Three value columns exist; only one is populated per row depending on the field type.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``id``
     - INTEGER
     - Primary key.
   * - ``field_id``
     - INTEGER
     - Which field this value belongs to. Joins to ``dynamic_field.id``.
   * - ``object_id``
     - BIGINT
     - The ID of the object this value is attached to. For ``object_type = 'Ticket'`` this is ``ticket.id``. For ``object_type = 'Article'`` this is ``article.id``. For ``object_type = 'CustomerUser'`` this is ``dynamic_field_obj_id_name.object_id`` (see below).
   * - ``value_text``
     - TEXT
     - Populated for: Text, TextArea, Dropdown, Multiselect, Checkbox fields.
   * - ``value_date``
     - DATETIME
     - Populated for: Date, DateTime fields.
   * - ``value_int``
     - BIGINT
     - Populated for: integer-type fields.

``dynamic_field_obj_id_name`` — object name bridge
====================================================

This table is only needed when querying ``CustomerUser`` dynamic fields. Because ``customer_user.login`` is a string, the system cannot use it directly as ``object_id`` (which must be an integer). This bridge table maps a surrogate integer ``object_id`` to the actual string login name.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``object_id``
     - INTEGER
     - The surrogate integer used as ``dynamic_field_value.object_id`` for ``CustomerUser`` fields.
   * - ``object_name``
     - VARCHAR(200)
     - The actual ``customer_user.login`` value.
   * - ``object_type``
     - VARCHAR(100)
     - Always ``CustomerUser`` in this context.

How the EAV Pattern Works
*************************

For a ``Ticket`` dynamic field, the relationship is direct:

.. code-block:: text

    ticket.id  ──────────────────►  dynamic_field_value.object_id
                                    dynamic_field_value.field_id  ──►  dynamic_field.id

For a ``CustomerUser`` dynamic field, a bridge table is needed:

.. code-block:: text

    customer_user.login  ──►  dynamic_field_obj_id_name.object_name
                              dynamic_field_obj_id_name.object_id  ──►  dynamic_field_value.object_id
                                                                        dynamic_field_value.field_id  ──►  dynamic_field.id

Which Value Column to Read
**************************

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Field type
     - Value column
   * - Text, TextArea
     - ``value_text``
   * - Dropdown, Multiselect
     - ``value_text``
   * - Checkbox
     - ``value_text`` (``0`` or ``1``)
   * - Date, DateTime
     - ``value_date``
   * - Integer fields
     - ``value_int``

Multi-Value Fields
******************

**Multiselect** and similar fields store **one row per selected option**. If a field has three options selected, ``dynamic_field_value`` will have three rows with the same ``field_id`` and ``object_id``.

A straight ``JOIN`` on a multi-value field will multiply your result rows. Use ``GROUP_CONCAT`` or a subquery to aggregate:

.. code-block:: sql

    -- Collect all selected options for a Multiselect field into one cell
    SELECT
        t.tn,
        GROUP_CONCAT(dfv.value_text ORDER BY dfv.value_text SEPARATOR ', ') AS selected_options
    FROM   ticket t
    JOIN   dynamic_field_value dfv ON dfv.object_id = t.id
    JOIN   dynamic_field       df  ON df.id = dfv.field_id
    WHERE  df.name        = 'YourMultiselectFieldName'
    AND    df.object_type = 'Ticket'
    AND    t.archive_flag = 0
    GROUP BY t.id, t.tn;

Query Patterns
**************

Get all dynamic field values for one ticket:

.. code-block:: sql

    SELECT
        df.name         AS field_name,
        df.field_type,
        dfv.value_text,
        dfv.value_date,
        dfv.value_int
    FROM   dynamic_field       df
    JOIN   dynamic_field_value dfv ON dfv.field_id = df.id
    WHERE  df.object_type = 'Ticket'
    AND    dfv.object_id  = :ticket_id;

Filter tickets by a specific dynamic field value (Dropdown):

.. code-block:: sql

    SELECT t.tn, t.title, t.create_time
    FROM   ticket t
    JOIN   dynamic_field_value dfv ON dfv.object_id = t.id
    JOIN   dynamic_field       df  ON df.id = dfv.field_id
    WHERE  df.name        = 'Category'
    AND    df.object_type = 'Ticket'
    AND    dfv.value_text = 'Hardware'
    AND    t.archive_flag = 0;

Filter tickets by a DateTime dynamic field within a range:

.. code-block:: sql

    SELECT t.tn, t.title, dfv.value_date AS due_date
    FROM   ticket t
    JOIN   dynamic_field_value dfv ON dfv.object_id = t.id
    JOIN   dynamic_field       df  ON df.id = dfv.field_id
    WHERE  df.name        = 'DueDate'
    AND    df.object_type = 'Ticket'
    AND    dfv.value_date BETWEEN '2024-01-01' AND '2024-12-31'
    AND    t.archive_flag = 0;

Get a CustomerUser dynamic field value:

.. code-block:: sql

    SELECT
        cu.login,
        dfv.value_text AS department
    FROM   customer_user          cu
    JOIN   dynamic_field_obj_id_name dion ON dion.object_name = cu.login
                                         AND dion.object_type = 'CustomerUser'
    JOIN   dynamic_field_value    dfv  ON dfv.object_id = dion.object_id
    JOIN   dynamic_field          df   ON df.id = dfv.field_id
    WHERE  df.name        = 'Department'
    AND    df.object_type = 'CustomerUser';
