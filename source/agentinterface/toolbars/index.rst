User Toolbars
#############

User toolbars appear in the navigation area, if configured, and give users quick access to filtered overviews.

Additionally, some toolbars are quick access items to create objects.

Lastly, there is also system views which can appear in the toolbar area.

.. note:: 
    
    Toolbars can also be included in many add-on features like FAQ or ITSM packages.

.. image:: images/user_toolbars.png
   :alt:  Toolbar image


Overviews
*********

.. table::
  :widths: 6

  +-------------------+-----------------+
  | :fa:`exclamation` | Escalation View |
  +-------------------+-----------------+
  | :fa:`list-ol`     | Status View     |
  +-------------------+-----------------+
  | :fa:`folder`      | Queue View      |
  +-------------------+-----------------+
  | :fa:`wrench`      | Service View    |
  +-------------------+-----------------+
  | :fa:`comment`     | Mention View    |
  +-------------------+-----------------+

Personal Views
**************

The user toolbars include:

.. table::
  :widths: 6

  +-----------------+---------------------+
  | :fa:`user`      | Owned Tickets       |
  +-----------------+---------------------+
  | :fa:`lock`      | Locked Tickets      |
  +-----------------+---------------------+
  | :fa:`user-plus` | Responsible Tickets |
  +-----------------+---------------------+
  | :fa:`eye`       | Watched Tickets     |
  +-----------------+---------------------+



Actions
*******

The quick access icons include

.. table::
  :widths: 6

  +----------------+--------------------+
  | :fa:`phone`    | New Phone Ticket   |
  +----------------+--------------------+
  | :fa:`envelope` | New Email Ticket   |
  +----------------+--------------------+
  | :fa:`sitemap`  | New Process Ticket |
  +----------------+--------------------+


Search Toolbars
***************

There are several search toolbars available for use and these can be configured in the system configuration area.


Ticket Search Profile
  If ``Frontend::ToolBarModule###210-Ticket::TicketSearchProfile`` is enabled, then saved profiles will be selectable directly in the toolbar.

Full Text Ticket Search
  If ``Frontend::ToolBarModule###220-Ticket::TicketSearchFulltext`` is enabled then the entire ticket (excluding attachments and dynamic fields) will be searched.

.. versionadded:: 6.4.3

  Additional configuration can be added to limit the search to ticket of specific attributes, by the system administrator. Most any attribute of type STRING can be configured to limit the results of the search.

Customer Search
  If ``Frontend::ToolBarModule###230-CICSearchCustomerID`` is enabled, you may search for a customer, and access the customer information center directly.

Customer User Search
  If ``Frontend::ToolBarModule###230-CICSearchCustomerUser`` is enabled, you may search for a customer user, and access the customer user information center directly.
