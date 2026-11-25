.. meta::
   :description: Upgrade from Znuny 7.3.x to Znuny LTS 7.5 — check breaking changes, follow the migration steps, test on a staging system first and back up your data before running the upgrade scripts.
   :keywords: znuny update 7.5, znuny 7.3 to 7.5, znuny lts 7.5, minor level update, znuny upgrade, znuny migration

Update to Znuny LTS 7.5
#######################

.. important::	We highly recommend to update on a test instance first. Backup your data!

This documentation explains how to update to the Znuny LTS 7.5 release.

Please note that your current system needs to be a

- Znuny 7.3.x for a minor level update or
- Znuny 7.5.x for a patch level update (see :doc:`patchlevel`)

We do not support direct updates from any version before Znuny 7.3. Update to the latest Znuny 7.3 release first.
	

Preparations
************

.. note::

  Check if every add-on you are using is available for version 7.5 **before** you continue. Add-ons for Znuny 7.3 or older versions are not compatible with Znuny 7.5 and need to be updated. Ask the **vendor** of the add-on when in doubt.

Check the following changes in Znuny LTS 7.5 before you update. See the :doc:`release notes </releases/7_5_1/index>` for all changes.

- **SAML authentication:** If you use SAML, Net::SAML2 0.89 or higher is required, and assertion signatures are now verified against the configured IdP certificate. Make sure ``AuthModule::SAML::IdPCACert`` (agents) and ``Customer::AuthModule::SAML::IdPCACert`` (customers) are set correctly.
- **Session cookie names:** The default session cookie names change to ``ZnunyAgentInterface`` and ``ZnunyCustomerInterface``. Unchanged values of ``SessionName`` and ``CustomerPanelSessionName`` are migrated automatically. If a reverse proxy, load balancer or single sign-on setup refers to the old names ``OTRSAgentInterface`` or ``OTRSCustomerInterface``, adjust it.
- **Time zone setting:** The system configuration setting ``OTRSTimeZone`` is renamed to ``ZnunyTimeZone``. The value is migrated automatically. Adjust ``Kernel/Config.pm`` or custom code if it sets or reads ``OTRSTimeZone``.
- **Package repositories:** Znuny now only requests the repository index file ``packages.xml``; ``otrs.xml`` is no longer used. Self-hosted package repositories have to provide ``packages.xml``.
- **Integrated packages:** The packages Znuny-AdvancedAttachments, Znuny-ZoomArticlePDFPreview and Znuny-CustomerCompanyService (and their Znuny4OTRS predecessors) are now part of Znuny. The migration script uninstalls them and migrates their system configuration settings, e.g. ``Znuny4OTRSZoomArticlePDFPreview###Width`` to ``ArticleZoomPDFPreview###Width`` and ``ZnunyAdvancedAttachments###ShowDuplicateFiles`` to ``Attachment###ShowDuplicateFiles``.
- **SAML and two-factor authentication:** Znuny's two-factor authentication is skipped for SAML logins. Enforce multi-factor authentication at the Identity Provider.
- **Customer self-registration:** Self-registration in the customer interface is now disabled by default. If your customers register themselves, check ``CustomerPanelCreateAccount`` after the update. Only the fields in ``CustomerPanelCreateAccount::AllowedFields`` are accepted, and the login and customer ID are taken from the email address.
- **E-mail headers:** The PostMaster headers ``X-OTRS-*`` are renamed to ``X-Znuny-*``. Incoming ``X-OTRS-*`` headers still work, and ``PostmasterX-Header``, ``KeepStateHeader`` and the PostMaster filters are migrated automatically.
- **Placeholders:** Placeholders now use the prefix ``ZNUNY_``. Existing ``OTRS_`` placeholders keep working.
- **Removed console commands:** ``Dev::Code::CPANAudit`` and ``Dev::Code::CPANUpdate`` have been removed. Remove them from your own scripts or cron jobs.

Before the update can be started we need to perform some tasks to prepare the update.

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

.. important::

  All Znuny RPMs are signed. Please import our GPG key with these instructions:

  .. code-block:: bash

    curl -LO https://download.znuny.org/znuny-release-key.asc
    rpm --import znuny-release-key.asc

You can find the correct URL for your RPM at https://www.znuny.org/releases. 

.. code-block:: bash

	# Update to Znuny 7.5
	dnf update -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.5.1-01.noarch.rpm

	# Check for missing modules and add required modules and install at least **required** modules.
	/opt/znuny/bin/znuny.CheckModules.pl --all

.. 

Update via source
*****************

The installation from source takes more steps. If there are more file to restore than mentioned in the restore block, add them by yourself.

.. code-block:: bash

  # Download latest Znuny 7.5
  cd /opt
  wget https://download.znuny.org/releases/znuny-7.5.1.tar.gz

  # Optional: verify the checksum of the downloaded version
  curl -LO https://download.znuny.org/releases/znuny-7.5.1.tar.gz.sha256
  sha256sum -c znuny-7.5.1.tar.gz.sha256

  # Optional: verify the GPG signature for the downloaded version,
  # the import is only required once
  curl -LO https://download.znuny.org/znuny-release-key.asc
  gpg --import znuny-release-key.asc
  curl -LO https://download.znuny.org/releases/znuny-7.5.1.tar.gz.asc
  gpg --verify znuny-7.5.1.tar.gz.asc znuny-7.5.1.tar.gz

  # Extract
  tar xfz znuny-7.5.1.tar.gz

  # Set permissions
  /opt/znuny-7.5.1/bin/znuny.SetPermissions.pl

  # Restore Kernel/Config.pm, articles, etc.
  cp -a /opt/znuny/Kernel/Config.pm /opt/znuny-7.5.1/Kernel/
  mv /opt/znuny/var/article/* /opt/znuny-7.5.1/var/article/

  # Restore dotfiles from the homedir to the new directory
  for f in $(find -L /opt/znuny -maxdepth 1 -type f -name .\* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.5.1/; done

  # Restore modified and custom cron job
  for f in $(find -L /opt/znuny/var/cron -maxdepth 1 -type f -name \* -not -name \*.dist); do cp -av "$f" /opt/znuny-7.5.1/var/cron/; done

  # Create/overwrite a symlink
  ln -snf /opt/znuny-7.5.1 /opt/znuny

  # Check for missing modules and add **required** modules
  /opt/znuny/bin/znuny.CheckModules.pl --all

..

Execute the migration script
****************************

.. code-block:: shell

    su -c 'scripts/MigrateToZnuny7_5.pl --verbose' - znuny

..

If the migration script fails check the error and try to fix it. Do **not** continue until the migration scripts returns "Migration completed!"

Reinstall or Upgrade Add-ons (Packages)
***************************************
	
.. note:: UpgradeAll can fail, if repositories are not reachable or configured, versions for your framework are not available, or packages have been renamed. In this case, you should upgarde your packages manually via the commandline or by installing/updating them via the package manager.

.. code-block:: shell

    # Make sure all add-ons are correct installed after a patch level update
    su -c 'scripts/MigrateToZnuny7_5.pl --verbose' - znuny
    su -c 'bin/znuny.Console.pl Admin::Package::ReinstallAll' - znuny
    # Upgrade all packages
    su -c 'bin/znuny.Console.pl Admin::Package::UpgradeAll' - znuny
    su -c 'scripts/MigrateToZnuny7_5.pl --verbose' - znuny
    

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
