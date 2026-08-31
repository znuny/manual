.. meta::
   :description: Reference for all Znuny statistic Object modules — what each module queries, which attributes are available for X-axis, Y-axis, and filters, and any special return-value or performance characteristics.
   :keywords: znuny statistics modules, stat object module, TicketAccumulation, TicketList, TicketAccountedTime, TicketSolutionResponseTime, ITSMConfigItem, ITSMTicketFirstLevelSolutionRate, ITSMTicketSolutionTimeAverage, ITSMChangeManagement

.. _PageNavigation annexes_stats_module_reference:

Statistics Object Module Reference
####################################

Each dynamic statistic is backed by an **Object module** that defines what data is queried and which attributes are available for use as X-axis, Y-axis (series), or filter. When creating or cloning a statistic in **Reports → Statistics**, the Object dropdown lists all installed modules.

The following modules are available. The first four are part of the base Znuny system; the remaining modules are installed by the ITSM packages.

.. contents::
   :local:
   :depth: 1

----

.. _stats-module-ticketaccumulation:

TicketAccumulation
*******************

**Module**: ``Kernel::System::Stats::Dynamic::Ticket``

**What it counts**: The number of tickets returned by ``TicketSearch`` that match all configured axis and filter values. Each cell value is a simple count.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - Type
     - ✓
     - ✓
     - ✓
     - Only present when ``Ticket::Type`` is enabled in SysConfig.
   * - Service
     - ✓
     - ✓
     - ✓
     - Only present when ``Ticket::Service`` is enabled.
   * - SLA
     - ✓
     - ✓
     - ✓
     - Only present when ``Ticket::Service`` is enabled.
   * - Queue
     - ✓
     - ✓
     - ✓
     -
   * - State
     - ✓
     - ✓
     - ✓
     - List is pre-filtered to closed states only by default.
   * - Priority
     - ✓
     - ✓
     - ✓
     -
   * - Created in Queue
     - ✓
     - ✓
     - ✓
     - The queue the ticket was in when first created.
   * - Created State
     - ✓
     - ✓
     - ✓
     -
   * - Created Priority
     - ✓
     - ✓
     - ✓
     -
   * - Agent/Owner
     - ✓
     - ✓
     - ✓
     - Only present when ``Stats::UseAgentElementInStats`` is enabled.
   * - Created by Agent/Owner
     - ✓
     - ✓
     - ✓
     - Only present when ``Stats::UseAgentElementInStats`` is enabled.
   * - Responsible
     - ✓
     - ✓
     - ✓
     - Only present when ``Stats::UseAgentElementInStats`` is enabled.
   * - CustomerID
     - ✓ *
     - ✓ *
     - ✓
     - X/Y available only when ``Stats::CustomerIDAsMultiSelect`` is enabled; otherwise filter-only.
   * - Create Time
     - ✓
     - ✓
     - ✓
     - Time period selector (start/stop date).
   * - Title
     - —
     - —
     - ✓
     - Text pattern match.
   * - CustomerUserLogin
     - —
     - —
     - ✓
     - Text pattern match.
   * - From / To / Cc / Subject / Body
     - —
     - —
     - ✓
     - Article-level text filters.
   * - Dynamic Fields
     - ✓ *
     - ✓ *
     - ✓
     - Select-type dynamic fields can be used as axes; text-type fields are filter-only.

----

.. _stats-module-ticketaccountedtime:

TicketAccountedTime
********************

**Module**: ``Kernel::System::Stats::Dynamic::TicketAccountedTime``

**What it measures**: Time manually booked against tickets and articles by agents using the time accounting field. Values are read from the ``time_accounting`` table, not derived from ticket history. Only time that agents have explicitly entered is counted.

**Evaluation by (mandatory axis)**: Unlike most modules, TicketAccountedTime requires the **Evaluation by** attribute to be placed on one axis. This selects what each cell reports:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Reporting mode
     - Description
   * - Total Time
     - Sum of all time units booked against matching tickets/articles. Returned as a decimal number of minutes.
   * - Ticket Average
     - Mean booked time per ticket.
   * - Ticket Min Time
     - Lowest total booked time across matching tickets.
   * - Ticket Max Time
     - Highest total booked time across matching tickets.
   * - Number of Tickets
     - Count of tickets that have at least one time booking in the period.
   * - Article Average
     - Mean booked time per individual article.
   * - Article Min Time
     - Lowest booked time on a single article.
   * - Article Max Time
     - Highest booked time on a single article.
   * - Number of Articles
     - Count of articles with at least one time booking.

