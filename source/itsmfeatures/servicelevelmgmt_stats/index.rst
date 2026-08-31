.. meta::
   :description: ITSM Service Level Management — pre-configured reporting statistics for ITSM operations covering ticket accumulation, first level solution rate, solution time averages, configuration items, and change management.
   :keywords: znuny itsm statistics, service level management, first level solution rate, solution time average, config item stats, change management stats, itsm reports

ITSM Service Level Management
##############################
.. _PageNavigation itsmfeatures_servicelevelmgmt_stats:

The ``ITSMServiceLevelManagement`` package installs a comprehensive set of pre-configured ITSM reporting statistics. SLA management, escalation, and business-hours calendars are features of the base Znuny framework; service criticality, incident impact, and priority derivation are provided by ``ITSMCore``. This package builds on those foundations by delivering 47 ready-to-use statistic templates that report on the SLA, incident, configuration item, and change management data those features produce.

All 47 templates are installed by ``ITSMServiceLevelManagement`` — including those for configuration items and change management. Each stat group depends on a stat Object module provided by a different package; the group only functions when that package is also installed:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Stat group
     - Object module provided by
   * - :ref:`Ticket Accumulation <itsm-stats-ticket>`
     - base Znuny
   * - :ref:`First Level Solution Rate <itsm-stats-flsr>`
     - ``ITSMIncidentProblemManagement``
   * - :ref:`Average Solution Time <itsm-stats-solutiontime>`
     - ``ITSMIncidentProblemManagement``
   * - :ref:`Configuration Items <itsm-stats-configitem>`
     - ``ITSMConfigurationManagement``
   * - :ref:`Change Management <itsm-stats-change>`
     - ``ITSMChangeManagement``

All statistics are dynamic matrix type and ship with the permission group ``stats``. They appear in **Reports → Statistics** once the required packages are installed.

.. note::

   Stat numbers are assigned sequentially at install time as ``StatID + Stats::StatsStartNumber``. The numbers shown in this guide reflect a clean installation with the default start number of 10000. On systems with pre-existing statistics or a custom ``Stats::StatsStartNumber``, the actual numbers will differ. Use **Reports → Statistics** to look up the numbers on your system.

----

.. _itsm-stats-ticket:

Ticket Accumulation Statistics
*******************************

These statistics use the ``Kernel::System::Stats::Dynamic::Ticket`` module — the same module available in the standard statistics module. They count tickets (rows returned from ``TicketSearch``) that match the configured restrictions and display the count in each cell of the result matrix.

**How the calculation works**

Each cell value is a simple count: the number of tickets that match all active filters *and* fall within the specific X-axis and Y-axis combination for that cell. No time weighting or averaging is performed. Summation rows and columns are enabled (``SumRow=1``, ``SumCol=1``), so totals appear along the bottom and right edge of the result table.

When a time-series X-axis is used (``CreateTime`` broken down by ``Day``), each column represents one calendar day and the Y-axis values are drawn as separate data series.

**Stat group overview**

.. list-table::
   :header-rows: 1
   :widths: 10 45 15 20 10

   * - Stat #
     - Title
     - X-Axis
     - Y-Axis (Series)
     - Restriction
   * - 10012
     - Total number of all tickets ever created per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - none
   * - 10013
     - Total number of all tickets ever created per Ticket-Type and State
     - Ticket Type
     - State
     - none
   * - 10014
     - Total number of all tickets ever created per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - none
   * - 10015
     - Total number of all tickets ever created per Ticket-Type and Service
     - Ticket Type
     - Service
     - none
   * - 10016
     - Monthly overview of all tickets created in the last month per Ticket-Type
     - Day of month
     - Ticket Type
     - Created in past month
   * - 10017
     - Monthly overview of all tickets created in the last month per Priority
     - Day of month
     - Priority
     - Created in past month
   * - 10018
     - Monthly overview of all tickets created in the last month per State
     - Day of month
     - State
     - Created in past month
   * - 10019
     - Monthly overview of all tickets created in the last month per Queue
     - Day of month
     - Queue
     - Created in past month
   * - 10020
     - Monthly overview of all tickets created in the last month per Service
     - Day of month
     - Service
     - Created in past month
   * - 10021
     - Number of tickets created in a specific time period per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - Create time period (user-selectable)
   * - 10022
     - Number of tickets created in a specific time period per Ticket-Type and State
     - Ticket Type
     - State
     - Create time period (user-selectable)
   * - 10023
     - Number of tickets created in a specific time period per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - Create time period (user-selectable)
   * - 10024
     - Number of tickets created in a specific time period per Ticket-Type and Service
     - Ticket Type
     - Service
     - Create time period (user-selectable)
   * - 10025
     - Number of currently open tickets per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - State type: open
   * - 10026
     - Number of currently open tickets per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - State type: open
   * - 10027
     - Number of currently open tickets per Ticket-Type and Service
     - Ticket Type
     - Service
     - State type: open

