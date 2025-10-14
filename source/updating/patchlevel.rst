==================
Patch Level Update
==================

This documentation explains how to perform a patch level update for Znuny 7.3.

.. note::   Your current system needs to be a Znuny 7.3.x where the x stands for the patch level. You can skip intermediate **patch levels**, e.g. update from 7.3.1 directly to 7.3.6


Prepare
*******

Stop all services to prevent any data from changing.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block::

          systemctl stop httpd
          # Stop your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl stop postfix 
          # Remove crontab, stop daemon
          su -c 'bin/Cron.sh stop' - znuny
          su -c 'bin/znuny.Daemon.pl stop' - znuny

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::
  
          systemctl stop apache2
          # Stop your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl stop postfix 
          # Remove crontab, stop daemon
          su -c 'bin/Cron.sh stop' - znuny
          su -c 'bin/znuny.Daemon.pl stop' - znuny
..


Backup
******  

Backup your system like you always do. The easiest way for small system is using the bundled backup script `scripts/backup.pl`.

Update
******

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

        .. code-block::

            rpm -Uvh https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.3.1-01.noarch.rpm
            su - znuny -c 'scripts/MigrateToZnuny7_3.pl --verbose'
            su - znuny -c 'bin/znuny.Console.pl Admin::Package::ReinstallAll'
            su - znuny -c 'scripts/MigrateToZnuny7_3.pl --verbose'
            # optional upgrade of the installed addons found in configured repositories
            su - znuny -c 'bin/znuny.Console.pl Admin::Package::UpgradeAll'

            # Clear log and application cache
            su - znuny -c 'bin/znuny.Console.pl Maint::Cache::Delete'
            su - znuny -c 'bin/znuny.Console.pl Maint::Log::Clear'
        
  .. tab-item:: Source installation
    :sync: source

        .. code-block:: bash

            cd /opt
            curl https://download.znuny.org/releases/znuny-latest-7.3.tar.gz | tar -xz

            # Restore Kernel/Config.pm, articles, etc.
            cp -av /opt/znuny/Kernel/Config.pm /opt/znuny-7.3.1/Kernel/
            mv /opt/znuny/var/article/* /opt/znuny-7.3.1/var/article/

            # Restore dotfiles from the homedir to the new directory
            for f in $(find -L /opt/znuny -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.3.1/; done

            # Restore modified and custom cron job
            for f in $(find -L /opt/znuny/var/cron -maxdepth 1 -type f -name \* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.3.1/var/cron/; done

            # Set the permissions
            znuny-7.3.1/bin/znuny.SetPermissions.pl
            ln -snf /opt/znuny-7.3.1 /opt/znuny

            su - znuny -c 'scripts/MigrateToZnuny7_3.pl --verbose'
            su - znuny -c 'bin/znuny.Console.pl Admin::Package::ReinstallAll'
            su - znuny -c 'scripts/MigrateToZnuny7_3.pl --verbose'
            # optional upgrade of the installed addons found in configured repositories
            su - znuny -c 'bin/znuny.Console.pl Admin::Package::UpgradeAll'

            # Clear log and application cache
            su - znuny -c 'bin/znuny.Console.pl Maint::Cache::Delete'
            su - znuny -c 'bin/znuny.Console.pl Maint::Log::Clear'

..


Start Znuny
***********

Start all services again. We do not start the Znuny daemon manually, instead we wait for cron starting the daemon.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block::

          systemctl start httpd
          # Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl start postfix 
          # Create Znuny's crontab to start the daemon
          su -c 'bin/Cron.sh start' - znuny

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::
  
          systemctl start apache2
          # Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl start postfix 
          # Create Znuny's crontab to start the daemon
          su -c 'bin/Cron.sh start' - znuny

..
