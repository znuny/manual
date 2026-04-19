.. meta::
   :description: Use the ExecuteInvoker transition action in Znuny to trigger a web service invoker from a process — supports synchronous and asynchronous execution via the Daemon.
   :keywords: executeinvoker, znuny transition action, web service invoker, process invoker, asynchronous invoker, daemon, znuny webservice

.. _TransitionAction ExecuteInvoker:

Invoke a Web Service
#####################

Summary
*******

Use this transition action to set trigger a web service invoker. This will allow the software to consume a web service an work with any response during a trasition.

The name of the transition action is :ref:`ExecuteInvoker <TransitionAction ExecuteInvoker>`

Transition Action Module Configuration
**************************************

The following list shows the mandatory items.

+--------------+---------------+-------------------------------------------------+-----------+
| Key          | Example value | Description                                     | Mandatory |
+==============+===============+=================================================+===========+
| Webservice   | Coffeemaker   | Name of web service                             | yes       |
+--------------+---------------+-------------------------------------------------+-----------+
| Invoker      | PowerOn       | Name of invoker                                 | yes       |
+--------------+---------------+-------------------------------------------------+-----------+
| Asynchronous | 1             | 0 or 1 possible for Synchronous or Asynchronous | no        |
+--------------+---------------+-------------------------------------------------+-----------+

.. tip:: Asynchronous execution is recommended but needs a running Daemon.