**Stat groups explained**

All-time cross-tabulations
   Cross-tabulate every ticket ever created against Type and a second dimension. Use these for high-level portfolio overviews or when you need totals not bounded by a time window.

Last month daily time series
   Show ticket creation volume per day across the previous calendar month. The X-axis automatically spans the 30 or 31 days of the past month (``TimeRelativeCount=1``, ``TimeRelativeUnit=Month``, ``TimeScaleCount=1``). These are the fastest route to a monthly trend line.

User-selected time period cross-tabulations
   Same shape as the all-time cross-tabulations but the creation time restriction is left open for the user to configure at run time. Use these when you need an ad-hoc period (a financial quarter, a specific incident window, etc.).

Open ticket snapshots
   Restricted to ``StateType = open``, so they reflect the current backlog at the moment the stat is run. There is no time dimension — these are point-in-time counts, not historical trends.

.. note::

   The all-time and time-period stats count tickets by *creation time*. A ticket created in a given period that was subsequently closed still appears in those stats. To count only tickets that are *currently open*, use the open ticket snapshot stats.

----

.. _itsm-stats-configitem:

Configuration Item Statistics
******************************

These statistics use the ``Kernel::System::Stats::Dynamic::ITSMConfigItem`` module to query the CMDB (Configuration Management Database). Each cell value is a count of configuration items matching the axis and restriction criteria.

Summation rows and columns are enabled for all four stats (``SumRow=1``, ``SumCol=1``).

.. list-table::
   :header-rows: 1
   :widths: 10 50 20 20

   * - Stat #
     - Title
     - X-Axis
     - Y-Axis (Series)
   * - 10028
     - Total number of all config items ever created per Class and State
     - CI Class
     - CI State
   * - 10029
     - Monthly overview of all config items created in the last month per Class
     - Day of month
     - CI Class
   * - 10030
     - Monthly overview of all config items created in the last month per State
     - Day of month
     - CI State
   * - 10031
     - Number of config items created in a specific time period per Class and State
     - CI Class
     - CI State

**Stat groups explained**

All-time Class × State matrix
   A complete picture of the CMDB: how many config items of each class exist in each state. Default CI classes include Computer, Hardware, Location, Network, and Software. CI states include Operational, Warning, and Incident. Useful for capacity and availability overviews.

Last month daily time series
   Show how many config items were *created* each day in the previous calendar month, broken down by class or state. Useful for CMDB growth monitoring and detecting onboarding spikes.

User-selected period Class × State matrix
   Same structure as the all-time matrix but filtered to config items created within a user-configurable time period. Use this for period-specific audits or compliance snapshots.

.. note::

   These stats count config items by *creation date*. They do not reflect the current state of items that were created in earlier periods. For a live view of current CMDB contents run the all-time Class × State stat without a time restriction.

----

.. _itsm-stats-flsr:

First Level Solution Rate Statistics
*************************************

These statistics use the ``Kernel::System::Stats::Dynamic::ITSMTicketFirstLevelSolutionRate`` module to report on the ITIL metric **First Level Resolution Rate (FLRR)** — the proportion of incidents resolved at the first level of support (the service desk) without escalation to a higher support tier.

**How the calculation works**

For each ticket that matches the configured axes and restrictions, the module fetches the list of **customer-visible articles** and applies the following rule:

A ticket counts as first-level resolved if it has **at most two customer-visible articles** that follow one of these patterns:

