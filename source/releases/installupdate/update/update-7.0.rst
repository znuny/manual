=============
Update to 7.0
=============

.. note::	We highly recommend to update on a test instance first.

This documentation explains how to update to the Znuny 7.0 release.

Please note that your current system needs to be a:

- ((OTRS)) Community Edition 6.0.x,
- OTRS 6.0.x or 
- Znuny LTS 6.0.x

to perform the update. We do not support direct updates from  any version of OTRS or ((OTRS)) Community Edition before 6.0.


Preparations
~~~~~~~~~~~~

Before the update can started we need to perform some tasks to prepare the update.

Check if every add-on your are using is available for version 7.0. You don't have to care on packages which are already integrated, see the list of them in the :ref:`release notes<Integrated features 7.0>`.

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

	# Update to Znuny 7.0 (RHEL 7 / CentOS 7)
	yum update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.0.1-01.noarch.rpm

	# Check for missing modules and add required modules
	/opt/otrs/bin/otrs.CheckModules.pl --all

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
	/opt/znuny-7.0.1/bin/otrs.SetPermissions.pl

	# Restore Kernel/Config.pm, articles, etc.
	cp -av /opt/otrs/Kernel/Config.pm /opt/znuny-7.0.1/Kernel/
	mv /opt/otrs/var/article/* /opt/znuny-7.0.1/var/article/

	# Restore dotfiles from the homedir to the new directory
	for f in $(find -L /opt/otrs -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.0.1/; done

	# Restore modified and custom cron job
	for f in $(find -L /opt/otrs/var/cron -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.0.1/var/cron/; done

	# Delete the old symlink
	rm /opt/otrs
	
	# Create a symlink 
	ln -s /opt/znuny-7.0.1 /opt/otrs

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

.. note:: Packages for Znuny LTS (6.0.x) are not compatible with Znuny 7.0 and have to be updated.


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

