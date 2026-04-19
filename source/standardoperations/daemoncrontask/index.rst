.. meta::
   :description: Manage Znuny daemon cron tasks — view, edit and schedule the background jobs that run SchedulerCronTaskManager, add custom tasks and tune execution cadence.
   :keywords: znuny daemon cron, schedulercrontaskmanager, cron scheduler, background jobs, scheduled tasks, daemon task

Cron Scheduler Task Management
##############################

Manage and monitor cron scheduler tasks in Znuny. These system configurations allows you to view, edit, and control the execution of scheduled tasks that are essential for the smooth operation of your system. Although most tasks are scheduled at a recommended time, you can adjust the schedule to better fit your needs. This section provides an overview of how to manage these tasks effectively. Additionally, you can add some of your own tasks to the scheduler, which can be useful for automating custom processes. For more information on how to add your own tasks, please refer to the documentation on adding custom cron tasks.

Below is a **user/admin documentation** for the shown `Daemon::SchedulerCronTaskManager::Task` settings (Znuny/OTRS-style). It’s written so you can paste it into your internal wiki/runbook.


Daemon Scheduler Cron Task Manager – Task Settings
**************************************************

These settings define **scheduled background jobs** executed by the Znuny/OTRS **Daemon Scheduler** via the `SchedulerCronTaskManager`. Each task entry controls:

* **What** is executed (Perl module + function)
* **How** it is executed (params)
* **When** it runs (cron-like schedule)
* **How many** may run in parallel

Setting structure
*****************

Each task is configured in the following fashion:

* `Module`: Perl module that provides the executable entry point.
* `Function`: Method name called on that module (often `Execute` for console commands).
* `Params`: Array of CLI-like arguments passed to the command (console commands).
* `Schedule`: Cron expression (`min hour dom month dow`). If omitted, the task may be triggered differently (depends on core defaults / manager logic).
* `MaximumParallelInstances`: How many instances of this task may run concurrently (usually `1` to avoid overlaps).


Default Active Tasks
********************

ArticleSearchIndexRebuild
=========================

**Purpose:** Rebuilds the **ticket/article fulltext search index** (worker-based).

