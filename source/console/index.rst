.. meta::
   :description: Znuny command-line interface — automate administration and maintenance using bin/znuny.Console.pl commands grouped by admin, development and maintenance tasks.
   :keywords: znuny console, znuny cli, znuny.Console.pl, command line, znuny scripts, console commands

.. _PageNavigation console_index:

Command Line Interface
######################

There are many things solely configurable via the command line. Most tasks require understanding how to remotely log on to the server and move about on the console.

Console Commands
################

Here you find the list of new console commands, added over the releases.

Console commands help automate processes using scripts to manage Znuny, without using a GUI. 

Commands are parameter of the console: 

``bin/znuny.Console.pl <COMMAND>``

Most of the commands take multiple parameters. 

.. note::   We keep adding commands to the documentation with every release. This list can be incomplete. To get an overview of available commands, call ``bin/znuny.Console.pl`` without any parameter as the application user (znuny or otrs).

.. toctree::
   :maxdepth: 2

   admin
   development
   maintenance
