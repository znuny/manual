.. _PackageBuilding PageNavigation:

Packaging Code
##############
.. _PackageBuilding PackagingCode:

To distribute your modules, the changes must first be packaged in the ``.opm`` format before it can be listed in a repository or installed.

.. note:: 
   
   An exception is during development when using the :ref:`module tools <DeveolperEnvironment ModuleTools>`. 


A specification file or ``.sopm``  is the basis for compiling a package from your source directory. This includes the properties, restrictions, and files of the module.

Package Specification File
***************************

Packages are simply XML files with encoded instructions, as are the specification files. Create or edit your ``.sopm`` in the editor of choice. The package metadata, list of files, and the database options are just a few things described by the SOPM.

Element List
=============

+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| XML Element           | Example                                                                                                                   | Description                                                                                                                                                                                             | Required |
+=======================+===========================================================================================================================+=========================================================================================================================================================================================================+==========+
| Name                  | Calendar                                                                                                                  | Name of package                                                                                                                                                                                         | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Version               | 1.2.3                                                                                                                     | Version of Package                                                                                                                                                                                      | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Framework             | 6.2.x                                                                                                                     | Version of Framework. This tag can be used multiple times and dictates the minimum framework level.                                                                                                     | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| Vendor                | Znuny GmbH                                                                                                                | Name of Vendor                                                                                                                                                                                          | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| URL                   | https://www.znuny.com                                                                                                     | Vendor URL                                                                                                                                                                                              | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| License               | GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007                                                                        | The license of the package.                                                                                                                                                                             | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|| ChangeLog            || Added some feature.                                                                                                      || The package change log (optional). The tag requires a version and date attribute. Can be used multiple times.                                                                                          || No      |
||                      ||                                                                                                                          || ``<ChangeLog Version="1.1.1" Date="2013-02-15 16:17:51">New package.</ChangeLog>``                                                                                                                     ||         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|| Description          || A web calendar.                                                                                                          || The sort description of the package. Can be used multiple times for packages in different languages.                                                                                                   || Yes     |
||                      ||                                                                                                                          || ``<Description Lang="de">Ein Web Kalender.</Description>``                                                                                                                                             ||         |
||                      ||                                                                                                                          || ``<Description Lang="en">A web calendar.</Description>``                                                                                                                                               ||         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| PackageIsVisible      | 1                                                                                                                         | If set, the package cannot be seen in the package manager.                                                                                                                                              | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| PackageIsDownloadable | 0                                                                                                                         | If set, the package cannot be downloaded in the front-end.                                                                                                                                              | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| PackageIsRemovable    | 1                                                                                                                         | If set, the package may be removed from the system.                                                                                                                                                     | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| BuildHost             | host.example.com                                                                                                          | Automatically filled during creation.                                                                                                                                                                   | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| BuildDate             | 2022-01-01                                                                                                                | Automatically filled during creation.                                                                                                                                                                   | Yes      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|| PackageRequired      || Package Name                                                                                                             || Describes dependencies including versions. Can be used multiple times. Requires a Version attribute.                                                                                                   || No      |
||                      ||                                                                                                                          || ``<PackageRequired Version="1.0.3">SomeOtherPackage</PackageRequired>``                                                                                                                                ||         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| ModuleRequired        | MIME::Tools                                                                                                               | Perl modules that must be installed beforehand (optional).                                                                                                                                              | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| OS                    | linux                                                                                                                     | Possible options are linux, darwin, mswin32. Defines operating system requirements, if needed.                                                                                                          | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|| Filelist             || ``<File Permission="644" Location="Kernel/Config/Files/Calendar.pm"/>``                                                  || This is a list of files included in the package. Self-closed tag. Can be used multiple time and requires a Permission and Location attribute.                                                          || No      |
||                      || ``<File Permission="644" Location="Kernel/Modules/AgentCalendar.pm"/>``                                                  ||                                                                                                                                                                                                        ||         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| DatabaseInstall       | see :ref:`example <PackageBuilding SQLExampleInstall>`                                                                    | Database commands to be executed during install. See :ref:`if attributes <PackageBuilding IfAttributes>`.                                                                                               | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| DatabaseUpgrade       | see :ref:`example <PackageBuilding SQLExampleUpgrade>`                                                                    | Database commands to be executed during upgrade. See :ref:`if attributes <PackageBuilding IfAttributes>`.                                                                                               | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| DatabaseReinstall     | see :ref:`example <PackageBuilding SQLExampleReinstall>`                                                                  | Database commands to be executed during re-installation. See :ref:`if attributes <PackageBuilding IfAttributes>`.                                                                                       | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| DatabaseUninstall     | see :ref:`example <PackageBuilding SQLExampleUninstall>`                                                                  | Database commands to be executed during removal. See :ref:`if attributes <PackageBuilding IfAttributes>`.                                                                                               | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| IntroInstall          | ``<IntroInstall Type="post" Lang="en" Title="Some Title"><![CDATA[Some Info formatted in HTML....]]></IntroInstall>``     | To show a "pre" or "post" install introduction in installation dialog. Can be used multiple times for extra languages.                                                                                  | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| IntroUninstall        | ``<IntroUninstall Type="post" Lang="en" Title="Some Title"><![CDATA[Some Info formatted in HTML....]]></IntroUninstall>`` | To show a "pre" or "post" uninstall introduction in uninstallation dialog.                                                                                                                              | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| IntroReinstall        | ``<IntroReinstall Type="post" Lang="en" Title="Some Title"><![CDATA[Some Info formatted in html....]]></IntroReinstall>`` | To show a "pre" or "post" reinstall introduction in re-installation dialog.                                                                                                                             | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| IntroUpgrade          | ``<IntroUpgrade Type="post" Lang="en" Title="Some Title"><![CDATA[Some Info formatted in html....]]></IntroUpgrade>``     | To show a "pre" or "post" upgrade introduction in upgrading dialog.                                                                                                                                     | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| CodeInstall           | see :ref:`example <PackageBuilding CodeExampleInstall>`                                                                   | Code to be executed during installation. See :ref:`if <PackageBuilding IfAttributes>` attributes.                                                                                                       | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| CodeUninstall         | see :ref:`example <PackageBuilding CodeExampleUninstall>`                                                                 | Code to be executed during removal. See :ref:`if <PackageBuilding IfAttributes>` attributes.                                                                                                            | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| CodeReinstall         | see :ref:`example <PackageBuilding CodeExampleReinstall>`                                                                 | Code to be executed during re-installation. See :ref:`if <PackageBuilding IfAttributes>` attributes.                                                                                                    | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
| CodeUpgrade           | see :ref:`example <PackageBuilding CodeExampleUpgrade>`                                                                   | Code to be executed during upgrade. See :ref:`if <PackageBuilding IfAttributes>` attributes.                                                                                                            | No       |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|| PackageMerge         || ``<PackageMerge Name="MergeOne" TargetVersion="2.0.0"></PackageMerge>``                                                  || This tag singals that a package has been merged into another package. In this case the original package needs to be removed from the file system and the packages database, but all data must be kept. || No      |
||                      ||                                                                                                                          || Let's assume that ``PackageOne`` was merged into ``PackageTwo``. Then ``PackageTwo.sopm`` should contain this.                                                                                         ||         |
||                      ||                                                                                                                          || See :ref:`notes below <PackageBuilding CodeMergeInfo>`                                                                                                                                                 ||         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+
|                       |                                                                                                                           |                                                                                                                                                                                                         |          |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+


