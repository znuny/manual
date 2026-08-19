==================
Patch Level Update
==================

This documentation explains how to perform a patch level update for Znuny LTS 6.5.

.. note::   Your current system needs to be a Znuny LTS 6.5.x where the x stands for the patch level. You can skip intermediate **patch levels**, e.g. update from 6.5.14 directly to 6.5.24


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
          su -c 'bin/Cron.sh stop' - otrs
          su -c 'bin/otrs.Daemon.pl stop' - otrs

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::
  
          systemctl stop apache2
          # Stop your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl stop postfix 
          # Remove crontab, stop daemon
          su -c 'bin/Cron.sh stop' - otrs
          su -c 'bin/otrs.Daemon.pl stop' - otrs
..


Backup
******  

Backup your system like you always do. The easiest way for small system is using the bundled backup script `scripts/backup.pl`.

Update
******

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RPM installation

        Starting with LTS version 6.5.20 we sign our RPMs. Please import our GPG key with these instructions:

        .. code-block:: bash

            curl -LO https://download.znuny.org/znuny-release-key.asc
            rpm --import znuny-release-key.asc

        .. code-block::

            rpm -Uvh https://download.znuny.org/releases/RPMS/rhel/7/znuny-6.5.24-01.noarch.rpm
            su - otrs -c 'scripts/MigrateToZnuny6_5.pl --verbose'
            su - otrs -c 'bin/otrs.Console.pl Admin::Package::ReinstallAll'
            su - otrs -c 'scripts/MigrateToZnuny6_5.pl --verbose'
            # optional upgrade of the installed addons found in configured repositories
            su - otrs -c 'bin/otrs.Console.pl Admin::Package::UpgradeAll'

            # Clear log and application cache
            su - otrs -c 'bin/otrs.Console.pl Maint::Cache::Delete'
            su - otrs -c 'bin/otrs.Console.pl Maint::Log::Clear'
        
  .. tab-item:: Source installation
    :sync: source

        .. code-block:: bash

            cd /opt
            curl -LO https://download.znuny.org/releases/znuny-6.5.24.tar.gz
            tar -xzf znuny-6.5.24.tar.gz

            # Optional: verify the checksum of the downloaded version
            curl -LO https://download.znuny.org/releases/znuny-6.5.24.tar.gz.sha256
            sha256sum -c znuny-6.5.24.tar.gz.sha256

            # Optional: verify the GPG signature for the downloaded version, the import is only required once
            curl -LO https://download.znuny.org/znuny-release-key.asc
            gpg --import znuny-release-key.asc
            curl -LO https://download.znuny.org/releases/znuny-6.5.24.tar.gz.asc
            gpg --verify znuny-6.5.24.tar.gz.asc znuny-6.5.24.tar.gz

            # Restore Kernel/Config.pm, articles, etc.
            cp -av /opt/otrs/Kernel/Config.pm /opt/znuny-6.5.24/Kernel/
            mv /opt/otrs/var/article/* /opt/znuny-6.5.24/var/article/

            # Restore dotfiles from the homedir to the new directory
            for f in $(find -L /opt/otrs -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.5.24/; done

            # Restore modified and custom cron job
            for f in $(find -L /opt/otrs/var/cron -maxdepth 1 -type f -name \* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.5.24/var/cron/; done

            # Set the permissions
            znuny-6.5.24/bin/otrs.SetPermissions.pl
            ln -snf /opt/znuny-6.5.24 /opt/otrs

            su - otrs -c 'scripts/MigrateToZnuny6_5.pl --verbose'
            su - otrs -c 'bin/otrs.Console.pl Admin::Package::ReinstallAll'
            su - otrs -c 'scripts/MigrateToZnuny6_5.pl --verbose'
            # optional upgrade of the installed addons found in configured repositories
            su - otrs -c 'bin/otrs.Console.pl Admin::Package::UpgradeAll'

            # Clear log and application cache
            su - otrs -c 'bin/otrs.Console.pl Maint::Cache::Delete'
            su - otrs -c 'bin/otrs.Console.pl Maint::Log::Clear'

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
          su -c 'bin/Cron.sh start' - otrs

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::
  
          systemctl start apache2
          # Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl start postfix 
          # Create Znuny's crontab to start the daemon
          su -c 'bin/Cron.sh start' - otrs

..
