.. meta::
   :description: Znuny maintenance console commands — manage cache, sessions, tickets, logs, S/MIME, statistics, and other housekeeping tasks via bin/znuny.Console.pl.
   :keywords: znuny maintenance commands, console maintenance, maint commands, cache delete, session cleanup, ticket index, console reference

.. _PageNavigation console_maintenance:

Console Commands - Maintenance
###############################

+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Command                                      | Version   | Description                                                          |
+==============================================+===========+======================================================================+
| Maint::Cache::Delete                         | pre-Znuny | Delete cache files created by Znuny.                                 |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Calendar::Ticket::Cleanup             | 6.3       | Cleanup obsolete calendar based ticket creation data.                |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Calendar::Ticket::Generate            | 6.3       | Creates calendar based tickets.                                      |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Config::Dump                          | pre-Znuny | Dump configuration settings.                                         |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Config::Rebuild                       | pre-Znuny | Rebuild the system configuration of Znuny.                           |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Config::Sync                          | pre-Znuny | Synchronize system configuration file with the latest deployment in  |
|                                              |           | the database.                                                        |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Daemon::List                          | pre-Znuny | List available daemons.                                              |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Daemon::Summary                       | pre-Znuny | Show a summary of one or all daemon modules.                         |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Database::Check                       | pre-Znuny | Check Znuny database connectivity.                                   |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Database::CKEditorMigration           | 7.2       | Migrates CKEditor content from version 4 to 5.                       |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Database::MySQL::InnoDBMigration      | pre-Znuny | Convert all MySQL database tables to InnoDB.                         |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Database::PasswordCrypt               | pre-Znuny | Make a database password unreadable for inclusion in                 |
|                                              |           | Kernel/Config.pm.                                                    |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Email::MailQueue                      | pre-Znuny | Mail queue management.                                               |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::FormDraft::Delete                     | pre-Znuny | Delete draft entries.                                                |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::GenericAgent::Run                     | pre-Znuny | Run all generic agent jobs from a configuration file.                |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::GenericInterface::DebugLog::Cleanup   | pre-Znuny | Delete Generic Interface debug log entries.                          |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Loader::CacheCleanup                  | pre-Znuny | Cleanup the CSS/JS loader cache.                                     |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Loader::CacheGenerate                 | pre-Znuny | Generate the CSS/JS loader cache.                                    |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Log::Clear                            | pre-Znuny | Clear the Znuny log.                                                 |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Log::CommunicationLog                 | pre-Znuny | Management of communication logs.                                    |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Log::Print                            | pre-Znuny | Print the Znuny log.                                                 |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::ObjectLink::Add                       | 6.1       | Links objects.                                                       |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::ObjectLink::Delete                    | 6.1       | Removes a link between objects.                                      |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::PostMaster::MailAccountFetch          | pre-Znuny | Fetch incoming emails from configured mail accounts.                 |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::PostMaster::Read                      | pre-Znuny | Read incoming email from STDIN.                                      |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::PostMaster::SpoolMailsReprocess       | pre-Znuny | Reprocess mails from spool directory that could not be imported in   |
|                                              |           | the first place.                                                     |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Session::DeleteAll                    | pre-Znuny | Delete all sessions.                                                 |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Session::DeleteExpired                | pre-Znuny | Delete expired sessions.                                             |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Session::DeleteOrphaned               | pre-Znuny | Delete orphaned sessions.                                            |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Session::ListAll                      | pre-Znuny | List all sessions.                                                   |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Session::ListExpired                  | pre-Znuny | List expired sessions.                                               |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Session::ListOrphaned                 | 7.0       | List orphaned sessions.                                              |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SMIME::CustomerCertificate::Fetch     | pre-Znuny | Fetch S/MIME certificates from customer backends.                    |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SMIME::CustomerCertificate::Renew     | pre-Znuny | Renew existing S/MIME certificates from customer backends.           |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SMIME::FetchFromCustomer              | pre-Znuny | Refresh existing keys for new ones from the LDAP.                    |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SMIME::KeysRefresh                    | pre-Znuny | Normalize S/MIME private secrets and rename all certificates to the  |
|                                              |           | correct hash.                                                        |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SMIME::ReindexKeys                    | 6.4       | Reindex S/MIME keys.                                                 |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Stats::Dashboard::Generate            | pre-Znuny | Generate statistics widgets for the dashboard.                       |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Stats::Generate                       | pre-Znuny | Generate (and send, optional) statistics which have been configured  |
|                                              |           | previously in the Znuny statistics module.                           |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SupportBundle::Generate               | pre-Znuny | Generate a support bundle for this system.                           |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::SupportData::CollectAsynchronous      | pre-Znuny | Collect certain support data asynchronously.                         |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::ArchiveCleanup                | pre-Znuny | Delete ticket/article seen flags and ticket watcher entries for      |
|                                              |           | archived tickets.                                                    |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::Delete                        | pre-Znuny | Delete one or more tickets.                                          |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::Dump                          | pre-Znuny | Print a ticket and its articles to the console.                      |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::EscalationCheck               | pre-Znuny | Trigger ticket escalation events and notification events for         |
|                                              |           | escalation.                                                          |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::EscalationIndexRebuild        | pre-Znuny | Completely rebuild the ticket escalation index.                      |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::FulltextIndex                 | pre-Znuny | Flag articles to rebuild the article search index or display the     |
|                                              |           | index status (use --status or --rebuild).                            |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::FulltextIndexRebuildWorker    | pre-Znuny | Rebuild the article search index for needed articles.                |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::InvalidUserCleanup            | pre-Znuny | Delete ticket/article seen flags and watcher entries of users        |
|                                              |           | invalid for more than a month; unlocks tickets by invalid agents     |
|                                              |           | immediately.                                                         |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::PendingCheck                  | pre-Znuny | Process pending tickets past their pending time and send pending     |
|                                              |           | reminders.                                                           |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::QueueIndexCleanup             | pre-Znuny | Cleanup unneeded entries from StaticDB queue index.                  |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::QueueIndexRebuild             | pre-Znuny | Rebuild the ticket index for AgentTicketQueue.                       |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::RestoreFromArchive            | pre-Znuny | Restore non-closed tickets from the ticket archive.                  |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::UnlockAll                     | pre-Znuny | Unlock all tickets by force.                                         |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::UnlockTicket                  | pre-Znuny | Unlock a single ticket by force.                                     |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::UnlockTimeout                 | pre-Znuny | Unlock tickets that are past their unlock timeout.                   |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::Ticket::Unwatch                       | 7.3       | Removes closed tickets from the watched tickets list after a number  |
|                                              |           | of days.                                                             |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
| Maint::WebUploadCache::Cleanup               | pre-Znuny | Cleanup the upload cache.                                            |
+----------------------------------------------+-----------+----------------------------------------------------------------------+