**Additional attributes**: Queue, State, State Type, Priority, Created Queue/State/Priority, Lock, From/To/Cc/Subject/Body text, Ticket/Article Accounted Time (date range), Ticket Create Time, Last Changed Time, Change Time, Ticket Close Time, Escalation times (First Response / Update / Solution), Service, SLA, Type, Archive Search, Agent/Owner and Accounted Time by Agent (when ``Stats::UseAgentElementInStats`` is enabled), Dynamic Fields.

**Special behaviour**: The **Accounted time by Agent** sub-attribute (gated by ``Stats::UseAgentElementInStats``) breaks the time totals down by the agent who entered each booking, not the ticket owner. This allows per-agent time-tracking reports within the same stat.

----

.. _stats-module-ticketsolutionresponsetime:

TicketSolutionResponseTime
***************************

**Module**: ``Kernel::System::Stats::Dynamic::TicketSolutionResponseTime``

**What it measures**: Solution and first-response times derived from the ticket's escalation configuration. Both wall-clock ("all over") and working-time variants are available. Only closed tickets are included in the search.

**Evaluation by (mandatory axis)**: The **Evaluation by** attribute must be placed on an axis. It selects which timing metric each cell reports:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Reporting mode
     - Description
   * - Solution Average
     - Mean elapsed time from creation to close across all matching tickets (wall-clock, no escalation config applied).
   * - Solution Min / Max Time
     - Fastest / slowest wall-clock solution time.
   * - Number of Tickets
     - Count of matching tickets (independent of escalation config).
   * - Solution Average *(affected by escalation)*
     - Mean solution time as tracked by the escalation clock — starts/stops per the SLA escalation window.
   * - Solution Min / Max Time *(affected by escalation)*
     - Fastest / slowest escalation-clock solution time.
   * - Solution Working Time Average *(affected by escalation)*
     - Mean working-time solution time, calendar-aware.
   * - Solution Min / Max Working Time *(affected by escalation)*
     - Fastest / slowest working-time solution time.
   * - First Response Average *(affected by escalation)*
     - Mean time from ticket creation to first agent response, per escalation clock.
   * - First Response Min / Max Time *(affected by escalation)*
     - Fastest / slowest first-response time.
   * - First Response Working Time Average *(affected by escalation)*
     - Calendar-aware first-response average.
   * - First Response Min / Max Working Time *(affected by escalation)*
     - Fastest / slowest calendar-aware first-response time.

The "affected by escalation configuration" modes use the ``FirstResponseInMin`` and ``SolutionInMin`` fields stored on the ticket, which are calculated by the escalation engine at close time according to the SLA or queue escalation settings. If no escalation is configured for a ticket, those fields are ``0`` and the ticket contributes a zero value to the average.

**Additional attributes**: Queue, State, Priority, Service, SLA, Type, Create Time, Close Time, Escalation times (First Response Time, Update Time, Solution Time), Dynamic Fields.

----

.. _stats-module-ticketlist:

TicketList
***********

**Module**: ``Kernel::System::Stats::Dynamic::TicketList``

**Type**: **List statistic** — produces a flat table of individual ticket rows rather than an aggregated matrix. Each row is one ticket; each column is a ticket attribute you choose. There are no X-axis or Y-axis concepts; the output is controlled through layout attributes instead.

**Layout attributes** (required):

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Attribute
     - Description
   * - Attributes to be printed
     - Selects which ticket fields appear as columns (Ticket Number, Title, Queue, State, Priority, Owner, Create Time, Close Time, and others). Multiple columns can be selected.
   * - Order by
     - The field used to sort the output rows.
   * - Sort sequence
     - Ascending or descending.
   * - Limit
     - Maximum number of rows returned.

**Filter attributes**: Queue, State, State Type, Priority, Lock, From/To/Cc/Subject/Body, Create Time, Last Changed Time, Change Time, Pending Until Time, Close Time, Historic Time Range, Escalation times, Service, SLA, Type, Agent/Owner (when enabled), Customer ID, Dynamic Fields.

**Unique attributes**:

