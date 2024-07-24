Update to Znuny 7.1
###################

.. important::	We highly recommend to update on a test instance first. Znuny 7.1 performs database changes during the migration. Backup your data!

This documentation explains how to update to the Znuny 7.1 release.

Please note that your current system needs to be a

- Znuny 7.0.x for a minor level update or
- Znuny 7.1.x for a patch level update

We do not support direct updates from any version before Znuny 7.0.

.. note::

	The base settings have been changed to reflect the product name since Znuny 7.0. We use ``znuny`` as the application user, ``/opt/znuny`` the application home and also a different web server configuration. Please verify these settings:

    - ``Home`` - typically in Kernel/Config.pm as ``$Self->{Home}``
    - System Configuration ``FrontEnd::WebPath`` has the default value `/znuny-web/`
    - System Configuration ``ScriptAlias`` has the default value `znuny/`
	

Preparations
************

.. note::

  Check if every add-on your are using is available for version 7.1 **before** you continue. Add-ons for Znuny 7.0 or older versions are not compatible with Znuny 7.1 and needs to be updated. Ask the vendor of the add-on when in doubt.

Before the update can started we need to perform some tasks to prepare the update.

You should or should have entered a scheduled maintenance time period in the admin area. Login as your admin user, select the active maintenance window and kill all sessions but your own. Now only administrators can login.

.. figure:: images/kill_sessions.png
	:alt: Maintenance Session Managment

	Maintenance Session Managment


Create a backup of the database, the application and all data, especially the attachments.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block::
        :caption: Stop all services

          systemctl stop httpd
          # Stop your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl stop postfix 
          # Remove crontab, stop daemon
          su -c 'bin/Cron.sh stop' - znuny
          su -c 'bin/znuny.Daemon.pl stop' - znuny

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::
        :caption: Stop all services
  
          systemctl stop apache2
          # Stop your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl stop postfix 
          # Remove crontab, stop daemon
          su -c 'bin/Cron.sh stop' - znuny
          su -c 'bin/znuny.Daemon.pl stop' - znuny

..

Update via RPM
**************

The update via RPM for RHEL based Linux distributions.

You can find the correct URL for your RPM at https://www.znuny.org/releases. 

.. code-block:: 

	# Update to Znuny 7.1
	dnf update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.1.1-01.noarch.rpm

	# Check for missing modules and add required modules and install at least **required** modules.
	/opt/znuny/bin/znuny.CheckModules.pl --all

.. 

Update via source
*****************

The installation from source takes more steps. If there are more file to restore than mentioned in the restore block, add them by yourself.

.. code-block::

	# Download latest Znuny 7.1
	cd /opt
	wget https://download.znuny.org/releases/znuny-latest-7.1.tar.gz

	# Extract
	tar xfz znuny-latest-7.1.tar.gz

	# Set permissions
	/opt/znuny-7.1.1/bin/znuny.SetPermissions.pl

	# Restore Kernel/Config.pm, articles, etc.
	cp -a /opt/znuny/Kernel/Config.pm /opt/znuny-7.1.1/Kernel/
	mv /opt/znuny/var/article/* /opt/znuny-7.1.1/var/article/

	# Restore dotfiles from the homedir to the new directory
	for f in $(find -L /opt/znuny -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.1.1/; done

	# Restore modified and custom cron job
	for f in $(find -L /opt/znuny/var/cron -maxdepth 1 -type f -name \* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.1.1/var/cron/; done

	# Create/overwrite a symlink 
	ln -snf /opt/znuny-7.1.1 /opt/znuny

	# Check for missing modules and add **required** modules
	/opt/znuny/bin/znuny.CheckModules.pl --all

..

Execute the migration script
****************************

.. code-block::

    su -c 'scripts/MigrateToZnuny7_1.pl --verbose' - znuny

..

If the migration script fails check the error and try to fix it. Do **not** continue until the migration scripts returns "Migration completed!"

Update installed packages
*************************
	
.. note:: UpgradeAll can fail, if repositories are not reachable or configured, versions for your framework are not available, or packages have been renamed. In this case, you should upgarde your packages manually via the commandline or by installing/updating them via the package manager.

.. code-block::

    # Make sure all add-ons are correct installed after a patch level update
    su -c 'bin/znuny.Console.pl Admin::Package::ReinstallAll' - znuny
    # Upgrade all packages
    su -c 'bin/znuny.Console.pl Admin::Package::UpgradeAll' - znuny
    

..

Restart everything
******************

.. important:: Before starting the cron or mail service and daemon, you should ensure the frontend is working properly. Once new mails are received, or articles are created, a roll back is much more difficult, and mails may get lost.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block::
        :caption: Start all services

          systemctl start httpd
          # Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl start postfix 
          # Fill the crontab and wait(!) at least 5 minutes that the Daemon is started via cron
          su -c 'bin/Cron.sh start' - znuny

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::
        :caption: Start all services
  
          systemctl start apache2
          # Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
          systemctl start postfix 
          # Fill the crontab and wait(!) at least 5 minutes that the Daemon is started via cron
          su -c 'bin/Cron.sh start' - znuny

Deactivate maintenance 
**********************

Don't forget to deactivate the scheduled maintenance, so that your users and customers can log in again.
