.. meta::
   :description: Znuny SQL reporting examples — eight complete, tested queries for common BI and reporting use cases.
   :keywords: znuny sql examples, znuny reporting queries, znuny bi queries, znuny sql reporting

.. _PageNavigation annexes_database_examples:

SQL Query Examples
##################

Eight complete queries covering the most common Znuny reporting use cases. All queries have been tested against a live Znuny database. Run them in Admin → SQL Box or via a direct database connection.

.. note::

    All queries filter ``archive_flag = 0`` to exclude archived tickets unless the example specifically addresses archived tickets.

1. Open Tickets per Queue with Owner Name
*****************************************

.. code-block:: sql

    SELECT
        q.name                                         AS queue,
        COUNT(*)                                       AS open_tickets,
        CONCAT(u.first_name, ' ', u.last_name)         AS owner
    FROM   ticket t
    JOIN   ticket_state      ts ON ts.id = t.ticket_state_id
    JOIN   ticket_state_type st ON st.id = ts.type_id
    JOIN   queue             q  ON  q.id = t.queue_id
    JOIN   users             u  ON  u.id = t.user_id
    WHERE  st.name    = 'open'
    AND    t.archive_flag = 0
    GROUP BY q.id, q.name, u.id, u.first_name, u.last_name
    ORDER BY q.name, open_tickets DESC;

2. Ticket Volume by State — Last 30 Days
*****************************************

.. code-block:: sql

    SELECT
        ts.name  AS state,
        COUNT(*) AS tickets
    FROM   ticket t
    JOIN   ticket_state ts ON ts.id = t.ticket_state_id
    WHERE  t.create_time >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    AND    t.archive_flag  = 0
    GROUP BY ts.id, ts.name
    ORDER BY tickets DESC;

3. Average First-Response Time per Queue (Minutes)
***************************************************

Uses ``ticket_history`` to find when the first agent response was sent per ticket, then averages the gap from ticket creation.

.. code-block:: sql

    SELECT
        q.name                                        AS queue,
        COUNT(DISTINCT t.id)                          AS tickets,
        ROUND(AVG(
            TIMESTAMPDIFF(MINUTE, t.create_time, fr.first_response_at)
        ))                                            AS avg_first_response_min
    FROM ticket t
    JOIN queue q ON q.id = t.queue_id
    JOIN (
        SELECT   th.ticket_id,
                 MIN(th.create_time) AS first_response_at
        FROM     ticket_history      th
        JOIN     ticket_history_type tht ON tht.id = th.history_type_id
        WHERE    tht.name IN ('EmailAgent', 'SendAnswer', 'PhoneCallAgent')
        GROUP BY th.ticket_id
    ) fr ON fr.ticket_id = t.id
    WHERE t.create_time  >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    AND   t.archive_flag  = 0
    GROUP BY q.id, q.name
    ORDER BY avg_first_response_min;

4. All Inbound Emails Received Today
*************************************

.. code-block:: sql

    SELECT
        t.tn,
        adm.a_from        AS sender,
        adm.a_subject     AS subject,
        a.create_time     AS received_at,
        q.name            AS queue
    FROM   article               a
    JOIN   article_data_mime     adm ON adm.article_id = a.id
    JOIN   article_sender_type   ast ON ast.id = a.article_sender_type_id
    JOIN   communication_channel cc  ON  cc.id = a.communication_channel_id
    JOIN   ticket                t   ON  t.id  = a.ticket_id
    JOIN   queue                 q   ON  q.id  = t.queue_id
    WHERE  ast.name            = 'customer'
    AND    cc.name             = 'Email'
    AND    DATE(a.create_time) = CURDATE()
    ORDER BY a.create_time DESC;

5. Tickets with a Specific Dynamic Field Value
***********************************************

Replace ``'Category'`` with the internal field name and ``'Hardware'`` with the value you are looking for.

.. code-block:: sql

    SELECT
        t.tn,
        t.title,
        dfv.value_text  AS category,
        t.create_time
    FROM   ticket              t
    JOIN   dynamic_field_value dfv ON dfv.object_id = t.id
    JOIN   dynamic_field       df  ON df.id = dfv.field_id
    WHERE  df.name        = 'Category'
    AND    df.object_type = 'Ticket'
    AND    dfv.value_text = 'Hardware'
    AND    t.archive_flag = 0
    ORDER BY t.create_time DESC;

6. Tickets by Priority × State (Pivot)
***************************************

.. code-block:: sql

    SELECT
        tp.name                                        AS priority,
        SUM(CASE WHEN tst.name = 'new'    THEN 1 ELSE 0 END)  AS new_tickets,
        SUM(CASE WHEN tst.name = 'open'   THEN 1 ELSE 0 END)  AS open_tickets,
        SUM(CASE WHEN tst.name = 'closed' THEN 1 ELSE 0 END)  AS closed_tickets,
        COUNT(*)                                       AS total
    FROM   ticket              t
    JOIN   ticket_priority     tp  ON tp.id  = t.ticket_priority_id
    JOIN   ticket_state        ts  ON ts.id  = t.ticket_state_id
    JOIN   ticket_state_type   tst ON tst.id = ts.type_id
    WHERE  t.create_time  >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    AND    t.archive_flag  = 0
    GROUP BY tp.id, tp.name
    ORDER BY tp.id;

7. Currently Escalated Tickets
*******************************

Tickets where any escalation clock has passed its deadline right now.

.. code-block:: sql

    SELECT
        t.tn,
        t.title,
        q.name                                           AS queue,
        CONCAT(u.first_name, ' ', u.last_name)           AS owner,
        FROM_UNIXTIME(t.escalation_time)                 AS escalated_at,
        CASE
            WHEN t.escalation_response_time > 0
             AND t.escalation_response_time < UNIX_TIMESTAMP(NOW())
            THEN 'First Response'
            WHEN t.escalation_update_time > 0
             AND t.escalation_update_time < UNIX_TIMESTAMP(NOW())
            THEN 'Update'
            WHEN t.escalation_solution_time > 0
             AND t.escalation_solution_time < UNIX_TIMESTAMP(NOW())
            THEN 'Solution'
            ELSE 'Other'
        END                                              AS escalation_type
    FROM   ticket t
    JOIN   queue  q ON q.id = t.queue_id
    JOIN   users  u ON u.id = t.user_id
    WHERE  t.escalation_time  > 0
    AND    t.escalation_time  < UNIX_TIMESTAMP(NOW())
    AND    t.archive_flag     = 0
    ORDER BY t.escalation_time;

8. Customer Companies Ranked by Open Ticket Count
**************************************************

.. code-block:: sql

    SELECT
        COALESCE(cc.name, t.customer_id)               AS company,
        COUNT(*)                                        AS open_tickets
    FROM   ticket               t
    LEFT JOIN customer_company  cc  ON cc.customer_id = t.customer_id
    JOIN   ticket_state         ts  ON ts.id = t.ticket_state_id
    JOIN   ticket_state_type    tst ON tst.id = ts.type_id
    WHERE  tst.name       IN ('new', 'open')
    AND    t.archive_flag  = 0
    AND    t.customer_id  IS NOT NULL
    AND    t.customer_id  != ''
    GROUP BY t.customer_id, cc.name
    ORDER BY open_tickets DESC
    LIMIT 25;
