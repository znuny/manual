System Permissions
##################
.. _PageNavigation annexes_permissions:

Permissions are used to access queues and modules. There are seven basic permissions in the system.

Default Permissions
*******************

+-------------+---------------------------------------------------------------+
| Permissions | Description                                                   |
+=============+===============================================================+
| ro          | User can read tickets or use a module.                        |
+-------------+---------------------------------------------------------------+
| create      | User can create a ticket in a queue.                          |
+-------------+---------------------------------------------------------------+
| move_into   | User can move a ticket into the queue.                        |
+-------------+---------------------------------------------------------------+
| note        | User can add a note to a ticket.                              |
+-------------+---------------------------------------------------------------+
| owner       | User can assign the owership or become the owner of a ticket. |
+-------------+---------------------------------------------------------------+
| priority    | User can change the priority of a ticket.                     |
+-------------+---------------------------------------------------------------+
| rw          | User has full access to a queue module.                       |
+-------------+---------------------------------------------------------------+

Extended Permissions
********************

There are some special pre-configured permissions which, when added, can be used to further limit access to modules.

+-------------+--------------------------------+
| Permissions | Description                    |
+=============+================================+
| phone       | Access to phone screens.       |
+-------------+--------------------------------+
| close       | Access to the close screen.    |
+-------------+--------------------------------+
| pending     | Access to the pending screen.  |
+-------------+--------------------------------+
| bounce      | Access to the bounce screen.   |
+-------------+--------------------------------+
| forward     | Access to the forward screen.  |
+-------------+--------------------------------+
| compose     | Access to the compose screen.  |
+-------------+--------------------------------+
| customer    | Access to the customer screen. |
+-------------+--------------------------------+

.. note::

    If a permission is configured, but not applied, it will be ignored. This means, until you implement the special permissions, the permissions will not be applied.

To activate these, use the system configuration option.

``Core::Permission``
