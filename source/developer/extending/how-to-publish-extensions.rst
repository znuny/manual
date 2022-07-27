Publishing Extensions
#####################

Package Management
*******************

The Package Manager is a mechanism to distribute software packages for the framework via HTTP, FTP, or file upload.

For example, the Znuny project maintains the following modules for the community and provides them on an HTTPS-enabled server.

* FAQ	
* Survey	
* SystemMonitoring	
* TimeAccounting

These packages are installable or upgradable over-the-wire by the administrator, using the package manager. For users without a network connection to our servers, the packages are installed and upgraded using the same tool by uploading the file using the package manager or calling it from the command line.


Package Distribution
*********************
      
Adding an online repository to the front-end is as easy as adding the resource to the following setting ``Package::RepositoryList``. In this option, newly selectable repository are enabled in the package manager.

The repository must contain an index file. The package manager then reads this index file and displays available packages.


Generate a package index using the ``Dev::Package::RepositoryIndex`` console command.

.. code-block::

   shell> bin/otrs.Console.pl Dev::Package::RepositoryIndex /path/to/repository/ > /path/to/repository/repo_name.xml
                        
.. note:: 
   
   Details about the package and available options from the source files (SOPM) generate index details. See


Package Commands
****************
      
Commands for maintaining packages are available as modules of ``bin/otrs.Console.pl``.

Using the command line, you can install or upgrade a package locally or from a remote resource.

.. note::
   
   Use this format instead of the local path for installation or upgrading modules from remote repositories ``https://host.example.org/path/to/:package.opm``.

Important Commands
===================

**Installing packages**

.. code::

   shell> bin/otrsConsole.pl Admin::Package::Install /path/to/package.opm

**Uninstall packages**

.. code::

   shell> bin/otrsConsole.pl Admin::Package::Uninstall /path/to/package.opm

**Upgrade packages**

.. code::

   shell> bin/otrsConsole.pl Admin::Package::Upgrade /path/to/package.opm

**List packages**

.. code::
   
   shell> bin/otrsConsole.pl Admin::Package::List


Full Command Listing
=====================

.. note:: 
   
   Use ``bun/otrs.Console.pl <COMMAND> --help`` for all usage options.


+------------------------------------+--------------------------------------------------------------+
| Name                               | Description                                                  |
+====================================+==============================================================+
| Admin::Package::Export             | Export the contents of an OTRS package to a directory.       |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::FileSearch         | Find a file in an installed OTRS package.                    |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::Install            | Install an OTRS package.                                     |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::List               | List all installed OTRS packages.                            |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::ListInstalledFiles | List all installed OTRS package files.                       |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::Reinstall          | Reinstall an OTRS package.                                   |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::ReinstallAll       | Reinstall all OTRS packages that are not correctly deployed. |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::RepositoryList     | List all known OTRS package repsitories.                     |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::Uninstall          | Uninstall an OTRS package.                                   |
+------------------------------------+--------------------------------------------------------------+
| Admin::Package::Upgrade            | Upgrade an OTRS package.                                     |
+------------------------------------+--------------------------------------------------------------+
