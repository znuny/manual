.. meta::
   :description: Manage Znuny customers and customer users — add organizations and contacts, choose writeable backends, map data sources and control customer user visibility.
   :keywords: znuny customer users, customer organization, customer user management, writeable backend, customer id, contact management, customer admin

.. _PageNavigation usermangement_customer_users_index:

Customers and Customer Users
############################

Customer users belong to a customer (organization, department, etc.). A customer is required before any customer user can be added.

Adding A Customer
*****************

Navigate to the administration menu, and clicking on the badge:

.. image:: images/admin_customer.png
    :alt: Admin Badge Customer

A customer record requires:

* Customer ID
* Customer Name

All other information is optional, as configured by your administrator. 

.. image:: images/admin_edit_customer.png
    :alt: Admin Edit Customer


If multiple writeable backends are available, choose the backend before clicking **Add Customer**.

.. image:: images/admin_customer_datasource.gif
    :alt: Selection Of admin_customer_datasource

Add A Customer User
*******************

After adding customers seen above you may then choose to add a customer user.

Navigate to the administration menu, and clicking on the badge:

.. image:: images/admin_customer_user.png
    :alt: Admin Badge Customer User

Depending on the configuration of custom user data mapping your form for entering customer user data may differ. Here is the example of the default user form.

.. image:: images/admin_customer_user_add.png
    :alt: Admin Customer User Add

.. seealso:: 

    :ref:`Add A Customer User As An Agent <PageNavigation agentinterface_dashboards_index>`

.. seealso::

   - More on customers in our concepts chapter :ref:`pagenavigation concepts_customers_index`
   - To assign a customer user to additional companies: :ref:`Customer Users ↔ Customers <PageNavigation admin_usermanagement_customer_user_customer_index>`