Administrator Interface
#######################

Administrating an instance requires a bit of experience and understanding of how the administration area works and how modules are interconnected.

As an administrator you will need to be able to 

* Create And Manage Queues
* Add And Manage Email Addresses And Accounts
* Filter Emails
* Perform Automated Tasks
* Add, Expand, Maintain Processes
* Add and Maintain Web Services
* Manage Users, Customers, And Customer Users
* Manage Roles, Permissions (Groups), And Access (ACLs).
* Activate And Deactivate Features
* Maintain And Read Logs

In the following chapters all of the required modules for this work are outlined.

The general rules are:

* A role has permissions to modules and queues.
* A queue requires a group, working calendar and an email address.
* A queue contains tickets.
* Modules allow users to access tickets and features.
* Modules can be affected by ACLs or role permissions.
* Processes are specially designed and have built-in automation.
* E-mails can be received in multiple ways and dispatch by recipient, queue, filter, or generic agent.
* Cases can be created by e-mail, phone and web, or generic interface.
* Configuring a module or feature is done centrally in the system configuration.


.. toctree::
   :maxdepth: 2

   usermanagement/index
   queues/index
   servicemanagement/index
   communication/index
   authentication/index
   email/index
   security/index
   dynamicfields/index
   ticketattributerelations/index
   automation/index
   processmanagement/index
   webservices/index
   packagemanagement/index
   systemconfiguration/index

