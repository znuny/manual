New Features
############
 
Znuny 6.3 has :ref:`new integrated features <Integrated features 6_3>`. These features were previously only available to Znuny commercial support users. We've now made them part of the framework.

List of integrated features:

* Znuny4OTRS-CalendarBasedTicketCreation
* Znuny4OTRS-ExcelStats
* Znuny4OTRS-AdvancedTimeUnit
* Znuny4OTRS-OAuth2TokenManagement
* Znuny4OTRS-MailAccounts
* Znuny4OTRS-RandomTicketNumberGenerator
* Znuny4OTRS-AdvancedBulkAction

Integrated Packages
*******************
.. _Integrated features 6_3:
 
.. note::

    If your setup depends on those add-ons, please note that you can remove them from your dependencies if you target 6.3.


- :ref:`Znuny4OTRS-CalendarBasedTicketCreation <Znuny4OTRS-CalendarBasedTicketCreation>`


Schedule Ticket Creation 
========================
.. _Znuny4OTRS-CalendarBasedTicketCreation:


Functionality
~~~~~~~~~~~~~

Use calendar entries to create tickets. Making calls and requests count! Keeping up with contacts by sending follow-up notes after a call, creating a
task list for a project kick-off or scheduling maintenance has never been easier. 

Use recurring tasks to:

* create jobs for patch days
* schedule a protocol for regular meetings
* remind about marketing deadlines
* schedule maintenance for your company car-fleet

Whatever you need to schedule, create an appointment to keep you on task.

More details can be found in :doc:`../../agentinterface/calendarscreens/appointments/index`.

Bulk Service and Dynamic Field Changes
=======================================

It is now possible to modify services and dynamic fields for multiple ticket during a bulk action change.

:ref:`Read More <Znuny4OTRS-AdvancedBulkAction>`

Advanced Excel Formatting
=========================

.. _Integrated AdvancedFormatting:

It is now possible to finely tune the format of an Excel Workbook produced by the statistic module.

:ref:`Read more <AdvancedFeatures excel-stat-formatting>`

Random Ticket Numbers
=====================

The ((OTRS)) Community Edition removed random ticket numbers. Znuny4OTRS-RandomTicketNumberGenerator brought this back. This feature is now back to the framework.

You can use this by changing ``Ticket::NumberGenerator`` to ``Kernel::System::Ticket::Number::Random'``.

.. warning:: 
    
    Never do this in a running system. Old ticket numbers will no longer receive responses.

Using the random number generator produces an ten-digit number plus the System ID.

**Example:** 370123489759

+----------+--------------------------------+
| SystemID | Random Available Ticket Number |
+==========+================================+
| 37       | 0123489759                     |
+----------+--------------------------------+
    

New Software Requirements
*************************

The following Perl modules will be required by :ref:`advanced formatting <Integrated AdvancedFormatting>`:

* Hash::Merge
* Excel::Writer::XLSX


OAuth2 Token Management
=======================

It is now possible to configure and refresh OAuth2 tokens in the administration area.

(:ref:`Read more <PageNavigation authenticate_token_index>`) about how to manage tokens.

OAuth2 Email Authentication
============================

It is now possible to use OAuth2 tokens instead of a password to fetch emails. This currently works and is tested on Google and Microsoft. Once you have a valid token, read :ref:`how to select it <PageNavigation email_postmaster_mail_account>` when setting up your PostMaster Mail Account.

Contributed Features
********************

Thanks to Sector Nord AG for the following transition actions.

* :ref:`Update an appointment <TransitionAction AppointmentUpdate>`.
* :ref:`Remove an appointment <TransitionAction AppointmentRemove>`.

New Features
************

With this release, we also introduced some completely new features.

Process Part Scope
==================

In process management, it has always been an issue that all process parts (Activities, Activity Dialogs, Transitions, and Transition Actions) are visible in each process.

It is now possible to view process parts globally or locally.

.. important::

    Scopes are not migrated. This means you must define all elements to limit them to a scope to use the filter functionality. Until this, all element parts are global.

Read more on :ref:`process scope <ProcessManagement ProcessScope>`.
