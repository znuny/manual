.. meta::
   :description: Manage Znuny customers and customer users — add organizations and contacts, choose writeable backends, map data sources and control customer user visibility.
   :keywords: znuny customer users, customer organization, customer user management, writeable backend, customer id, contact management, customer admin

.. _PageNavigation admin_usermanagement_customer_users_index:

Customers and Customer Users
############################

Customer users belong to a customer (organization, department, etc.). A customer is required before any customer user can be added.

Adding a Customer
*****************

Navigate to the administration menu, and click on the badge:

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
   :alt: Selection of admin_customer_datasource

Add a Customer User
*******************

After adding a customer as shown above, you may then choose to add a customer user.

Navigate to the administration menu, and click on the badge:

.. image:: images/admin_customer_user.png
   :alt: Admin Badge Customer User

Depending on the configuration of custom user data mapping, your form for entering customer user data may differ. Here is an example of the default user form.

.. image:: images/admin_customer_user_add.png
   :alt: Admin Customer User Add

.. seealso::

   :ref:`Add a Customer User as an Agent <PageNavigation agentinterface_dashboards_index>`

.. seealso::

   - More on customers in our concepts chapter :ref:`pagenavigation concepts_customers_index`
   - To assign a customer user to additional companies: :ref:`Customer Users ↔ Customers <PageNavigation admin_usermanagement_customer_user_customer_index>`