* **State Historic / State Type Historic**: Filter tickets by the state they were in at a specific point in the past, not their current state. Used together with **Historic Time Range** to snapshot the queue at a given date.
* **Historic Time Range**: Defines the point-in-time for historic state queries.
* **CustomerID (complex search)** and **CustomerID (exact match)**: Two variants of customer filtering — complex allows wildcard matching; exact match requires a full ID.

----

.. _stats-module-configitem:

ITSMConfigItem
***************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMConfigItem``

**Installed by**: ``ITSMConfigurationManagement``

**What it counts**: The number of config items returned by ``ConfigItemSearchExtended`` that match all configured axis and filter values.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - Class
     - ✓
     - ✓
     - ✓
     - CI classes from ``ITSM::ConfigItem::Class`` in the General Catalog (Computer, Hardware, Location, Network, Software by default).
   * - Deployment State
     - ✓
     - ✓
     - ✓
     - Values from ``ITSM::ConfigItem::DeploymentState`` (Production, Pre-Production, Repair, Retired).
   * - Incident State
     - ✓
     - ✓
     - ✓
     - Values from ``ITSM::Core::IncidentState`` (Incident, Operational, Warning).
   * - Create Time
     - ✓
     - ✓
     - ✓
     - Filters by the date the CI record was created.
   * - Change Time
     - ✓
     - ✓
     - ✓
     - Filters by the date any attribute of the CI was last modified.
   * - Number
     - —
     - —
     - ✓
     - CI number text match.
   * - Name
     - —
     - —
     - ✓
     - CI name text match.
   * - Class-specific XML fields
     - ✓ *
     - ✓ *
     - ✓
     - Each CI class definition exposes its searchable attributes (e.g. CPU, RAM, Vendor for the Computer class). These appear as ``ClassName::FieldName`` in the attribute list. **When any XML attribute is used on an axis, a Class must also be selected on at least one axis.**

----

.. _stats-module-flsr:

ITSMTicketFirstLevelSolutionRate
*********************************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMTicketFirstLevelSolutionRate``

**Installed by**: ``ITSMIncidentProblemManagement``

**What it counts**: Tickets that pass a ``TicketSearch`` with the configured filters AND pass the article-structure check for first-level resolution. The cell value is a raw count, not a percentage.

The first-level resolution check examines the customer-visible article list for each matching ticket. A ticket counts as first-level resolved when it has at most two customer-visible articles following one of these patterns:

* **Single article, not from system** — the ticket was resolved with no agent reply required.
* **Two articles — customer then agent** — the customer reported, the agent responded once, and the ticket was closed with no follow-up.

Any ticket with three or more customer-visible articles, a customer follow-up before close, or no articles at all does not count.

**Available attributes**: Identical to the :ref:`TicketAccumulation module <stats-module-ticketaccumulation>` — Type, Service, SLA, Queue, State, Priority, Create Time, Dynamic Fields, etc. The State list is pre-filtered to closed states.

**Special behaviours**

* Returns ``0`` (not a dash) when no tickets match, so it appears in summation rows.
* The article-structure check runs in Perl after the database search. On large datasets, query time scales with the total ticket count, not the result count.

----

.. _stats-module-solutiontime:

ITSMTicketSolutionTimeAverage
******************************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMTicketSolutionTimeAverage``

**Installed by**: ``ITSMIncidentProblemManagement``

**What it returns**: A human-readable duration string (e.g. ``2h 30m``) representing the mean working time each ticket spent in an active (viewable) state. This is **not** a number — cells cannot be summed and ``SumRow``/``SumCol`` are always disabled.

**How it calculates**: For each matching ticket the module walks the state history and identifies spans where the ticket was in a viewable (active) state — typically ``new``, ``open``, and ``pending`` states. It sums the working time across those spans using the ticket's SLA calendar (or queue calendar as fallback), then averages over all matching tickets.

**Available attributes**: Identical to the :ref:`TicketAccumulation module <stats-module-ticketaccumulation>`.

**Special behaviours**

* Returns ``-`` (a dash) when no tickets match, and ``ERROR`` if history data is missing.
* Uses the SLA or queue calendar to measure working time — off-hours and weekends are excluded.
* If a ticket has no ``StateUpdate`` or ``NewTicket`` history entry, the module substitutes a fixed 3-minute value.

----

.. _stats-module-changemanagement:

ITSMChangeManagement
*********************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMChangeManagement``

**Installed by**: ``ITSMChangeManagement``

