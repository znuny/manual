.. meta::
   :description: Use the DynamicFieldPendingTimeSet transition action in Znuny to set ticket pending time relative to a date/time dynamic field with an optional offset and target state.
   :keywords: dynamicfieldpendingtimeset, znuny transition action, pending time, pending auto close, date offset, ticket pending, process pending

.. _TransitionAction DynamicFieldPendingTimeSet:

Set a Pending Time
###################

Summary
*******

Use this module to set the pending time of a ticket.

The name of the transition action is :ref:`DynamicFieldPendingTimeSet <TransitionAction DynamicFieldPendingTimeSet>` 

.. note:: Example Results

   The screenshot depicts setting the state to pending auto close+ two days after the date set in "DeliverDate".


Transition Action Module Configuration
**************************************

+--------------+---------------+-----------------------------------------------------+-----------+
| Key          | Example value | Description                                         | Mandatory |
+==============+===============+=====================================================+===========+
| DynamicField | DeliveryDate  | Name of the dynamic field                           | Yes       |
+--------------+---------------+-----------------------------------------------------+-----------+
| Offset       | 2d            | Optional string with offset                         | No        |
+--------------+---------------+-----------------------------------------------------+-----------+
| State        | 1             | Any state of the type pending auto/pending reminder | No        |
+--------------+---------------+-----------------------------------------------------+-----------+


.. important:: Dynamic Field

   The field must be a ``Ticket`` field of type ``Date`` or ``DateTime``.


Offset Options
==============

An additional offset can be added to the date. The offset is a string with numbers and units. The units are:

* d - days
* h - hours
* m - minutes
* s - seconds

Offset Examples
~~~~~~~~~~~~~~~

* 1d 2h 3m 40s
* 20h 13m
