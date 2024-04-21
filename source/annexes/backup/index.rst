Backing Up Your System
######################

A backup is a very personal choice, mostly based on the infrastructure you're using. Sometimes, regulations also require certain backup strategies to be implemented. In order to backup your system properly, you must first understand the architecture of the system you're dealing with. You will also have to have a recovery strategy, including disaster recovery. In this case, there are issues we need to address here.

System Architecture
*******************

Znuny is a web-based application, which uses portable code to access a relational database management system (RDBMS). It saves its data explicitly on the DB, unless otherwise directed. Long-term storage can be used for persistent data like communications and attachments, as well as for temporary data like sessions and cache. Configuration data is primarily located in the database, however defaults and some special configurations are only located in the file system. Underlying resources, like the Perl installation (including all its modules), the web server, the database and the OS, are completely autonomous and can be switched practically at will. Other components, like network, firewall, directory, mail and proxy servers, for example, are another concern and need be internally understood during a recovery or migration to a new environment or server.

Backup Checklist
*****************

.. important:: 

   As always, these steps are only a recommendation, and may include more or fewer steps than needed.

- Stop all services related to Znuny
  - Web server
  - MTA
  - Daemon
  - Cron
- Backup the database
- Backup Kernel/Config.pm
- Backup dot files and dot folder in the application home like .procmailrc
- Backup custom cron tasks from var/cron (if added or modified)
- Backup own XML configuration files
- Backup own modules or scripts
- Backup PGP/SMIME certs (if used)
- Backup attachment directory (when ArticleStorageDB)
- Backup underlying service configuration and settings (Web server, MTA, DBMS)

Restoring or Recovery
*********************

.. important:: 

   As always, these steps are only a recommendation, and may include more or fewer steps than needed.

- Install base operating system and additional required software oh
- Restore underlying service configurations and settings (Web server, MTA, DBMS)
- Download and unpack the desired Znuny version (The most current patch level, or next minor version.)
- Restore database backup
- Place all saved configuration and files as backed up above in the correct place
- Set Permissions using the onboard script
- Build the configuration using ``bin/znuny.Console.pl Maint::Config::Sync``
- Run ``bin/znuny.Console.pl Admin::Package::ReinstallAll``
- Start all supporting services
- Restart the cron, make sure the .dist files have been renamed or replaced from your backup, ``bin/Cron.sh start``

Backup Script Example
*********************

An example script is available to backup your system. We recommend this for small to mid-sized systems only.

.. warning::

  This works for users of MySQL, MariaDB, and PostgreSQL only if backing up the database. Also, all articles will be compressed as well. This script may take some time to run, as it will attempt in 2/3 cases to compress the attachments as well, and is not threaded.

Using this script, you can quickly get a backup running on smaller systems. You should still stop all services, before running this script, and restart them afterward.

.. code-block:: shell

  [znuny@example ~]$ scripts/backup.pl -h
  
  Backup a Znuny system.
  
  Usage:
   backup.pl -d /data_backup_dir [-c gzip|bzip2] [-r DAYS] [-t fullbackup|nofullbackup|dbonly]
  
  Options:
   -d                     - Directory where the backup files should place to.
   [-c]                   - Select the compression method (gzip|bzip2). Default: gzip.
   [-r DAYS]              - Remove backups which are more than DAYS days old.
   [-t]                   - Specify which data will be saved (fullbackup|nofullbackup|dbonly). Default: fullbackup.
   [-h]                   - Display help for this command.
  
  Help:
  Using -t fullbackup saves the database and the whole Znuny home directory (except /var/tmp and cache directories).
  Using -t nofullbackup saves only the database, /Kernel/Config* and /var directories.
  With -t dbonly only the database will be saved.
  
  Output:
   Config.tar.gz          - Backup of /Kernel/Config* configuration files.
   Application.tar.gz     - Backup of application file system (in case of full backup).
   VarDir.tar.gz          - Backup of /var directory (in case of no full backup).
   DataDir.tar.gz         - Backup of article files.
   DatabaseBackup.sql.gz  - Database dump.

Restore Script Example
**********************

Parallel to the backup example script, a restore script as also available.

.. code-block:: shell

  [znuny@example ~]$ scripts/restore.pl -h
  
  Restore a Znuny system from backup.
  
  Usage:
   restore.pl -b /data_backup/<TIME>/ -d /opt/znuny/
  
  Options:
   -b                     - Directory of the backup files.
   -d                     - Target Znuny home directory.
   [-h]                   - Display help for this command.
  
Restoring using this method requires

- Prepare your target using the :ref:`pagenavigation installupdate_install`.
- Restore underlying service settings.
- Restore external files and folders not included in the application directory.
- Extract the Config.pm from your backup.
- The database, user, and home from your Source Config.pm must be correct and available
- Run the script.
- Alternatively, use the latest patch level version, and update all packages after running the migration script.
- Fill the crontab ``bin/Cron.sh start``
- Restart your required service like teh web server, cron etc.
- Test functionality.
