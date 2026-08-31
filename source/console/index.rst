.. meta::
   :description: Znuny command-line interface — automate administration and maintenance using bin/znuny.Console.pl commands grouped by admin, development and maintenance tasks.
   :keywords: znuny console, znuny cli, znuny.Console.pl, command line, znuny scripts, console commands


.. _PageNavigation console_index:

Command Line Interface
######################

There are often technical tasks to be done on a Znuny system that do have a component in the graphical user interface. For these tasks, the administrator will need to have remote shell access to Znuny. Once logged in, the administrator can use the shell to perform various tasks. Znuny provides a command line interface (CLI) to perform many of these tasks. The CLI is implemented as a Perl script called ``otrs.Console.pl``, located in the ``bin`` directory of your Znuny installation. Other tasks or features may have configurations files located in the application directory of your Znuny installation.

Console Commands
****************

Console commands offer the possibility to execute various tasks from the command line. These can be maintenance tasks, administrative tasks, or development tasks. Here you find an overview of all available console commands.

Commands are parameter of the console script:

``bin/znuny.Console.pl <COMMAND>``

A full list of available commands can be obtained by executing the console script with the following command:

``bin/znuny.Console.pl List``

You can search for a specific command by using the ``Search`` command. For example, to search for all commands related to users, you would execute:

``bin/znuny.Console.pl Search User``

Most of the commands take multiple parameters and or arguments. For detailed information on a specific command, please refer to the respective documentation page. All commands have a help option that can be accessed by executing the command with the ``--help`` parameter. For example, to get help on the ``Admin::User::Add`` command, you would execute:

``bin/znuny.Console.pl Admin::User::Add --help``

.. note::   We keep adding commands to the documentation with every release. This list can be incomplete. To get an overview of available commands, call ``bin/otrs.Console.pl List`` without any parameter or arguments as the application user (znuny or otrs).


Advanced Features
*****************
Some tasks or advanced features are not directly related to a specific administration module, and have configurations which need shell access. These features are documented in this section.

.. toctree::
   :maxdepth: 2

   admin
   development
   maintenance
   advanced_stats
