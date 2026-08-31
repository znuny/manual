.. meta::
   :description: Znuny database reference for reporting, BI tools, and ad-hoc SQL — data model, table schemas, dynamic fields, and worked query examples.
   :keywords: znuny database, znuny schema, znuny reporting, znuny bi, znuny sql, znuny data model

.. _PageNavigation annexes_database:

Database Reference
##################

This reference is a learning path for analysts and developers who want to query the Znuny database directly — to build reports, connect BI tools (Metabase, Power BI, Tableau), or write ad-hoc SQL for data extraction.

The Znuny database has 119 tables. For the vast majority of reporting use cases you need to know roughly 15 of them. This reference covers those 15 and explains how they relate to each other.

**Prerequisites:** You need SELECT access to the database. The built-in SQL Box (**Admin → SQL Box**) is the easiest way to run queries without direct database access — it allows SELECT, SHOW, and DESC statements by default.

.. toctree::
   :maxdepth: 1

   data_model
   ticket_table
   lookup_tables
   articles
   dynamic_fields
   history
   permissions
   examples

Sections at a glance
********************

:doc:`data_model`
    The four core entities — Ticket, Article, User/Customer, Queue — and how they relate. Start here.

:doc:`ticket_table`
    Every column in the ``ticket`` table explained for a reporting audience, including escalation time fields and the archive flag.

:doc:`lookup_tables`
    The small reference tables that resolve ID columns to human-readable names. A join cheat-sheet you will use in every query.

:doc:`articles`
    The ``article`` and ``article_data_mime`` tables — where email bodies, subjects, senders, and recipients are stored.

:doc:`dynamic_fields`
    How dynamic fields are stored using the Entity–Attribute–Value (EAV) pattern across three tables, including the ``dynamic_field_obj_id_name`` bridge table for non-ticket objects.

:doc:`history`
    The ``ticket_history`` table — a complete audit trail of every state change, owner change, and communication event on every ticket.

:doc:`permissions`
    Roles, groups, and the six permission keys — how to query which agents have access to which groups, directly or via roles, and the equivalent tables for customer access.

:doc:`examples`
    Eight complete, tested SQL queries covering the most common reporting needs.