SQL Examples
============

**Example SQL Install:**

.. _PackageBuilding SQLExampleInstall:

.. code-block:: xml
   
   <DatabaseInstall>
      <TableCreate Name="calendar_event">
      <Column Name="id" Required="true" PrimaryKey="true" AutoIncrement="true" Type="BIGINT"/>
      <Column Name="title" Required="true" Size="250" Type="VARCHAR"/>
      <Column Name="content" Required="false" Size="250" Type="VARCHAR"/>
      <Column Name="start_time" Required="true" Type="DATE"/>
      <Column Name="end_time" Required="true" Type="DATE"/>
      <Column Name="owner_id" Required="true" Type="INTEGER"/>
      <Column Name="event_status" Required="true" Size="50" Type="VARCHAR"/>
      </TableCreate>
   </DatabaseInstall>

**Example SQL Update**

.. _PackageBuilding SQLExampleUpgrade:

.. code-block:: xml

   <DatabaseUpgrade>
       <TableCreate Name="calendar_event_involved" Version="1.3.4">
           <Column Name="event_id" Required="true" Type="BIGINT"/>
           <Column Name="user_id" Required="true" Type="INTEGER"/>
       </TableCreate>
   </DatabaseUpgrade>

**Example SQL Reinstall**

.. _PackageBuilding SQLExampleReinstall:

