Update to 6.4
#############
.. _PageNavigation install_update-6_4:

.. note:: Test your Update

  We highly recommend to update on a test instance first.

A Step-by-Step explanation on how to update to Znuny 6.4.

.. important:: 

  Please make sure your current system is at the latest patchlevel version of 6.3, this is 6.3.4


We do not support direct updates from any version of OTRS, ((OTRS)) Community Edition, Znuny LTS or before 6.3

For updates from OTRS, ((OTRS)) Community Edition, or Znuny LTS contact `Znuny GmbH <https://www.znuny.com>`_ or the experts of your choice for assistance.

Preparations
************

Before the update can started we need to perform some tasks to prepare the update.

You should or should have entered a scheduled maintenance time period in the admin area. Login as your admin user, select the active maintenance window and kill all sessions but your own. Now only administrators can login.

.. figure:: images/kill_sessions.png
	:alt: Maintenance Session Managment

	Maintenance Session Managment

Create a backup of the database, the application and all data, especially the attachments.

Check if every add-on you are using is available for version 6.4.

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


New Required Modules
********************

If you want to use the JSON web token support (JWT) for web servivces please ensure the installation of the following Perl modules:

* Crypt::JWT - optional, only when JSON web token support should be used
* Crypt::OpenSSL::X509 - optional, only when using JWT with X509 certificates

Update via RPM
***************

The update via RPM.

You can find the correct URL for your RPM at https://www.znuny.org/releases. 

.. code-block::

  # Update to Znuny 6.4 (RHEL 7 / CentOS 7)
  yum update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-6.4.4-01.noarch.rpm

  # Check for missing modules and add required modules
  /opt/otrs/bin/otrs.CheckModules.pl --all


Update via source
*****************

The installation from source takes some more steps. If there are more file to restore than mentioned in the restore block, add them by yourself.

.. code-block::

  # Download latest Znuny 6.4
  cd /opt
  wget https://download.znuny.org/releases/znuny-latest-6.4.tar.gz

  # Extract
  tar xfz znuny-latest-6.4.tar.gz

  # Set permissions
  /opt/znuny-6.4.4/bin/otrs.SetPermissions.pl

  # Restore Kernel/Config.pm, articles, etc.
  cp -av /opt/otrs/Kernel/Config.pm /opt/znuny-6.4.4/Kernel/
  mv /opt/otrs/var/article/* /opt/znuny-6.4.4/var/article/

  # Restore dotfiles from the homedir to the new directory
  for f in $(find -L /opt/otrs -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.4.4/; done

  # Restore modified and custom cron job
  for f in $(find -L /opt/otrs/var/cron -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.4.4/var/cron/; done

  # Delete the old symlink
  rm /opt/otrs

  # Create a symlink 
  ln -s /opt/znuny-6.4.4 /opt/otrs

  # Check for missing modules and add required modules
  /opt/otrs/bin/otrs.CheckModules.pl --all


Execute the migration script
****************************

.. code-block::

  su - otrs
  scripts/MigrateToZnuny6_4.pl


Update All Packages
~~~~~~~~~~~~~~~~~~~

**Framework Updates:**
(For 6.3 to 6.4)

You have two options:

* Run the script, install the missing package using the package manager 

.. code-block::

  > bin/otrs.Console.pl Admin::Package::Upgrade LOCATIONOFYOURPACKAGE
  #or
  > bin/otrs.Console.pl Admin::Package::UpgradeAll
  #or by renamed packages
  > bin/otrs.Console.pl Admin::Package::Upgrade LOCATIONOFYOURPACKAGE

Update installed packages (if not done above)
*********************************************

.. note:: Packages for earlier versions of Znuny LTS (6.0.x) or Znuny (>=6.1.x) might not be compatible with Znuny 6.4 and have to be updated. Please contact the vendor of the packages before upgrading if you have doubts.

If all packages are available online, you can use the console command for updating.

.. note:: UpgradeAll should only be performed, after your target version has been reached. 
	
.. note:: UpgradeAll can fail, if repositories are not reachable or configured, versions for your framework are not available, or packages have been renamed. In this case, you should upgarde your packages manually via the commandline or by installing/updating them via the package manager.

.. code-block::

  su - otrs
  bin/otrs.Console.pl Admin::Package::UpgradeAll

If the repository is not registered or available, download the package and update manually using the package manager, or command line.

Restart everything
*******************

.. code-block::

  # Fill the crontab and wait(!) at least 5 minutes that the Daemon is started via cron
  su -c 'bin/Cron.sh start' - otrs

  # Start the webserver
  systemctl start httpd # CentOS / RHEL
  systemctl start apache2 # Debian / Ubuntu

  # Start your local MTA, mostly Postfix, sometimes Exim or Sendmail
  systemctl start postfix

Deactivate maintenance 
**********************

Don't forget to deactivate the scheduled maintenance, so that your users and customers can login again.


Post Update Changes
********************

ACLs
~~~~

.. versionadded:: 6.4.4

  If you use an ACL which Matches or Limits ``Ticket => NewOwner``, the behavior has changed to use the login and not display name of the user.


