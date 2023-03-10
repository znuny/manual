Update to 6.5
#############
.. _PageNavigation install_update-6_5:

.. note:: Test your Update

  We highly recommend to update on a test instance first.

A Step-by-Step explanation on how to update to Znuny 6.5.

.. important:: 

  Please make sure your current system is at the latest patchlevel version of 6.4


We do not support direct updates from any version of OTRS, ((OTRS)) Community Edition, Znuny LTS or before 6.4

For updates from OTRS, ((OTRS)) Community Edition, or Znuny LTS contact `Znuny GmbH <https://www.znuny.com>`_ or the experts of your choice for assistance.

Preparations
************

Before the update can started we need to perform some tasks to prepare the update.

Check if every add-on you are using is available for version 6.5.

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

None

Update via RPM
***************

The update via RPM.

You can find the correct URL for your RPM at https://www.znuny.org/releases. 

.. code-block::

  # Update to Znuny 6.5 (RHEL 7 / CentOS 7)
  yum update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-6.5.1-01.noarch.rpm

  # Check for missing modules and add required modules
  /opt/otrs/bin/otrs.CheckModules.pl --all


Update via source
*****************

The installation from source takes some more steps. If there are more file to restore than mentioned in the restore block, add them by yourself.

.. code-block::

  # Download latest Znuny 6.5
  cd /opt
  wget https://download.znuny.org/releases/znuny-latest-6.5.tar.gz

  # Extract
  tar xfz znuny-latest-6.5.tar.gz

  # Set permissions
  /opt/znuny-6.5.1/bin/otrs.SetPermissions.pl

  # Restore Kernel/Config.pm, articles, etc.
  cp -av /opt/otrs/Kernel/Config.pm /opt/znuny-6.5.1/Kernel/
  mv /opt/otrs/var/article/* /opt/znuny-6.5.1/var/article/

  # Restore dotfiles from the homedir to the new directory
  for f in $(find -L /opt/otrs -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.5.1/; done

  # Restore modified and custom cron job
  for f in $(find -L /opt/otrs/var/cron -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-6.5.1/var/cron/; done

  # Delete the old symlink
  rm /opt/otrs

  # Create a symlink 
  ln -s /opt/znuny-6.5.1 /opt/otrs

  # Check for missing modules and add required modules
  /opt/otrs/bin/otrs.CheckModules.pl --all


Execute the migration script
****************************

.. code-block::

  su - otrs
  scripts/MigrateToZnuny6_5.pl


Update All Packages
~~~~~~~~~~~~~~~~~~~

.. note:: Packages for earlier versions of Znuny LTS (6.0.x) or Znuny (>=6.1.x) might not be compatible with Znuny 6.5 and have to be updated. Please contact the vendor of the packages before upgrading if you have doubts.

If all packages are available online, you can use the console command for updating.

.. code-block::

  su - otrs
  bin/otrs.Console.pl Admin::Package::UpgradeAll

If the repository is not registered or available, download the package and update manually using the package manager, or command line.

You have two options:

* Run the script, install the missing package using the package manager 

.. code-block::

  > bin/otrs.Console.pl Admin::Package::Upgrade LOCATIONOFYOURPACKAGE
  #or for renamed packages
  > bin/otrs.Console.pl Admin::Package::Install LOCATIONOFYOURPACKAGE


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

Post Update Changes
********************

None