.. code-block:: xml
   
   <DatabaseReinstall></DatabaseReinstall>
                            

**Example SQL Uninstall**

.. _PackageBuilding SQLExampleUninstall:

.. code-block:: xml

   <DatabaseUninstall>
      <TableDrop Name="calendar_event" />
   </DatabaseUninstall>

.. note::

   You also can choose ``<Database* Type="post">`` or ``<Database* Type="pre">`` to define the time of execution separately (``post`` is default). 
   For more info see package life cycle. Information on which actions have to be performed in case of an upgrade (optional). 
   Example if already installed package version is below 1.3.4 (e. g. 1.2.6), the defined action will be performed:

Introduction Texts
===================

**Package Texts**

For some tags it's possible to use HTML formatted texts. You can also use the ``Format`` attribute to define if you want to use "html" (which is default) or "plain" to use automatically a ``<pre></pre>`` tag when text is shown (to keep the newlines and whitespace of the content).

Helper Code Examples
====================

**Code Installation Example**

.. _PackageBuilding CodeExampleInstall:

It may be necessarry to execute perl code upon installation. Add this tag to your SOPM.

.. code-block:: xml

   <CodeInstall><![CDATA[
   # log example
   $Kernel::OM->Get('Kernel::System::Log')->Log(
         Priority => 'notice',
         Message => "Some Message!",
   );
   # database example
   $Kernel::OM->Get('Kernel::System::DB')->Do(SQL => "SOME SQL");
   ]]></CodeInstall>

**Code Uninstallation Example**

.. _PackageBuilding CodeExampleUninstall:

It may be necessary to execute perl code upon installation. Add this tag to your SOPM.

.. code-block:: xml

   <CodeUninstall><![CDATA[
   # log example
   $Kernel::OM->Get('Kernel::System::Log')->Log(
         Priority => 'notice',
         Message => "Some Message!",
   );
   # database example
   $Kernel::OM->Get('Kernel::System::DB')->Do(SQL => "SOME SQL");
   ]]></CodeUninstall>

**Code Reinstall Example**

.. _PackageBuilding CodeExampleReinstall:

It may be necessary to execute perl code upon installation. Add this tag to your SOPM.

.. code-block:: xml

   <CodeReinstall><![CDATA[
   # log example
   $Kernel::OM->Get('Kernel::System::Log')->Log(
         Priority => 'notice',
         Message => "Some Message!",
   );
   # database example
   $Kernel::OM->Get('Kernel::System::DB')->Do(SQL => "SOME SQL");
   ]]></CodeReinstall>

**Code Upgrade Example**

.. _PackageBuilding CodeExampleUpgrade:

It may be necessary to execute perl code upon installation. Add this tag to your SOPM.

.. code-block:: xml

   <CodeUpgrade><![CDATA[
   # log example
   $Kernel::OM->Get('Kernel::System::Log')->Log(
         Priority => 'notice',
         Message => "Some Message!",
   );
   # database example
   $Kernel::OM->Get('Kernel::System::DB')->Do(SQL => "SOME SQL");
   ]]></CodeUpgrade>
                            

.. note:: 

   You also can choose ``<Code* Type="post">`` or ``<Code* Type="pre">`` to define the time of execution separately (``post`` is default). 
   For more info see Package Life Cycle. Perl code to be executed when the package is upgraded (subject to ``version`` tag), (optional). Example if already installed package version is below 1.3.4 (e. g. 1.2.6), defined action will be performed.

Merging Packages
================

**Code Merging Notes**

.. _PackageBuilding CodeMergeInfo:

Additionally it is possible to add required database and code upgrade tags for ``PackageOne`` to make sure that it gets properly upgraded to the ``TargetVersion`` *before* merging it - to avoid inconsistency problems. Here's how this could look like:

.. code:: xml

   <PackageMerge Name="MergeOne" TargetVersion="2.0.0">
      <DatabaseUpgrade Type="merge">
         <TableCreate Name="merge_package">
               <Column Name="id" Required="true" PrimaryKey="true" AutoIncrement="true" Type="INTEGER"/>
               <Column Name="description" Required="true" Size="200" Type="VARCHAR"/>
         </TableCreate>
      </DatabaseUpgrade>
   </PackageMerge>
                     

