.. meta::
   :description: Znuny ticket_history table — complete audit trail of ticket events for SLA reporting, change tracking, and compliance queries.
   :keywords: znuny ticket history, znuny audit trail, znuny sla reporting, znuny ticket_history schema

.. _PageNavigation annexes_database_history:

History and Audit Trail
#######################

The ``ticket_history`` table is a complete, append-only log of everything that ever happened to a ticket. Every state change, owner change, queue transfer, note, email sent, or attribute update writes a row here. It is the primary source for SLA reporting, response-time analysis, and compliance audit trails.

The ``ticket_history`` Table
*****************************

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``id``
     - BIGINT
     - Primary key.
   * - ``name``
     - VARCHAR(200)
     - Human-readable description of the event (e.g. ``%%open%%new%%``, ``%%agent@example.com%%``). The format varies by history type — see the note below.
   * - ``history_type_id``
     - SMALLINT
     - The category of event. Joins to ``ticket_history_type.id``.
   * - ``ticket_id``
     - BIGINT
     - The ticket this event belongs to. Joins to ``ticket.id``.
   * - ``article_id``
     - BIGINT
     - The article associated with this event, if any (e.g. when an email is sent). NULL otherwise.
   * - ``type_id``
     - SMALLINT
     - The ticket type at the time of the event. Joins to ``ticket_type.id``.
   * - ``queue_id``
     - INTEGER
     - The queue the ticket was in at the time of the event. Joins to ``queue.id``.
   * - ``owner_id``
     - INTEGER
     - The ticket owner at the time of the event. Joins to ``users.id``.
   * - ``priority_id``
     - SMALLINT
     - The ticket priority at the time of the event. Joins to ``ticket_priority.id``.
   * - ``state_id``
     - SMALLINT
     - The ticket state at the time of the event. Joins to ``ticket_state.id``.
   * - ``create_time``
     - DATETIME
     - When the event occurred. This is the timestamp to use for all time-based history queries.
   * - ``create_by``
     - INTEGER
     - Agent who triggered the event. Joins to ``users.id``.

.. note::

    The ``name`` column stores a structured string whose format depends on the history type. For state changes it looks like ``%%open%%new%%`` (old state %% new state). For email events it may contain the recipient address. For reporting purposes, rely on ``history_type_id``/``ticket_history_type.name`` to filter event types, and use ``create_time`` for timing — avoid parsing ``name`` unless you need its specific content.

``ticket_history_type`` — resolves ``ticket_history.history_type_id``
======================================================================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Name
     - When it is written
   * - ``NewTicket``
     - Ticket was created.
   * - ``StateUpdate``
     - Ticket state changed.
   * - ``OwnerUpdate``
     - Owner changed.
   * - ``ResponsibleUpdate``
     - Responsible agent changed.
   * - ``PriorityUpdate``
     - Priority changed.
   * - ``Move``
     - Ticket moved to a different queue.
   * - ``TitleUpdate``
     - Ticket title changed.
   * - ``TypeUpdate``
     - Ticket type changed.
   * - ``CustomerUpdate``
     - Customer contact or organization changed.
   * - ``ServiceUpdate``
     - Associated service changed.
   * - ``SLAUpdate``
     - Associated SLA changed.
   * - ``EmailAgent``
     - Agent sent an email.
   * - ``EmailCustomer``
     - Customer sent an email (inbound).
   * - ``SendAnswer``
     - Agent sent a reply.
   * - ``PhoneCallAgent``
     - Agent created a phone-call note (outbound).
   * - ``PhoneCallCustomer``
     - Agent created a phone-call note (inbound from customer).
   * - ``AddNote``
     - Note added to the ticket. Whether it is internal or customer-visible is determined by ``article.is_visible_for_customer``.
   * - ``FollowUp``
     - Customer sent a reply to an existing ticket (inbound email or message creating a new article).
   * - ``SetPendingTime``
     - The pending-until time was set or changed.
   * - ``TicketDynamicFieldUpdate``
     - A dynamic field value on the ticket was changed.
   * - ``Merged``
     - Ticket was merged into another ticket.
   * - ``Lock``
     - Ticket was locked.
   * - ``Unlock``
     - Ticket was unlocked.
   * - ``EscalationSolutionTimeStart``
     - Solution escalation clock started.
   * - ``EscalationSolutionTimeStop``
     - Solution escalation clock stopped (resolved before deadline).
   * - ``EscalationResponseTimeStart``
     - First-response escalation clock started.
   * - ``EscalationResponseTimeStop``
     - First-response escalation clock stopped.
   * - ``EscalationUpdateTimeStart``
     - Update escalation clock started.
   * - ``EscalationUpdateTimeStop``
     - Update escalation clock stopped.

Common History Queries
**********************

When was a ticket first responded to?

.. code-block:: sql

    -- First agent response per ticket (first EmailAgent or SendAnswer event)
    SELECT
        th.ticket_id,
        MIN(th.create_time) AS first_response_at
    FROM   ticket_history      th
    JOIN   ticket_history_type tht ON tht.id = th.history_type_id
    WHERE  tht.name IN ('EmailAgent', 'SendAnswer', 'PhoneCallAgent')
    GROUP BY th.ticket_id;

Average first-response time per queue (in minutes):

.. code-block:: sql

    SELECT
        q.name                                       AS queue,
        ROUND(AVG(
            TIMESTAMPDIFF(MINUTE, t.create_time, fr.first_response_at)
        ))                                           AS avg_first_response_min
    FROM ticket t
    JOIN queue q ON q.id = t.queue_id
    JOIN (
        SELECT   th.ticket_id, MIN(th.create_time) AS first_response_at
        FROM     ticket_history th
        JOIN     ticket_history_type tht ON tht.id = th.history_type_id
        WHERE    tht.name IN ('EmailAgent', 'SendAnswer', 'PhoneCallAgent')
        GROUP BY th.ticket_id
    ) fr ON fr.ticket_id = t.id
    WHERE t.create_time >= DATE_SUB(NOW(), INTERVAL 30 DAY)
    AND   t.archive_flag = 0
    GROUP BY q.id, q.name
    ORDER BY avg_first_response_min;

Full state-change timeline for one ticket:

.. code-block:: sql

    SELECT
        th.create_time,
        tht.name                                     AS event_type,
        th.name                                      AS detail,
        CONCAT(u.first_name, ' ', u.last_name)       AS agent
    FROM   ticket_history      th
    JOIN   ticket_history_type tht ON tht.id = th.history_type_id
    JOIN   users               u   ON  u.id  = th.create_by
    WHERE  th.ticket_id = :ticket_id
    ORDER BY th.create_time;

Tickets that escalated in the last 7 days (by history event):

.. code-block:: sql

    SELECT DISTINCT
        t.tn,
        t.title,
        th.create_time AS escalated_at,
        q.name         AS queue
    FROM   ticket_history      th
    JOIN   ticket_history_type tht ON tht.id = th.history_type_id
    JOIN   ticket              t   ON  t.id  = th.ticket_id
    JOIN   queue               q   ON  q.id  = t.queue_id
    WHERE  tht.name IN (
               'EscalationSolutionTimeStart',
               'EscalationResponseTimeStart',
               'EscalationUpdateTimeStart'
           )
    AND    th.create_time >= DATE_SUB(NOW(), INTERVAL 7 DAY);
