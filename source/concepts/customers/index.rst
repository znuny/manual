.. meta::
   :description: Customers and Customer Users in Znuny — how organizational entities relate to individual end-users who submit tickets and access the self-service customer portal.
   :keywords: znuny customer, customer user, customer entity, end user, customer portal, customer relationship

.. _PageNavigation concepts_customers_index:

Customers and Customer Users
############################

In **Znuny**, the concepts of **Customers** and **Customer Users** are structured to manage external users efficiently. Here's how these terms differ:

Customer
********

A **Customer** represents an **organizational entity**—a company, business unit, or institution that interacts with your service or support team. 
Customers are the **top-level entities** that contain customer users.

- Example: A company like **"Acme Corporation"** would be a **Customer**.
- Customers do not log into Znuny directly but serve as a reference for associated customer users.

Customer User
*************

A **Customer User** is an **individual person** who belongs to a **Customer** and interacts with your service or support system. 
They are the **end-users** who submit tickets, request support, and have access the customer portal.

- Example: **John Doe (john.doe@acme.com)** is a **Customer User** under the **Acme Corporation** Customer.

.. important:: 

    It is possible to associate a customer with multiple customers, using the Customer User <=> Customers module.

    .. seealso:: 

       :ref:`PageNavigation admin_usermanagement_customer_users_index`


Key Relationships Between Customers and Customer Users
*******************************************************

- A **Customer** can have **multiple Customer Users** (e.g., all employees of Acme Corporation).
- A **Customer User** belongs to only **one Customer**.
- Customer Users can log in to the Znuny **Customer Interface** to manage their tickets.

Usage in Znuny
**************

- **Customer-based ticketing**: When a customer user submits a ticket, Znuny associates it automatically with their respective customer.
- **Access Control**: Customer users can see tickets within their own company.
- **Reporting & SLAs**: Service levels can be applied at the Customer level to manage contract-based support.


Related Content
***************

:ref:`pagenavigation admin_usermanagement_customer_users_index`