* **Single article, not from system**: The ticket was closed with only one customer-visible article — regardless of whether the sender was an agent or a customer. Covers cases such as an agent creating and immediately resolving a ticket, or a customer submitting a request that is closed without any reply being needed.
* **Two articles — customer then agent**: The first customer-visible article is from a customer, and the second is from an agent. The agent's response resolved the issue in a single reply, with no follow-up from the customer.

A ticket **does not** count as first-level resolved if:

* It has three or more customer-visible articles (any back-and-forth conversation beyond one exchange).
* It has two articles but the second is from the customer (the customer followed up before the ticket was closed).
* The only article is from the ``system`` sender type.
* It has no customer-visible articles at all.

This logic is implemented entirely in the ``GetStatElement`` method of the module. There is no ticket state or dynamic field that flags "first-level resolution" — the criterion is derived purely from the article conversation structure.

**Pre-configured restrictions**

The shipped stats (10032–10041) fix two restrictions:

* **Ticket state**: Restricted to StateIDs 2 and 10 in the default ITSM state configuration, corresponding to the ITSM closed states. These are fixed and cannot be changed at run time.
* **Ticket type (X-axis)**: Fixed to the Incident-family TypeIDs in the default ITSM type configuration. These define which ticket types appear as columns when the stat is run.

If your Znuny installation has a non-standard type or state configuration (e.g. custom states were added before installing the ITSM package), the fixed IDs may not correspond to the expected types and states. In that case, clone the stat and adjust the restrictions before using it for reporting.

Each cell in the result matrix holds the **count** of tickets matching the axis combination that also pass the article-structure check. Summation rows and columns are enabled (``SumRow=1``, ``SumCol=1``).

.. important::

   The stats output raw counts, not percentages. To calculate the actual First Level Resolution Rate (as a percentage), divide the count from these statistics by the total number of closed incident tickets for the same period and axes. The total can be obtained from the equivalent ticket accumulation statistics filtered to the same incident types and closed states.

**Stat group overview**

.. list-table::
   :header-rows: 1
   :widths: 10 45 15 20 10

   * - Stat #
     - Title
     - X-Axis
     - Y-Axis (Series)
     - Time Restriction
   * - 10032
     - First level solution rate for all tickets ever created per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - none (all-time)
   * - 10033
     - First level solution rate for all tickets ever created per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - none (all-time)
   * - 10034
     - First level solution rate for all tickets ever created per Ticket-Type and Service
     - Ticket Type
     - Service
     - none (all-time)
   * - 10035
     - Monthly overview of first level solution rate per Ticket-Type in the last month
     - Day of month
     - Ticket Type
     - Created in past month
   * - 10036
     - Monthly overview of first level solution rate per Priority in the last month
     - Day of month
     - Priority
     - Created in past month
   * - 10037
     - Monthly overview of first level solution rate per Queue in the last month
     - Day of month
     - Queue
     - Created in past month
   * - 10038
     - Monthly overview of first level solution rate per Service in the last month
     - Day of month
     - Service
     - Created in past month
   * - 10039
     - First level solution rate for all tickets created in a specific time period per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - Create time period (user-selectable)
   * - 10040
     - First level solution rate for all tickets created in a specific time period per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - Create time period (user-selectable)
   * - 10041
     - First level solution rate for all tickets created in a specific time period per Ticket-Type and Service
     - Ticket Type
     - Service
     - Create time period (user-selectable)

**Stat groups explained**

All-time cross-tabulations (10032–10034)
   Count all first-level-resolved incidents since the system was set up, broken down by Type × Priority, Queue, or Service. Useful for identifying which service areas or queues handle the highest proportion of first-level resolutions.

Last month daily time series (10035–10038)
   Track the daily volume of first-level resolutions over the previous calendar month. Each series represents one dimension (Ticket Type, Priority, Queue, or Service). Use these to spot day-of-week patterns or drops in first-level performance.

User-selected time period cross-tabulations (10039–10041)
   Cross-tabulate first-level resolutions within a configurable time period by Type and a second dimension. These give the same matrix structure as 10032–10034 but scoped to a user-defined range — useful for ad-hoc period analysis and monthly service reports.

----

.. _itsm-stats-solutiontime:

Average Solution Time Statistics
*********************************

These statistics use the ``Kernel::System::Stats::Dynamic::ITSMTicketSolutionTimeAverage`` module to report the **mean working time spent while the ticket was in an active state**, expressed as a human-readable duration (e.g. ``2h 30m``).

