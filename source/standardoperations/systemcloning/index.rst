.. meta::
   :description: Clone a Znuny production system into staging or dev safely — disable outbound email, customer access and integrations, and avoid accidental writes to PROD.
   :keywords: znuny system cloning, clone to dev, staging system, disable outbound email, test environment, znuny staging

Cloning a System for Staging or Development
###########################################

**Scope**

This document describes safety precautions, procedures, and best practices for cloning a productive Znuny system into a test or development environment.

**Objectives**

When cloning PROD → TEST/DEV, the primary goals are preventing:

* outbound email
* customer access
* productive integrations (REST, SMTP, IMAP, POP3)
* accidental connection to PROD database

Additionally, the cloned system should: 

* Be clearly mark system as non-production
* Have an isolated filesystem and database
* Avoid corruption of productive data

Pre-Clone Preparation (Production System)
*****************************************

* Freeze System State
* Stop daemon and background jobs:

.. code-block:: bash

   bin/znuny.Daemon.pl stop \
   bin/Cron.sh stop \
   systemctl disable --now cron postfix apache2

Create Full Backup
==================

- Database dump
- Kernel/Config.pm
- ``var/article`` (or storage directory see ``Ticket::Article::Backend::MIMEBase::ArticleDataDir``)
- Non-packaged Custom images, skins, and modules
- Cron configuration ``var/cron/`` not in ``aaa_base`` or ``znuny_daemon``
- Web server configuration

Clone Procedure
===============

Prepare Self-contained Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create a new VM, container or bare-metal with:
- Base OS installed (e.g. Debian, Ubuntu, CentOS)
- Znuny application files (e.g. /opt/znuny)
- Dedicated local database instance (e.g. MySQL, PostgreSQL)
- Web server configured for Znuny
- Separate hostname (e.g. znuny-dev.example.local)
- Separate IP address
- Separate filesystem (no shared mounts with PROD)
- Separate database instance (never reuse PROD DB)
- Separate mail server or disabled mail sending

Clone Database
~~~~~~~~~~~~~~

- Restore dump into new DB instance (Avoid reuse of PROD DBMS)
- Create dedicated DEV DB user

Update the following parameters in ``Kernel/Config.pm``:

.. code-block:: perl

   $Self->{DatabaseHost}
   $Self->{Database}
   $Self->{DatabaseUser}
   $Self->{DatabasePw}

Verify that the DEV system accesses the new database and not PROD.

``bin/znuny.Console.pl Maint::Database::Check``

Restore Settings and Filesystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restore or copy the following directories:

- Restore custom cronjobs ``/opt/znuny/var/cron/`` (not in aaa_base or znuny_daemon)
- Restore custom images, skins, and modules
- ``Kernel/Config.pm``

Mandatory Safety Adjustments (DEV/TEST)
=======================================

Change System Identity
~~~~~~~~~~~~~~~~~~~~~~~

Modify ``Kernel/Config.pm``.

**FQDN**

.. code-block:: perl

   $Self->{FQDN} = 'znuny-dev.example.local';

**CustomerTagLine**

Clearly mark system as non-production:

.. code-block:: perl

   $Self->{'Customer::Frontend::Header::CustomerTagLine'}
       = '*** TEST SYSTEM – NO REAL DATA ***';

**Product Name**

.. code-block:: perl

   $Self->{ProductName} = 'Znuny DEV';

This ensures browser tabs, screenshots, and headers clearly indicate DEV.

Disable Email Sending (CRITICAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``Kernel/Config.pm``:

.. code-block:: perl

   $Self->{SendmailModule} = 'Kernel::System::Email::DoNotSendEmail';

This prevents:

- Ticket notifications
- Escalation alerts
- Auto-responses
- Agent notifications
- GenericAgent email actions

Adjust system_address and mail_account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the database:

- Delete or Modify all entries in ``system_address``
- Delete or Modify all entries in ``mail_account``

.. code-block:: sql

   UPDATE system_address SET valid_id = 2;
   UPDATE mail_account SET valid_id = 2;

Alternatively:

- Replace SMTP server with invalid host
- Remove IMAP/POP credentials

This prevents inbound and outbound mail processing.

Filesystem Synchronization (/opt/znuny/var/article)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If using filesystem article storage:

Ensure correct permissions and ownership:

.. code-block:: bash

   bin/znuny.SetPermissions.pl

Verify:

- No shared NFS mount with production
- No shared object storage
- No shared attachments directory

Never mount the same ``var/article`` storage as PROD.

GenericAgent Cleanup (GA)
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a GenericAgent job in DEV to:

- Delete all tickets
- Remove old customer data
- Clear dynamic field values

This ensures the DEV system starts clean.

Disable External Integrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Disable:**

- REST GenericInterface connectors

Finalization on Cloned System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Reinstall packages:**

.. code-block:: bash

   bin/znuny.Console.pl Maint::Package::ReinstallAll

**Clear cache:**

.. code-block:: bash

   bin/znuny.Console.pl Maint::Cache::Delete

**Start daemon:**

.. code-block:: bash

   bin/znuny.Console.pl Maint::Daemon::Start

**Reenabling Services :**

.. code-block:: bash

   systemctl enable --now cron postfix apache2

Verification Checklist
======================

- FQDN clearly shows DEV
- ProductName indicates DEV
- CustomerTagLine shows warning
- Email sending disabled
- No active mail_account entries
- No active system_address entries
- DEV DB is separate from PROD
- No shared var/article storage
- No REST endpoints pointing to PROD
- Tickets optionally removed
- Daemon running correctly

Best Practices
==============

- Always restrict DEV by IP via web server
- Never allow public DNS entry for DEV
- Never connect DEV to production mail server
- Maintain a documented clone procedure

Golden Rule
===========

A cloned system must:

- Have email disabled
- (optionally) Authenticate against productive identity providers
- Connect only to non-productive databases
- Only use development api endpoints
- Never share filesystem storage with PROD

If any of the above is possible, the clone is unsafe.
