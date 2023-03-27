.. _TransitionAction TicketCustomerSet:

Set a Ticket Customer
#####################

Summary
********

With this module you can set the customer user of a ticket.

The name of the transition action is :ref:`TicketCustomerSet <TransitionAction TicketCustomerSet>`

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+----------------+-----------------+-----------------------+-----------------------------------------+
| Key            | Example Value   | Description           | Mandatory                               |
+================+=================+=======================+=========================================+
| CustomerID     | client123       | A valid customer      | yes, or CustomerUserID                  |
+----------------+-----------------+-----------------------+-----------------------------------------+
| CustomerUserID | client-user-123 | A valid customer user | no                                      |
+----------------+-----------------+-----------------------+-----------------------------------------+
| No             | client123       | A valid customer      | no, alternative to CustomerID           |
+----------------+-----------------+-----------------------+-----------------------------------------+
| User           | client-user-123 | A valid customer user | no, alternate to CustomerUserID         |
+----------------+-----------------+-----------------------+-----------------------------------------+
| UserID         | 123             | A valid user id       | no, will override the logged in user id |
+----------------+-----------------+-----------------------+-----------------------------------------+
