.. meta::
   :description: Znuny admin console commands — create users, fix frontend files, manage groups, queues and system tasks from bin/znuny.Console.pl without the web UI.
   :keywords: znuny admin commands, znuny.Console.pl, admin console, cli admin, admin scripts, console reference

.. _PageNavigation console_admin:

Console Commands - Admin
########################

The command format is:

bin/znuny.Console.pl <COMMAND> <OPTIONS>

Use the option -h or --help to get more information about a specific command.

+--------------------------------------------------+--------------+--------------------------------------------------------------+
| Command                                          | Versions     | Description                                                  |
+==================================================+==============+==============================================================+
|| Admin::Config::FixMissingFrontendFiles          || 6.1         || Fixes missing JavaScript and CSS configurations between     |
||                                                 ||             || Znuny upgrades.                                             |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
|| Admin::DynamicField::DefaultColumnsScreenConfig || 6.1, 7.0.11 || Adds and removes dynamic fields to/from default column      |
||                                                 ||             || screen configurations.                                      |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
|| Admin::DynamicField::Export                     || 6.1, 7.0.11 || Exports configuration of all dynamic fields. Output can be  |
||                                                 ||             || formatted as YAML or Perl structure.                        |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
|| Admin::DynamicField::Import                     || 7.0.11      || Imports configuration of dynamic fields and dynamic field   |
||                                                 ||             || screens from a file in YAML format.                         |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
| Admin::DynamicField::ScreenConfig                | 6.1, 7.0.11  |                                                              |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
|| Admin::Object::Export                           || 7.2.1       || Exports configuration or data of specified objects. Output  |
||                                                 ||             || can be formatted as YAML or Perl structure.                 |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
|| Admin::PostMasterFilter::Export                 || 6.1         || Exports configuration of all PostMaster filters. Output can |
||                                                 ||             || be formatted as YAML or Perl structure.                     |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
|| Admin::PostMasterFilter::Import                 || 6.1         || Imports configuration of PostMaster filter from a file in   |
||                                                 ||             || YAML format.                                                |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
| Admin::TicketAttributeRelations::Import          | 6.2          | Imports ticket attribute relations from a CSV/Excel file.    |
+--------------------------------------------------+--------------+--------------------------------------------------------------+
