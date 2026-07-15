.. meta::
   :description: Znuny developer console commands — generate unit tests, scaffold packages, run translation updates, cache benchmarks, and other developer tooling via bin/znuny.Console.pl.
   :keywords: znuny developer commands, znuny cli development, unit test ticket, developer console, dev commands, znuny.Console.pl dev, package build, translations update

.. _PageNavigation console_development:

Console Commands - Developer
############################

+------------------------------------------+-----------+----------------------------------------------------------------------+
| Command                                  | Version   | Description                                                          |
+==========================================+===========+======================================================================+
| Dev::Code::ContributorsListUpdate        | pre-Znuny | Update the list of contributors based on git commit information.     |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Code::CPANAudit                     | pre-Znuny | Scan CPAN dependencies in Kernel/cpan-lib and in the system for      |
|                                          |           | known vulnerabilities.                                               |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Code::CPANUpdate                    | pre-Znuny | Update dependencies in Kernel/cpan-lib.                              |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Code::Generate::ConsoleCommand      | pre-Znuny | Generate a console command skeleton.                                 |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Code::Generate::UnitTest::Backend   | pre-Znuny | Generate a unit test skeleton.                                       |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Package::Build                      | pre-Znuny | Create a package (opm) file from a package source (sopm) file.       |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Package::RepositoryIndex            | pre-Znuny | Generate an index file (otrs.xml) for a package repository.          |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::CacheBenchmark               | pre-Znuny | Run a benchmark over the available cache backends.                   |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::Config2Docbook               | pre-Znuny | Generate a config options reference chapter (docbook) for the        |
|                                          |           | administration manual.                                               |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::ConsoleStats                 | pre-Znuny | Print some statistics about available console commands.              |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::Database::RandomDataInsert   | pre-Znuny | Insert random data into the database for testing purposes.           |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::Database::XML2SQL            | pre-Znuny | Convert database XML to SQL.                                         |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::Database::XMLExecute         | pre-Znuny | Convert a database XML file to SQL and execute it in the current     |
|                                          |           | database.                                                            |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::GenericInterface::DebugRead  | pre-Znuny | Read parts of the generic interface debug log based on your given    |
|                                          |           | options.                                                             |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::ImportFakeEmails             | pre-Znuny | Insert fake emails/tickets to the system.                            |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::RPMSpecGenerate              | pre-Znuny | Generate RPM spec files.                                             |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::Shell                        | pre-Znuny | An interactive REPL shell for the Znuny API.                         |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::TestEmails                   | pre-Znuny | Get emails from test backend and output them to screen.              |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::Tools::TranslationsUpdate           | pre-Znuny | Update the Znuny translation files.                                  |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::UnitTest::Run                       | pre-Znuny | Execute unit tests.                                                  |
+------------------------------------------+-----------+----------------------------------------------------------------------+
| Dev::UnitTest::TicketToUnitTest          | 6.1       | Creates a unit test of a ticket.                                     |
+------------------------------------------+-----------+----------------------------------------------------------------------+
