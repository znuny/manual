Agent Dashboards
################

.. _PageNavigation agentinterface_dashboards_index:



Agent Dashboard
***************

The first view an agent has is the dashboard. On the dashboard, there are widgets which can be configured individually for each user.


.. image:: images/full_dashboard.png
    :alt: Full Dashboard Image

Widgets can be rearranged by dragging and dropping using the widget title. There are large (left) and small (right) widgets.

.. note::

    Widgets may only be moved top to bottom, not left to right.

Dashboard Focus
===============

.. versionadded:: 7.0
   Dashboard Focus


.. image:: images/dashlet_focus.png
   :alt:  Dashboard Buttons Image


It is possible to focus on just one dashboard module, by clicking on one of the dashboard module names at the top.


Widget Settings
===============

A :fa:`cog` and :fa:`times` appears at the top right-hand side of each widget. The :fa:`times` removes the widget, and the :fa:`gear` takes you to the settings page. Settings are different per module.

You may see some or all of the default modules as configured. Here is a list of the default widgets available and their purpose.

Widgets can be activated or deactivated by opening the settings on the top right-hand side of the screen.

.. image:: images/widget_settings.gif
    :alt: Widget Settings Screen Image

Widget filters
==============

Each widget has filters to help reduce the content to a relevant scope.

My locked tickets
    Tickets I've locked to my user
My responsible tickets
    Tickets for which I'm responsible
Tickets in My Queues
    Tickets in my selected queues
Tickets in My Services
    Tickets in my selected services
All tickets
    All tickets that match the filter criteria


Large Dashboard Widgets
=======================

Reminder Tickets
    A list of tickets that have reached their reminder time
Escalated Tickets
    Tickets with a breached SLA
Open Tickets
    Tickets that are in an open state
New Tickets
    New tickets which have no agent interaction
Running Process Tickets
    Process tickets active in the system.
Ticket Queue Overview
    A count of all tickets and their states in the system
Events Ticket Calendar
    A small calendar showing tickets having a start and end date for an event

Small Dashboard Widgets
=======================

7-Day Stats
    A line chart showing the tickets created and closed per day for the last 7 days
Upcoming Events
    A list of tickets reaching their reminder time or breaching their SLA soon
Logged-In agents
    A list of agents and their session status (active/inactive)
News
    An RSS feed
Appointments
    Shows upcoming events and allows for creating an event from the dashboard


Customer Information Center
***************************

The **Customer Information Center** gives you access to all customer user data and tickets for an individual customer. 

.. image:: images/customer_information_center_overview.png
    :alt: Customer User Information Center Image

A user can create tickets for our customer user directly from this screen and additionally add customer users to the customer via this screen.

Adding a customer user redirects the normal agent to the administration section of the software without having to have administrator access.

When using the add a customer feature the CustomerID will automatically be pre-populated.

.. seealso::

    Read more in :ref:`Manage Customers <PageNavigation usermangement_customer_users_index>`.
