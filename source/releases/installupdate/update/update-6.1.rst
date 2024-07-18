=============
Update to 6.1
=============

.. note::	We highly recommend to update on a test instance first.

This documentation explains how to update to the Znuny 6.1 release.

Please note that your current system needs to be a:

- ((OTRS)) Community Edition 6.0.x,
- OTRS 6.0.x or 
- Znuny LTS 6.0.x

to perform the update. We do not support direct updates from  any version of OTRS or ((OTRS)) Community Edition before 6.0.


Preparations
~~~~~~~~~~~~

Before the update can started we need to perform some tasks to prepare the update.

You should or should have entered a scheduled maintenance time period in the admin area. Login as your admin user, select the active maintenance window and kill all sessions but your own. Now only administrators can login.

.. figure:: images/kill_sessions.png
	:alt: Maintenance Session Managment

	Maintenance Session Managment

Create a backup of the database, the application and all data, especially the attachments.

Check if every add-on your are using is available for version 6.1. You don't have to care on packages which are already integrated, see the list of them in the :ref:`release notes<Integrated features 6.1>`.

Create a backup of the database, the application and all data, especially the attachments.


.. code-block:: 
	:caption: **Stop all services**

	# Stop the webserver
	systemctl stop httpd # CentOS / RHEL
	systemctl stop apache2 # Debian / Ubuntu

	# Stop your local MTA, mostly Postfix, sometimes Exim or Sendmail
	systemctl stop postfix


	# Remove crontab, stop daemon
	su -c 'bin/Cron.sh stop' - otrs
	su -c 'bin/otrs.Daemon.pl stop' - otrs

..


Update via RPM
~~~~~~~~~~~~~~

The update via RPM.

You can find the correct URL for your RPM at https://www.znuny.org/releases. 

.. code-block:: 

	# Update to Znuny 6.1 (RHEL 7 / CentOS 7)
	yum update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-6.1.2-01.noarch.rpm

	# Check for missing modules and add required modules
	/opt/otrs/bin/otrs.CheckModules.pl --all

.. 

Update via source
~~~~~~~~~~~~~~~~~~

The installation from source takes some more steps. If there are more file to restore than mentioned in the restore block, add them by yourself.

.. code-block::

	# Download latest Znuny 6.1
	cd /opt
	wget https://download.znuny.org/releases/znuny-latest-6.1.tar.gz

	# Extract
	tar xfz znuny-latest-6.1.tar.gz

	# Set permissions
	/opt/znuny-6.1.2/bin/otrs.SetPermissions.pl

	# Restore Kernel/Config.pm, articles, etc.
	cp -av /opt/otrs/Kernel/Config.pm /opt/znuny-6.1.2/Kernel/
	mv /opt/otrs/var/article/* /opt/znuny-6.1.2/var/article/

	# Restore dotfiles from the homedir to the new directory
	for f in $(find -L /opt/otrs -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.1.2/; done

	# Restore modified and custom cron job
	for f in $(find -L /opt/otrs/var/cron -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.1.2/var/cron/; done

	# Delete the old symlink
	rm /opt/otrs
	
	# Create a symlink 
	ln -s /opt/znuny-6.1.2 /opt/otrs

	# Check for missing modules and add required modules
	/opt/otrs/bin/otrs.CheckModules.pl --all

..

Execute the migration script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    su - otrs
    scripts/MigrateToZnuny6_1.pl

..

Update installed packages
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Packages for Znuny LTS (6.0.x) are not compatible with Znuny 6.1 and have to be updated.

.. note:: UpgradeAll should only be performed, after your target version has been reached. 
	
.. note:: UpgradeAll can fail, if repositories are not reachable or configured, versions for your framework are not available, or packages have been renamed. In this case, you should upgarde your packages manually via the commandline or by installing/updating them via the package manager.


.. code-block::

    su - otrs
    bin/otrs.Console.pl Admin::Package::UpgradeAll

..


Restart everything
~~~~~~~~~~~~~~~~~~

.. code-block::

	# Fill the crontab and wait(!) at least 5 minutes that the Daemon is started via cron
	su -c 'bin/Cron.sh start' - otrs

	# Start the webserver
	systemctl start httpd # CentOS / RHEL
	systemctl start apache2 # Debian / Ubuntu

	# Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
	systemctl start postfix

..

Deactivate maintenance 
**********************

Don't forget to deactivate the scheduled maintenance, so that your users and customers can login again.