As you can see the attribute ``Type="merge"`` needs to be set in this case. These sections will only be executed if a package merge is possible.

Conditions: ``IfPackage`` and ``IfNotPackage``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _PackageBuilding IfAttributes:

These attributes can be added to the regular ``Database*`` and ``Code*`` sections. If they are present, the section will only be executed if another package is or is not in the local package repository.

.. code-block:: xml

   <DatabaseInstall IfPackage="AnyPackage">
         ...
   </DatabaseInstall>
                     

.. code-block:: xml

   <CodeUpgrade IfNotPackage="OtherPackage">
         ...
   </CodeUpgrade>
                     

   These attributes can be also set in the ``Database*`` and
   ``Code*`` sections inside the ``PackageMerge`` tags.

Example Source File
********************

This is an example spec file looks with some of the above tags.

.. code:: xml

   <?xml version="1.0" encoding="utf-8" ?>
   <otrs_package version="1.0">
         <Name>Calendar</Name>
         <Version>0.0.1</Version>
         <Framework>3.2.x</Framework>
         <Vendor>OTRS AG</Vendor>
         <URL>https://otrs.com/</URL>
         <License>GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007</License>
         <ChangeLog Version="1.1.2" Date="2013-02-15 18:45:21">Added some feature.</ChangeLog>
         <ChangeLog Version="1.1.1" Date="2013-02-15 16:17:51">New package.</ChangeLog>
         <Description Lang="en">A web calendar.</Description>
         <Description Lang="de">Ein Web Kalender.</Description>
         <IntroInstall Type="post" Lang="en" Title="Thank you!">Thank you for choosing the Calendar module.</IntroInstall>
         <IntroInstall Type="post" Lang="de" Title="Vielen Dank!">Vielen Dank fuer die Auswahl des Kalender Modules.</IntroInstall>
         <BuildDate>?</BuildDate>
         <BuildHost>?</BuildHost>
         <Filelist>
            <File Permission="644" Location="Kernel/Config/Files/Calendar.pm"></File>
            <File Permission="644" Location="Kernel/System/CalendarEvent.pm"></File>
            <File Permission="644" Location="Kernel/Modules/AgentCalendar.pm"></File>
            <File Permission="644" Location="Kernel/Language/de_AgentCalendar.pm"></File>
            <File Permission="644" Location="Kernel/Output/HTML/Standard/AgentCalendar.tt"></File>
            <File Permission="644" Location="Kernel/Output/HTML/NotificationCalendar.pm"></File>
            <File Permission="644" Location="var/httpd/htdocs/images/Standard/calendar.png"></File>
         </Filelist>
         <DatabaseInstall>
            <TableCreate Name="calendar_event">
               <Column Name="id" Required="true" PrimaryKey="true" AutoIncrement="true" Type="BIGINT"/>
               <Column Name="title" Required="true" Size="250" Type="VARCHAR"/>
               <Column Name="content" Required="false" Size="250" Type="VARCHAR"/>
               <Column Name="start_time" Required="true" Type="DATE"/>
               <Column Name="end_time" Required="true" Type="DATE"/>
               <Column Name="owner_id" Required="true" Type="INTEGER"/>
               <Column Name="event_status" Required="true" Size="50" Type="VARCHAR"/>
            </TableCreate>
         </DatabaseInstall>
         <DatabaseUninstall>
            <TableDrop Name="calendar_event"/>
         </DatabaseUninstall>
   </otrs_package>
               
Build Package
**************

To build a package from the specification file, do the following.

.. code-block:: screen

   shell> bin/otrs.Console.pl Dev::Package::Build /path/to/example.sopm /tmp
   Building package...
   Done.
               

Package Life Cycle
*******************


Install/Upgrade/Uninstall
=========================

The following image shows you how the life cycle of a package installation/upgrade/un-installation works in the backend step by step.

.. mermaid::

   graph LR
       subgraph Package Life Cycle
           A[OS, Framework, Package, Modules]
           B[Code Execution]
           C[Database Processing]
           D[File Processing]
           E[Database Execution]
           F[Code Processing]
               subgraph Check Process
                   A
               end
               subgraph Pre
                   A --> B --> C
               end
               subgraph Processing
                   C --> D
               end
               subgraph Post
                   D --> E --> F
               end
           end