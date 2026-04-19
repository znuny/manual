.. meta::
   :description: Running Znuny with multiple frontend servers — pros and cons of high-availability topologies for performance, redundancy, scalability, sessions and disaster recovery.
   :keywords: znuny high availability, ha setup, multiple frontend servers, load balancer, failover, znuny scalability, redis sessions

.. _PageNavigation concepts_ha_index:

Using Multiple Frontend Servers
###############################

In the chase for high available solutions, one issue is the performance benefit and availability of multiple frontend servers.
It is possible to run multiple front-end nodes native. All other requirements are not covered here. 

Pros and Cons of HA (General)
*****************************

+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Category**                 | **Pros**                                                             | **Cons**                                                                                        |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Performance**              | - Load distribution improves response times.                         | - Higher resource consumption (CPU, RAM, DB load).                                              |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Redundancy & Reliability** | - Prevents downtime with failover mechanisms.                        | - Complexity in setting up redundancy mechanisms.                                               |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Scalability**              | - Easier to handle increasing user requests.                         | - More servers mean higher licensing and maintenance costs.                                     |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Session Management**       | - Ensures uninterrupted user experience in distributed environments. | - Requires additional session management (Redis, database-backed sessions, or sticky sessions). |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Database Load**            | - Offloads frontend tasks, improving database performance.           | - Requires database replication and connection pooling to avoid bottlenecks.                    |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Disaster Recovery**        | - Redundant servers can take over if one fails.                      | - Needs real-time monitoring and automated failover, which can be costly.                       |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Infrastructure Cost**      | - Avoids major revenue losses from downtime.                         | - More hardware/cloud instances increase operating expenses.                                    |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Maintenance & Complexity** | - Easier to perform rolling updates without downtime.                | - More components = more maintenance, troubleshooting, and monitoring.                          |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Network Considerations**   | - HA proxies (Nginx, HAProxy, Load Balancers) optimize traffic.      | - Load balancer failure can become a single point of failure if not replicated.                 |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| **Security**                 | - Redundant firewalls and authentication systems improve security.   | - More entry points mean increased attack vectors if not properly secured.                      |
+------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+


HA Basics
*********

.. note::

    Main reason for the lack of "guides", is that this is pretty complicated with any software and overkill for the most setups. 

To do this the properly you need at least:

- 2 Application Servers
- a shared caching server Redis/Memcached server
- a database server
- a shared storage
- a load balancer
- a monitoring setup

This is a minimum. (More is better, but complexity will increase)

Setup Application Severs
************************

1. Prepare the database server
2. Prepare two znuny as application servers and a third znuny for the management tasks.
3. Connect all to the same database source.

.. note:: 
    
    Install each server as a standalone instance, as if it would only run for itself.

3. Establish a shared cache. There are some modules out there. Redis and Memcached should be easy to find.
4. Configure the systems to save attachments to the file system, not the database, as a synchronization between the database nodes will affect your performance. This will require a shared location such as an NFS
5. Start the Daemon on all instances.

.. note:: 

    The load balancer can work as you need it to, by load of the app server, by geo location... as you want.

Keeping in synchronization
**************************

.. note::

  System Configurations, ACLs, Processes are created in the GUI, stored in the DB and written to the file system. These must be automatically or manually synchronized.

Other Considerations
======================

1. Cache Redis/Memcached

.. important::
    
    A special module is needed for that (Available with Znuny support).

2. Config.pm (Host specific configs)

.. note::

    Each Config.pm using the ``NodeID`` setting, with it's own node number. The Management server should be **1**.

3. Packages should be installed only on the management server and all other administration front-ends should be deactivated
    
.. note:: 

    The Console command is recommended for reinstall packages locally on the application servers, after Installing updating the addon on the management server, as it reinstalls from the database.

.. important:: 

    It's recommended to deactivate the system configuration on all app servers, and just keep it on the management server.

4. Any administration tasks should be performed only on the administration server.

Issues and troubleshooting
**************************

The configuration and setup, outside the above loose recommendations, is where you should seek help from professionals in the community, or for more assistance info@znuny.com.