**What it counts**: The number of ITSM changes returned by ``ChangeSearch`` that match the configured axes and filters.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - Change State
     - ✓
     - ✓
     - ✓
     - ITSM change workflow states (approved, canceled, failed, in progress, pending approval, rejected, requested, retracted, successful).
   * - Category
     - ✓
     - ✓
     - ✓
     - Change risk/impact category (1 very low through 5 very high).
   * - Priority
     - ✓
     - ✓
     - ✓
     - Change priority — separate from ticket priority.
   * - Impact
     - ✓
     - ✓
     - ✓
     - Change impact level.
   * - Timeperiod
     - ✓
     - ✓
     - ✓
     - Change creation time (start/stop date).
   * - Dynamic Fields
     - ✓ *
     - ✓ *
     - ✓
     - Change-object dynamic fields that support stats.

----

.. _stats-module-changehistory:

ITSMChangeManagementHistory
*****************************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMChangeManagementHistory``

**Installed by**: ``ITSMChangeManagement``

**What it counts**: The number of **state-transition events** recorded in the change history where the ``ChangeStateID`` changed to the configured target state. This is not the count of changes currently in that state — it is the count of times changes *entered* that state within the time period.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - Change State
     - ✓
     - ✓
     - ✓
     - The state that was transitioned *into*.
   * - Timeperiod
     - ✓
     - ✓
     - ✓
     - The date the state transition was recorded.

**Special behaviour**: A single change can contribute multiple counts if it transitions into the same state more than once within the period. The module counts transition events, not unique changes.

----

.. _stats-module-changesincidents:

ITSMChangeManagementChangesIncidents
**************************************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMChangeManagementChangesIncidents``

**Installed by**: ``ITSMChangeManagement``

**What it counts**: Depends on the Objects axis value for each row. Each row represents either ITSM changes or tickets of a specific type:

* Objects value ``-1`` (Changes): calls ``ChangeSearch`` and returns the count of matching changes.
* Objects value = a ticket TypeID: calls ``TicketSearch`` restricted to that type and returns the ticket count.

A single stat matrix therefore mixes two data sources — the change table and the ticket table — in the same output.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - Objects
     - —
     - ✓
     - —
     - Entity type for each series: one entry for Changes and one per enabled ticket type.
   * - Timeperiod
     - ✓
     - ✓
     - ✓
     - The time window for the count.

----

.. _stats-module-rfcrequester:

ITSMChangeManagementRfcRequester
*********************************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMChangeManagementRfcRequester``

**Installed by**: ``ITSMChangeManagement``

**What it counts**: The number of Request for Change tickets submitted by each requester (agent or customer) within the time period. The ticket types treated as RfCs are controlled by the ``ITSMChange::AddChangeLinkTicketTypes`` SysConfig key.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - Requester
     - ✓
     - ✓
     - ✓
     - Combined list of agents and customer users. Each entry is prefixed ``agent_`` or ``customer_`` followed by the login/ID so agents and customers with the same name can be distinguished.
   * - Timeperiod
     - ✓
     - ✓
     - ✓
     - Ticket creation time window.

----

.. _stats-module-changesperci:

ITSMChangeManagementChangesPerCIClasses
*****************************************

**Module**: ``Kernel::System::Stats::Dynamic::ITSMChangeManagementChangesPerCIClasses``

**Installed by**: ``ITSMChangeManagement``

**What it counts**: The number of ITSM changes (via their work orders) that are linked to at least one config item of the specified class and category. The query joins the ``link_object`` table to find ITSMWorkOrder ↔ ITSMConfigItem links, then applies the CI class and state filters.

**Available attributes**

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 10 40

   * - Attribute
     - X-axis
     - Y-axis
     - Filter
     - Notes
   * - ConfigItem Classes
     - ✓
     - ✓
     - ✓
     - CI class from the General Catalog (Computer, Hardware, Location, Network, Software).
   * - Category
     - ✓
     - ✓
     - ✓
     - Change category (1 very low through 5 very high).
   * - ConfigItem Status
     - —
     - —
     - ✓
     - The incident state of the linked config item (Incident, Operational, Warning). Filter-only.
   * - Timeperiod
     - ✓
     - ✓
     - ✓
     - Change creation time window.

**Special behaviour**: The link is at the **work order** level, not the change level. A change with multiple work orders each linked to different CI classes will be counted once per distinct class. A change with no linked work orders will not appear in this stat.