* **Module:** `Kernel::System::Console::Command::Maint::Ticket::FulltextIndexRebuildWorker`
* **Function:** `Execute`
* **Params:** `--children …` (spawns worker children for parallel processing)
* **Params:** `4` (number of worker children, depends on system resources)
* **Params:** `--limit …` (limit number of tickets per worker, depends on ticket volume)
* **Params:** '20000' (number of tickets per worker, adjust based on performance
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Typically used after upgrades, search backend changes, or corrupted/empty index.
* Can be heavy on CPU/IO depending on ticket volume.
* Ensure it doesn’t overlap with other index-related jobs.


CalendarTicketCreate
====================

**Purpose:** Generates tickets from calendar entries (calendar → ticket automation).

* **Module:** `Kernel::System::Console::Command::Maint::Calendar::Ticket::Generate`
* **Function:** `Execute`
* **Schedule:** `*/2 * * * *` (every 2 minutes)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* High frequency means: calendar-based triggers are near real-time.
* If this job stalls, calendar-driven ticket creation will lag.


CalendarTicketCreateCleanup
===========================

**Purpose:** Cleans up calendar ticket generation artifacts (old entries / locks / processed markers depending on implementation).

* **Module:** `Kernel::System::Console::Command::Maint::Calendar::Ticket::Cleanup`
* **Function:** `Execute`
* **Schedule:** `0 2 * * *` (daily at 02:00)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Run during low-traffic hours.
* If disabled, the system may accumulate stale calendar processing data.


CommunicationLogDelete
======================

**Purpose:** Purges the communication log (mail, channels, outbound/inbound tracking), based on retention rules.

* **Module:** `Kernel::System::Console::Command::Maint::Log::CommunicationLog`
* **Function:** `Execute`
* **Params:** `--purge` (trigger purge mode)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Helps control database size.
* Retention behavior depends on additional parameters not shown in the snippet (often “days” or “created-before”).


ConfigurationDeploymentCleanup
==============================

**Purpose:** Cleans up old SysConfig deployment data (historical deployments, temporary artifacts).

* **Module:** `Kernel::System::SysConfig`
* **Function:** `ConfigurationDeployCleanup`
* **Schedule:** `40 0 * * 0` (Sundays at 00:40)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Keeps configuration deployment storage lean.
* Good to run weekly.
* Truncates all but twenty of the last deployments (default behavior non-configurable).


CoreCacheCleanup
================

**Purpose:** Purges expired entries from the core cache backend.

* **Module:** `Kernel::System::Cache`
* **Function:** `CleanUp`
* **Params:** `Expired` (cleanup mode)
* **Params:** `1` (only expired entries)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* If cache cleanup never runs, you may see increased disk/memory usage (depends on cache backend).


DeleteOrphanedSessions
======================

**Purpose:** Removes session records that are orphaned (e.g., incomplete/invalid session state).

* **Module:** `Kernel::System::Console::Command::Maint::Session::DeleteOrphaned`
* **Function:** `Execute`
* **Schedule:** `58 * * * *` (hourly at minute 58)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Helps keep the session table clean and improves performance.


EscalationCheck
===============

**Purpose:** Performs escalation processing (SLA timers, escalation updates, escalation events).

* **Module:** `Kernel::System::Console::Command::Maint::Ticket::EscalationCheck`
* **Function:** `Execute`
* **Schedule:** `*/5 * * * *` (every 5 minutes)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* If this task stops, escalations and SLA-related behaviors become unreliable.
* Typical monitoring target.


GenerateDashboardStats
======================

**Purpose:** Pre-computes dashboard statistics for faster dashboard rendering.

* **Module:** `Kernel::System::Console::Command::Maint::Stats::Dashboard::Generate`
* **Function:** `Execute`
* **Schedule:** `5 * * * *` (hourly at minute 5)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Keeps dashboards fast and consistent.
* If disabled, dashboards may calculate live (slower) depending on config.


GenericInterfaceDebugLogCleanup
===============================

**Purpose:** Cleans up GenericInterface debug logs (web service request/response debug data).

* **Module:** `Kernel::System::Console::Command::Maint::GenericInterface::DebugLog::Cleanup`
* **Function:** `Execute`
* **Params:** `--created-before-days …` (retention window)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Important if debug logging is enabled in production (logs can grow fast).
* Ensure retention fits compliance/audit requirements.


LoaderCacheDelete
=================

**Purpose:** Clears loader cache (compiled/aggregated frontend assets/caches).

* **Module:** `Kernel::System::Loader`
* **Function:** `CacheDelete`
* **Schedule:** `30 0 * * 0` (Sundays at 00:30)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Helps if asset cache grows or after certain changes.
* Might cause slight performance dip on next requests while cache warms.


MailAccountFetch
================

**Purpose:** Fetches mail from configured inbound mail accounts (PostMaster).

* **Module:** `Kernel::System::Console::Command::Maint::PostMaster::MailAccountFetch`
* **Function:** `Execute`
* **Schedule:** `*/10 * * * *` (every 10 minutes)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Controls inbound email latency.
* Too frequent can stress mail servers; too infrequent delays ticket creation.


MailQueueSend
=============

**Purpose:** Sends queued outbound emails (mail queue).

* **Module:** `Kernel::System::Console::Command::Maint::Email::MailQueue`
* **Function:** `Execute`
* **Params:** `--send …`
* **MaximumParallelInstances:** `1`

**Operational notes:**

* If this fails, outbound notifications will pile up.
* Usually paired with monitoring of mail queue size.


ReindexSMIMECertificates
========================

**Purpose:** Reindexes S/MIME keys/certificates for lookup/validation.

* **Module:** `Kernel::System::Console::Command::Maint::SMIME::ReindexKeys`
* **Function:** `Execute`
* **Params:** `all …` (reindex all keys)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Useful after importing keys/certs or changing key storage.


RenewCustomerSMIMECertificates
==============================

**Purpose:** Renews customer S/MIME certificates (automation).

* **Module:** `Kernel::System::Console::Command::Maint::SMIME::CustomerCertificate::Renew`
* **Function:** `Execute`
* **Schedule:** `02 02 * * *` (daily at 02:02)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Ensures customer certs remain valid (depends on how renewals are managed in your environment).


SessionDeleteExpired
====================

**Purpose:** Deletes expired sessions (regular session retention cleanup).

* **Module:** `Kernel::System::Console::Command::Maint::Session::DeleteExpired`
* **Function:** `Execute`
* **Schedule:** `55 */2 * * *` (every 2 hours at minute 55)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Keeps session table small.
* Frequency can be tuned if you have very high login traffic.


SpoolMailsReprocess
===================

**Purpose:** Reprocesses mail spool (failed/deferred inbound messages).

* **Module:** `Kernel::System::Console::Command::Maint::PostMaster::SpoolMailsReprocess`
* **Function:** `Execute`
* **Schedule:** `10 0 * * *` (daily at 00:10)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Important safety net if inbound processing failed earlier.
* Investigate repeated spool growth (root cause is usually parsing, permissions, or connectivity).


SupportDataCollectAsynchronous
==============================

**Purpose:** Collects support data asynchronously (system diagnostics/support bundle data).

* **Module:** `Kernel::System::Console::Command::Maint::SupportData::CollectAsynchronous`
* **Function:** `Execute`
* **Schedule:** `1 * * * *` (hourly at minute 1)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Helps keep Support Data current without interactive waiting.


TicketAcceleratorRebuild
========================

**Purpose:** Rebuilds ticket accelerator data (performance-related cache/index structures).

* **Module:** `Kernel::System::Ticket`
* **Function:** `TicketAcceleratorRebuild`
* **Schedule:** `01 01 * * *` (daily at 01:01)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Useful for performance and consistency depending on accelerator type.


TicketDraftDeleteExpired
========================

**Purpose:** Deletes expired form drafts (Agent draft data).

* **Module:** `Kernel::System::Console::Command::Maint::FormDraft::Delete`
* **Function:** `Execute`
* **Params:** `--object-type …` (what kind of drafts to delete, depends on full params)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Prevents draft storage bloat.


TicketNumberCounterCleanup
==========================

**Purpose:** Cleans up ticket number auto-increment counter artifacts.

* **Module:** `Kernel::System::Ticket::Number::AutoIncrement`
* **Function:** `TicketNumberCounterCleanup`
* **Schedule:** `*/10 * * * *` (every 10 minutes)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Supports integrity/cleanup of auto-increment ticket number generation.


TicketPendingCheck
==================

**Purpose:** Checks pending tickets and triggers pending-related transitions/actions.

* **Module:** `Kernel::System::Console::Command::Maint::Ticket::PendingCheck`
* **Function:** `Execute`
* **Schedule:** `45 */2 * * *` (every 2 hours at minute 45)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* If stopped, pending-to-open transitions and pending events may not fire on time.


TicketUnlockTimeout
===================

**Purpose:** Unlocks tickets after lock timeout (prevents stale locks).

* **Module:** `Kernel::System::Console::Command::Maint::Ticket::UnlockTimeout`
* **Function:** `Execute`
* **Schedule:** `35 * * * *` (hourly at minute 35)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Critical in environments where agents forget locked tickets.


WebUploadCacheCleanup
=====================

**Purpose:** Cleans upload cache (temporary files during web uploads/forms).

* **Module:** `Kernel::System::Web::UploadCache`
* **Function:** `FormIDCleanUp`
* **Schedule:** `46 * * * *` (hourly at minute 46)
* **MaximumParallelInstances:** `1`

**Operational notes:**

* Prevents disk usage growth in upload temp directories.


Common troubleshooting
======================

**Task not running**

1. Check daemon status (systemd service) and logs.
2. Check task definition syntax (Perl config compile errors stop loading).
3. Verify cron `Schedule` is valid (5 fields).
4. Ensure `MaximumParallelInstances` isn’t blocking due to a stuck run.

**Tasks overlapping / stuck**

* If a task runtime exceeds its interval, set a less frequent schedule or fix performance.
* Compare process tree and process table to identify stuck instances. Most commands should have a --force-pid option to kill stuck runs.

**High database growth**

* Focus on: `CommunicationLogDelete`, session cleanup tasks, upload cache cleanup, debug log cleanup.

Task Overview
=============

+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| Task Name                       | Purpose                                  | Schedule                | Criticality | Impact if Disabled                        |
+=================================+==========================================+=========================+=============+===========================================+
| ArticleSearchIndexRebuild       | Rebuilds fulltext search index           | (manual / worker-based) | Medium      | Search results incomplete or outdated     |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
|| CalendarTicketCreate           || Generates tickets from calendar entries || ``*/2 * * * *``        || Medium     || Calendar-triggered tickets delayed/not   |
||                                ||                                         ||                        ||            || created                                  |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| CalendarTicketCreateCleanup     | Cleans calendar processing data          | ``0 2 * * *``           | Low         | Old calendar artifacts accumulate         |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| CommunicationLogDelete          | Purges communication logs                | (configured via params) | Medium      | DB growth, larger communication_log table |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| ConfigurationDeploymentCleanup  | Cleans old SysConfig deployment data     | ``40 0 * * 0``          | Low         | Deployment history accumulates            |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| CoreCacheCleanup                | Removes expired cache entries            | (no schedule shown)     | Medium      | Increased memory/disk usage               |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| DeleteOrphanedSessions          | Removes broken session entries           | ``58 * * * *``          | Medium      | Session table grows unnecessarily         |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| EscalationCheck                 | Processes SLA escalations                | ``*/5 * * * *``         | High        | SLAs/escalations stop triggering          |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| GenerateDashboardStats          | Precomputes dashboard statistics         | ``5 * * * *``           | Low–Medium  | Dashboards slower / calculated live       |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| GenericInterfaceDebugLogCleanup | Cleans web service debug logs            | (configured via params) | Medium      | GI debug logs grow rapidly                |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| LoaderCacheDelete               | Clears frontend loader cache             | ``30 0 * * 0``          | Low         | Frontend cache may grow / stale assets    |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| MailAccountFetch                | Fetches inbound emails                   | ``*/10 * * * *``        | High        | Emails not converted to tickets           |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| MailQueueSend                   | Sends queued outbound emails             | (configured via params) | High        | Notifications pile up                     |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| ReindexSMIMECertificates        | Reindexes S/MIME keys                    | (no schedule shown)     | Low         | Certificate lookup inconsistencies        |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| RenewCustomerSMIMECertificates  | Renews customer certificates             | ``02 02 * * *``         | Medium      | Expired S/MIME certs                      |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| SessionDeleteExpired            | Deletes expired sessions                 | ``55 */2 * * *``        | Medium      | Session table growth                      |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| SpoolMailsReprocess             | Reprocesses failed inbound mail          | ``10 0 * * *``          | Medium      | Spool accumulates                         |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| SupportDataCollectAsynchronous  | Collects support diagnostics             | ``1 * * * *``           | Low         | Support data outdated                     |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| TicketAcceleratorRebuild        | Rebuilds ticket accelerator structures   | ``01 01 * * *``         | Medium      | Slower ticket performance                 |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| TicketDraftDeleteExpired        | Deletes expired drafts                   | (configured via params) | Low         | Draft storage grows                       |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| TicketNumberCounterCleanup      | Cleans ticket number counter data        | ``*/10 * * * *``        | Medium      | Counter inconsistencies over time         |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| TicketPendingCheck              | Processes pending tickets                | ``45 */2 * * *``        | High        | Pending → open transitions fail           |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| TicketUnlockTimeout             | Unlocks stale ticket locks               | ``35 * * * *``          | High        | Tickets remain locked                     |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+
| WebUploadCacheCleanup           | Cleans temporary upload cache            | ``46 * * * *``          | Medium      | Disk space consumption increases          |
+---------------------------------+------------------------------------------+-------------------------+-------------+-------------------------------------------+

Optional Tasks
**************


These tasks are shipped but **not active by default**. They serve one of the following purposes:

1. Legacy mail fetching
2. Custom scheduler extension points
3. File-based GenericAgent execution
4. Optional housekeeping (watch cleanup)

Legacy Mail Fetching (FetchMail)
================================

**Purpose**

Provides internal fetchmail-based email retrieval instead of the modern `MailAccountFetch` console command.

+--------------+----------------+----------------------------+--------------------------+
| Setting      | Schedule       | Module                     | Notes                    |
+==============+================+============================+==========================+
| FetchMail    | ``*/5 * * * *``| Kernel::System::FetchMail  | Standard fetchmail       |
+--------------+----------------+----------------------------+--------------------------+
| FetchMailSSL | ``*/5 * * * *``| Kernel::System::FetchMail  | Same module, SSL variant |
+--------------+----------------+----------------------------+--------------------------+

**Generalized Behavior**

* Runs every 5 minutes (default)
* Uses legacy FetchMail module
* Modern Znuny installations typically use:

.. code-block:: shell
    
    Maint::PostMaster::MailAccountFetch

* Usually unnecessary unless explicitly required

**Recommendation**

Keep disabled unless:

* Using system-level fetchmail integration
* Running legacy mail infrastructure


TicketWatchRemoveClosed
========================

**Purpose**

Remove closed tickets from agents’ watch lists.

**Default Configuration**

* **Module:** `Kernel::System::Console::Command::Maint::Ticket::Unwatch`
* **Function:** `Execute`
* **Schedule:** `46 * * * *` (hourly at minute 46)
* **Params:** `--days`
* **Params:** `7` (remove watches closed for more than 7 days)
* **MaximumParallelInstances:** `1`

**Behavior**

* Runs daily at 02:00
* Cleans up outdated watch entries
* Prevents stale watched ticket references

**Recommendation**

Optional but useful in environments where:

* Agents heavily use ticket watching
* Large ticket volumes accumulate closed watches


Custom Task Slots (Custom1–Custom9)
***********************************

*Purpose*

Predefined scheduler extension slots for executing custom modules or console commands.

**Default Configuration**

.. code-block:: shell

    Schedule: * * * * *
    Module: (empty)
    Function: (required if Module is defined)

**Behavior**

* Executes every minute if activated
* Does nothing by default (Module not defined)
* Can execute:

  * Console commands
  * Kernel modules
  * Custom logic

### Usage Pattern

Typical configuration example:

.. code-block:: yaml

    Module: Kernel::System::Console::Command::My::CustomCommand
    Function: Execute
    Schedule: 0 * * * *
    MaximumParallelInstances: 1

**Recommendation**

Keep disabled until:

* Custom automation is required
* You need scheduler-driven integrations
* You want lightweight background jobs without system cron

Use-Case Example:
=================

.. code-block:: yaml

    TaskName: Send Report 10001
    Function: Execute
    Module: Kernel::System::Console::Command::Maint::Stats::Generate
    MaximumParallelInstances: 1
    Schedule: 30 6 * * *
    Params:
      - --number
      - 10001
      - --format
      - Excel
      - --mail-recipient
      - max.mustermann@example.com
      - --mail-recipient
      - maria.muller@example.com
      - --mail-body
      - TestReport
      - --mail-sender
      - sender@example.com

File-Based GenericAgent Slots (GenericAgentFile1–5)
***************************************************

**Purpose**

Execute file-based GenericAgent configurations.

**Default Schedule**

```
*/20 * * * *
```
**Sample task for sending a statistics report via email:**

.. code-block:: yaml

    TaskName: Custom1
    Function: Execute
    Module: Kernel::System::Console::Command::Maint::Stats::Generate
    MaximumParallelInstances: 1
    Schedule: 30 6 * * *
    Params:
      - --number
      - 10001
      - --format
      - Excel
      - --mail-recipient
      - max.mustermann@example.com
      - --mail-recipient
      - maria.muller@example.com
      - --mail-body
      - TestReport
      - --mail-sender
      - sender@example.com

**Notes**

* Intended for file-based GenericAgent jobs
* Requires console command usage
* Module must be specified via the `--configuration-module` parameter
* PID handling managed via console wrapper

**Modern Context**

Most installations:

* Use DB-based GenericAgent configuration
* Rely on internal daemon jobs

File-based GA is legacy-oriented, or for self-programmed modules.

**Recommendation**

Enable only if:

* You maintain file-based GA definitions
* You run external deployment of GA configs

Consolidated Overview
=====================

| Category                | Tasks                   | Default Status | Typical Need          |
| ----------------------- | ----------------------- | -------------- | --------------------- |
| Legacy Mail Fetch       | FetchMail, FetchMailSSL | Disabled       | Rare / Legacy only    |
| Custom Scheduler Slots  | Custom1–9               | Disabled       | Advanced automation   |
| File-Based GenericAgent | GenericAgentFile1–5     | Disabled       | Legacy GA deployments |
| Watch Cleanup           | TicketWatchRemoveClosed | Disabled       | Medium-volume systems |

Architectural Interpretation
============================

These tasks represent:

* Backward compatibility mechanisms
* Extension hooks
* Deployment-time flexibility
* Optional housekeeping

They are intentionally disabled to:

* Reduce resource usage
* Avoid duplicate mail processing
* Prevent accidental execution of empty custom slots
* Encourage console-based modern maintenance commands
