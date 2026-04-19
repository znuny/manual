.. meta::
   :description: Organize Znuny process tickets with categories — configure ProcessPreferences settings, enable the agent module and deactivate the customer frontend feature.
   :keywords: process ticket categories, znuny process management, process grouping, processpreferences, agent ticket process category, customer process category

.. _Pagenavigation admin_processmanagement_categories:

Process Ticket Categories
#########################

This section provides an overview of how to manage process ticket categories within the admin interface. Categories help organize tickets and streamline the process management workflow. The system configuration allows for the creation, editing, and deletion of categories.

Modifying Categories
********************

To modify existing categories, follow these steps:

1. Navigate to the **System Configuration** section in the admin interface.
2. Search for **ProcessPreferences###001-TicketProcessCategory-Category** to modify the category settings.
3. Click on **Edit this setting**.
4. Adjust the category names as needed. You can add new categories or modify existing ones.
5. Save your changes to apply the new category settings.

Per process, the category can now be set. :ref:`pagenavigation processmanagement_createprocess` provides details on how to create a new process and assign categories to it.

Deactivate Feature
******************

By disabling the module ``CustomerFrontend::Module###CustomerTicketProcessCategory``, the feature for process ticket categories will be deactivated. This means that the system will no longer display or utilize the process ticket categories in the customer frontend.

Activate for Agents
*******************

Enable the following modules to allow agents to start and filter process ticket categories:

* ``Frontend::Module###AgentTicketProcessCategory``
* ``Frontend::Navigation###AgentTicketProcessCategory###001-ProcessManagement``

