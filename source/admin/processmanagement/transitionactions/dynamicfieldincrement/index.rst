.. _TransitionAction DynamicFieldIncrement:

Incrementing a Dynamic Field Value
##################################

Summary
********

Use this action to increase or decrease a numerical value saved to a text field.

The name of the transition action is :ref:`DynamicFieldIncrement <TransitionAction DynamicFieldIncrement>`.

.. note::

   This transition action is designed for fields of the type Text. Don't expect a valid result when using a dropdown, for example.

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

.. note:: 

   The key is the name of the field. The `DynamicField_` prefix is not required.

+--------------+---------------+-----------------------------------------+-----------+
| Key          | Example value | Description                             | Mandatory |
+==============+===============+=========================================+===========+
|| FieldName   || 1            || Identinfies field for change           || yes      |
||             ||              || One field is mandatory.                ||          |
+--------------+---------------+-----------------------------------------+-----------+
|| SecondField || 1            || Identinfies field for change           || no       |
||             ||              || Additional fields are optional         ||          |
+--------------+---------------+-----------------------------------------+-----------+
|| ThirdField  || 1            || Identinfies field for change           || no       |
||             ||              || Additional fields are optional         ||          |
+--------------+---------------+-----------------------------------------+-----------+
|| Value       || 5            || Amount to change. ex 5 or -5           || no       |
||             ||              || Default value 1 if not set.            ||          |
+--------------+---------------+-----------------------------------------+-----------+
| UserID       | 123           | no, will override the logged in user id | no        |
+--------------+---------------+-----------------------------------------+-----------+
