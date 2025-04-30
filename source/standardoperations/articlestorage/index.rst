.. _PageNavigation standardoperations_articlestorage_index:

Article Storage
###############

Znuny stores the article data in one of two locations

- Database (ArticleStorageDB - Default)
- Filesystem (ArticleStorageFS)

In smaller and new systems, the database will be the preferred location due to speed, flexibility, ease of use and backup purposes.
As time and usage progresses, you may decide to change to the file system.

Migrate to the Filesystem
*************************

1. Verify Current Storage Configuration:

- Navigate to Admin -> SysConfig.
- Search for ``Ticket::Article::Backend::MIMEBase::ArticleStorage``.
- Check if it's set to **ArticleStorageDB** (database storage) or **ArticleStorageFS** (file system storage).
  - If you want to permanently change this, you can. Otherwise, afterward, the attachments will be divided across backends. In this case:
- Activate ``Ticket::Article::Backend::MIMEBase::CheckAllStorageBackends``, to run in mixed mode.
  
2. Prepare for Migration:
 
- Verify Directory: The location where Znuny will save the articles can be found in ``Ticket::Article::Backend::MIMEBase::ArticleDataDir``
- Backup Your Data: Ensure you have a complete backup of both your database and file system.
- Check Permissions: Confirm that the web server user has appropriate read and write permissions to the target storage directory. It's recommended that the web server runs under the 'znuny' user to avoid permission issues.
  
3. Execute the Storage Switch:

- Open a terminal on your Znuny server.
- Navigate to the Znuny installation directory (commonly /opt/znuny).
- | Run the following command to migrates all articles from the database to the file system:
  | ``bin/znuny.Console.pl Admin::Article::StorageSwitch --target ArticleStorageFS``

4. Post-Migration Steps:
   
- Verify Migration: Ensure that articles and attachments are accessible and correctly served from the new storage backend.

5. Address Potential Issues:
   
- Permission Issues: Ensure that both the Znuny application and the web server have the necessary permissions to read and write to the new storage location.
- | Skipping Problematic Articles: If certain articles cause errors during migration, you can use the --tolerant option to continue the process despite errors:
  | ``bin/znuny.Console.pl Admin::Article::StorageSwitch --target ArticleStorageFS --tolerant``

Partial Migration
*****************

It is possible to migrate part of the data, and run in mixed mode.

1. Activate ``Ticket::Article::Backend::MIMEBase::CheckAllStorageBackends``, to run in mixed mode.
2. Run a partial migration using the console command options to migrate based on the time options.
   
.. code-block:: shell

 [--tickets-closed-before-date ...] - Only process tickets closed before given ISO date.
 [--tickets-closed-before-days ...] - Only process tickets closed more than ... days ago.
 [--tickets-created-before-date ...] - Only process tickets created before given ISO date.
 [--tickets-created-before-days ...] - Only process tickets created more than ... days ago.


Performance Issues
******************

To run the migration during live operations, use the ``--micro-sleep`` options.

.. code-block:: 
    
    [--micro-sleep ...]            - Specify microseconds to sleep after every ticket to reduce system load (e.g. 1000).

File Structure
**************

The attachments are stored logically on the file system in the following way

``$ArticleDataDir/YYYY/MM/DD/ArticleID/``

The following file may be found.

**plain.txt**
    The raw email message

**file-1**
    The plain message part

**file-2**
    The HTML message part

**name.disposition**
    The MIME part disposition

**name.content_type**
    The MIME part content_type

**name.content_id**
    The MIME part content_id

**name.content_alternative**
    The MIME part content_alternative