**How the calculation works**

For each matching ticket the module walks the ticket's state history and identifies spans where the ticket was in a **viewable** (active) state — typically ``new``, ``open``, and ``pending`` states. It sums the working time across those spans using the ticket's SLA calendar (or queue calendar as fallback), then averages the result over all matching tickets in the cell.

Key characteristics:

* **Unit**: Human-readable duration string (``Xh Ym``), not a raw number. Cells cannot be summed mathematically.
* **Working time, calendar-aware**: The module uses the SLA or queue calendar attached to the ticket, so weekends and off-hours are excluded from the measurement. A ticket idle over a weekend does not inflate the average.
* **Active-state spans only**: Time spent in closed or removed states is excluded. If a ticket is closed, reopened, and closed again, only the second open span is counted.
* **Restriction — closed states only**: Only tickets currently in a closed state are included in the search. This ensures only completed tickets contribute to the average.
* **No summation**: ``SumRow=0``, ``SumCol=0``. Row and column totals are suppressed because averaging averages is statistically incorrect.
* **No type restriction**: The pre-configured stats do not fix a ticket type. All ticket types with a closed state contribute unless you add a type restriction at run time.

**Stat group overview**

.. list-table::
   :header-rows: 1
   :widths: 10 45 15 20 10

   * - Stat #
     - Title
     - X-Axis
     - Y-Axis (Series)
     - Time Restriction
   * - 10042
     - Average solution time for all tickets ever created per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - none (all-time)
   * - 10043
     - Average solution time for all tickets ever created per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - none (all-time)
   * - 10044
     - Average solution time for all tickets ever created per Ticket-Type and Service
     - Ticket Type
     - Service
     - none (all-time)
   * - 10045
     - Monthly overview of the average solution time per Ticket-Type in the last month
     - Day of month
     - Ticket Type
     - Created in past month
   * - 10046
     - Monthly overview of the average solution time per Priority in the last month
     - Day of month
     - Priority
     - Created in past month
   * - 10047
     - Monthly overview of the average solution time per Queue in the last month
     - Day of month
     - Queue
     - Created in past month
   * - 10048
     - Monthly overview of the average solution time per Service in the last month
     - Day of month
     - Service
     - Created in past month
   * - 10049
     - Average solution time of tickets created in the last month per Ticket-Type and Priority
     - Ticket Type
     - Priority
     - Created in past month
   * - 10050
     - Average solution time of tickets created in the last month per Ticket-Type and Queue
     - Ticket Type
     - Queue
     - Created in past month
   * - 10051
     - Average solution time of tickets created in the last month per Ticket-Type and Service
     - Ticket Type
     - Service
     - Created in past month

**Stat groups explained**

All-time cross-tabulations (10042–10044)
   Show the average solution time across all closed tickets in the system, broken down by Type × Priority, Queue, or Service. Because these span the full history of the system, the values can be heavily influenced by old tickets resolved under different conditions. Use with caution when comparing to current performance.

Last month daily time series (10045–10048)
   Plot the average solution time per day for the previous calendar month, with one series per dimension. Cells for days with no closed tickets are empty. Use these to spot day-of-week trends or sudden spikes in resolution time.

Last month cross-tabulations (10049–10051)
   Average solution time for tickets *created* in the previous calendar month, broken down by Type and a second dimension. These are the most useful stats for month-on-month SLA reporting.

----

.. _itsm-stats-change:

Change Management Statistics
*****************************

These statistics cover the ITSM Change Management process. They use several specialized modules:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Module
     - Purpose
   * - ``ITSMChangeManagement``
     - Count changes by state or category over a time period
   * - ``ITSMChangeManagementHistory``
     - Track state transitions (e.g. rejected, retracted changes)
   * - ``ITSMChangeManagementChangesIncidents``
     - Compare change volume to incident/ticket volume
   * - ``ITSMChangeManagementRfcRequester``
     - Count Request for Change (RfC) tickets per requester
   * - ``ITSMChangeManagementChangesPerCIClasses``
     - Correlate changes with affected CI classes

**How calculations work**

