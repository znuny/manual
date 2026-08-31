.. meta::
   :description: Znuny article tables — article, article_data_mime, communication_channel, and article_sender_type for reporting and SQL queries.
   :keywords: znuny article table, znuny email storage, znuny article schema, znuny communication log

.. _PageNavigation annexes_database_articles:

Articles
########

An article is a single communication record attached to a ticket — an inbound email, an outbound reply, a phone-call note, an internal note, or a chat message. Every article belongs to exactly one ticket.

Article storage is split across two tables: ``article`` holds the metadata common to all communication channels, and ``article_data_mime`` holds the email-specific content (subject, body, headers).

The ``article`` Table
*********************

One row per communication event. Contains channel and visibility metadata.

.. list-table::
   :header-rows: 1
   :widths: 28 15 57

   * - Column
     - Type
     - Description
   * - ``id``
     - BIGINT
     - Primary key. Referenced by ``article_data_mime.article_id`` and ``ticket_history.article_id``.
   * - ``ticket_id``
     - BIGINT
     - The ticket this article belongs to. Joins to ``ticket.id``.
   * - ``article_sender_type_id``
     - SMALLINT
     - Who sent this article (agent, customer, or system). Joins to ``article_sender_type.id``.
   * - ``communication_channel_id``
     - BIGINT
     - Which channel the article came through. Joins to ``communication_channel.id``.
   * - ``is_visible_for_customer``
     - SMALLINT
     - ``1`` = visible in the customer portal, ``0`` = internal (agents only).
   * - ``create_time``
     - DATETIME
     - When the article was created.
   * - ``create_by``
     - INTEGER
     - Agent who created the article. Joins to ``users.id``.

The ``article_data_mime`` Table
*******************************

One row per MIME (email) article. Contains the actual message content. Always joined to ``article`` via ``article_id``.

.. list-table::
   :header-rows: 1
   :widths: 22 15 63

   * - Column
     - Type
     - Description
   * - ``id``
     - BIGINT
     - Primary key.
   * - ``article_id``
     - BIGINT
     - Joins to ``article.id``.
   * - ``a_from``
     - MEDIUMTEXT
     - The From header (sender name and address).
   * - ``a_reply_to``
     - MEDIUMTEXT
     - The Reply-To header.
   * - ``a_to``
     - MEDIUMTEXT
     - The To header.
   * - ``a_cc``
     - MEDIUMTEXT
     - The Cc header.
   * - ``a_bcc``
     - MEDIUMTEXT
     - The Bcc header.
   * - ``a_subject``
     - TEXT
     - The email subject line.
   * - ``a_message_id``
     - TEXT
     - The RFC 2822 Message-ID header. Used for threading.
   * - ``a_body``
     - MEDIUMTEXT
     - The message body. May be plain text or HTML depending on ``a_content_type``.
   * - ``a_content_type``
     - VARCHAR(250)
     - MIME content type of the body (e.g. ``text/plain; charset=utf-8``).
   * - ``incoming_time``
     - INTEGER
     - Unix epoch of when the message was received. ``0`` for outbound messages.
   * - ``create_time``
     - DATETIME
     - When the record was written.

Sender Type and Channel
***********************

``article_sender_type`` — resolves ``article.article_sender_type_id``

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Meaning
   * - ``agent``
     - Written or sent by a Znuny agent.
   * - ``customer``
     - Sent by a customer contact.
   * - ``system``
     - Generated automatically by the system.

``communication_channel`` — resolves ``article.communication_channel_id``

Standard channels:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Name
     - Meaning
   * - ``Email``
     - MIME email (inbound or outbound).
   * - ``Phone``
     - Phone call note created by an agent.
   * - ``Internal``
     - Internal note, not visible to customers.
   * - ``Chat``
     - Chat message (if the chat feature is enabled).

Typical Article Queries
***********************

All external emails on a ticket:

.. code-block:: sql

    SELECT
        adm.a_from,
        adm.a_to,
        adm.a_subject,
        adm.a_body,
        a.create_time,
        ast.name  AS sender_type,
        cc.name   AS channel
    FROM   article                a
    JOIN   article_data_mime      adm ON adm.article_id = a.id
    JOIN   article_sender_type    ast ON ast.id = a.article_sender_type_id
    JOIN   communication_channel  cc  ON  cc.id = a.communication_channel_id
    WHERE  a.ticket_id = :ticket_id
    AND    a.is_visible_for_customer = 1
    ORDER BY a.create_time;

Count of inbound emails received per day:

.. code-block:: sql

    SELECT
        DATE(a.create_time)  AS day,
        COUNT(*)             AS inbound_emails
    FROM   article               a
    JOIN   article_sender_type   ast ON ast.id = a.article_sender_type_id
    JOIN   communication_channel cc  ON  cc.id = a.communication_channel_id
    WHERE  ast.name = 'customer'
    AND    cc.name  = 'Email'
    GROUP BY DATE(a.create_time)
    ORDER BY day DESC;
