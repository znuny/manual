=============
Update to 7.0
=============

.. note::	We highly recommend to update on a test instance first.

This documentation explains how to update to the Znuny 7.0 release.

Please note that your current system needs to be a

- Znuny LTS 6.5.x or Znuny 7.0.x for a patch level update

to perform the update. We do not support direct updates from any version before Znuny LTS 6.5.

IMPORTANT: The base settings have been changed to reflect the new product name. This means, that you may either switch to the new user znuny and new base dir /opt/znuny, or keep your old settings.
If you decide to change, you'll need to create the new user, and modify your Config.pm settings before continuing. This upgrading instruction now uses <HOME_DIR> and <APP_USER>.

Preparations
~~~~~~~~~~~~

Before the update can started we need to perform some tasks to prepare the update.

Check if every add-on your are using is available for version 7.0. You don't have to care on packages which are already integrated, see the list of them in the :ref:`release notes <Integrated features 7.0>`.

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
	su -c 'bin/znuny.Daemon.pl stop' - otrs

..

Update via RPM
~~~~~~~~~~~~~~

The update via RPM.

You can find the correct URL for your RPM at https://www.znuny.org/releases. 

.. code-block:: 

	# Update to Znuny 7.0 (RHEL 7 / CentOS 7)
	yum update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.0.6-01.noarch.rpm

	# Check for missing modules and add required modules
	<HOME_DIR>/bin/znuny.CheckModules.pl --all

.. 

Update via source
~~~~~~~~~~~~~~~~~~

The installation from source takes some more steps. If there are more file to restore than mentioned in the restore block, add them by yourself.

.. code-block::

	# Download latest Znuny 7.0
	cd /opt
	wget https://download.znuny.org/releases/znuny-latest-7.0.tar.gz

	# Extract
	tar xfz znuny-latest-7.0.tar.gz

	# Set permissions
	# If you intend on keeping the previous user, then run this command.
	# The new default user is znuny
	/opt/znuny-7.0.6/bin/znuny.SetPermissions.pl --znuny-user <APP_USER>

	# Restore Kernel/Config.pm, articles, etc.
	cp -av <HOME_DIR>/Kernel/Config.pm /opt/znuny-7.0.6/Kernel/
	mv <HOME_DIR>/var/article/* /opt/znuny-7.0.6/var/article/

	# Restore dotfiles from the homedir to the new directory
	for f in $(find -L /opt/znuny -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.0.6/; done

	# Restore modified and custom cron job
	for f in $(find -L <HOME_DIR>/var/cron -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.0.6/var/cron/; done

	# Delete the old symlink
	rm /opt/<HOME_DIR>
	
	# Create a symlink 
	ln -s /opt/znuny-7.0.6 /opt/<HOME_DIR>

	# Check for missing modules and add required modules
	<HOME_DIR>/bin/znuny.CheckModules.pl --all

..

Execute the migration script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    su - <APP_USER>
    scripts/MigrateToZnuny7_0.pl

..

Update installed packages
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Packages for Znuny LTS (6.5.x) are not compatible with Znuny 7.0 and have to be updated.


.. code-block::

    su - <APP_USER>
    bin/znuny.Console.pl Admin::Package::UpgradeAll

..


Restart everything
~~~~~~~~~~~~~~~~~~

.. code-block::

	# Fill the crontab and wait(!) at least 5 minutes that the Daemon is started via cron
	su -c 'bin/Cron.sh start' - <APP_USER>

	# Start the webserver
	systemctl start httpd # CentOS / RHEL
	systemctl start apache2 # Debian / Ubuntu

	# Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
	systemctl start postfix

..