The change management modules query the change management tables rather than the ticket table. Each module counts change records (or related objects) that match the configured axis combinations and restrictions. The default time window is the last calendar month (``TimeRelativeCount=1``, ``TimeRelativeUnit=Month``, ``TimeScaleCount=1``), displayed as a daily time series. Users can adjust the time window at run time. None of the change management stats use summation rows or columns (``SumRow=0``, ``SumCol=0``).

**Stat group overview**

.. list-table::
   :header-rows: 1
   :widths: 10 30 25 25 10

   * - Stat #
     - Title
     - Module
     - Y-Axis (Series)
     - X-Axis
   * - 10052
     - ITSMChange Count Changes
     - ITSMChangeManagement
     - Change State
     - Day of month
   * - 10053
     - ITSMChange Changes per Category
     - ITSMChangeManagement
     - Change Category
     - Day of month
   * - 10054
     - ITSMChange rejected changes
     - ITSMChangeManagementHistory
     - New State = "rejected"
     - Day of month
   * - 10055
     - ITSMChange retracted changes
     - ITSMChangeManagementHistory
     - New State = "retracted"
     - Day of month
   * - 10056
     - Relation Tickets (by types) ↔ Changes
     - ITSMChangeManagementChangesIncidents
     - Object (Changes + Ticket Types)
     - Day of month
   * - 10057
     - RfCs per Requester
     - ITSMChangeManagementRfcRequester
     - Requester
     - Day of month
   * - 10058
     - Changes per config item class
     - ITSMChangeManagementChangesPerCIClasses
     - CI Class
     - Change Category

**Stat groups explained**

10052 — Change count by state
   Plots the daily volume of changes for each change state (approved, canceled, failed, in progress, pending approval, rejected, requested, retracted, successful). Use this to monitor change pipeline health and identify bottlenecks in the approval workflow.

10053 — Change count by category
   Shows daily change volume broken down by risk/impact category (1 very low through 5 very high). Use this to assess the risk profile of the change calendar.

10054–10055 — Rejected and retracted changes
   These use the ``ITSMChangeManagementHistory`` module, which records state-transition events rather than current change state. Stat 10054 counts changes that *entered* the "rejected" state on each day; stat 10055 counts those that entered "retracted". Together they provide a daily view of change attrition during the approval process.

10056 — Changes vs. tickets by type
   Overlays the daily volume of ITSM changes with the volume of tickets of each ITSM type (Incident, Incident::Major, Problem, RfC, ServiceRequest, Unclassified). This correlation stat helps service managers assess whether change activity is driving incident rates.

10057 — RfCs per requester
   Counts the number of Request for Change tickets submitted by each requester over the time period. Useful for identifying high-volume change requesters and ensuring equitable workload distribution.

10058 — Changes per CI class
   Cross-tabulates change categories against the CI classes affected by those changes. Restrictions can be set on CI state (Incident, Operational, Warning). X-axis shows change category (1 very low through 5 very high); Y-axis shows CI class (Computer, Hardware, Location, Network, Software). Use this to identify which infrastructure components are subject to the most high-risk changes.

----

Using These Statistics
**********************

Accessing statistics
====================

Navigate to **Reports → Statistics** in the agent interface. The imported stats are listed in the overview. Click the title or the **Run** icon to execute a stat.

Adjusting axes and filters at run time
======================================

Stats shipped with ``Fixed="1"`` on an axis or restriction cannot have those values changed at run time — the element is shown for reference only. Stats without ``Fixed="1"`` allow the user to add or remove values from the selection before running.

The time restrictions on monthly stats (``TimeRelativeCount=1``, ``TimeRelativeUnit=Month``) automatically calculate the previous calendar month relative to the current date. To report on a different period, edit the stat and change the time restriction type to an absolute date range.

Exporting results
=================

All ITSM statistics support the following output formats:

* **CSV** — comma-separated values, suitable for import into spreadsheet applications
* **Excel** — native Excel format
* **Print** — formatted print view
* **D3::BarChart** — vertical bar chart rendered in the browser
* **D3::LineChart** — line chart rendered in the browser
* **D3::StackedAreaChart** — stacked area chart rendered in the browser

.. seealso::

   **Statistics Object Module Reference** (Annexes) — full attribute tables for every Object module available in the statistic dropdown, including the four base Znuny modules and all ITSM-specific modules. Use this reference when building your own custom statistics.
