Manage User Access
##################
.. _PageNavigation admin_usermanagemnt_index

Managing access to the system with modules found in the system administration.

The comes ready to use with built-in user management. Data sources can differ, but the software is ready-to-run.

Types Of Access
***************

There are different types of users in the software.These are divided into:

* Customer Users And 
* Agent Users

Each user type has their own individual interface

+--------------------+----------------------------------+
| User Type          | interface                        |
+====================+==================================+
| User (a.k.a agent) | Agent Interface (index.pl)       |
+--------------------+----------------------------------+
| Customer User      | Customer Interface (customer.pl) |
+--------------------+----------------------------------+

User type sources are individually configurable. Depending on your system configuration you may be able to edit users, customer users, and their information, or only read such.

Supported Backends
******************

Authentication Backend
======================

For user authentication the system can use the following sources:

* Database 
* Directory Service
* HTTP Basic Authentication (the basis for Singe-Sign-On)
* Radius server
  
Data Source
===========

For maintainability it's easier to use the Active Directory or other directory service for maintaining your data.

* Database
* Directory Service

.. note::

    Synchronization of agent user data is possible but the data source is always a database table.

    Customer user synchronization is not currently supported.

User Access Diagram
===================

Here's an example access concept.

.. mermaid::

    graph TD
    user(Logged in User)
    user --> role1(Role One)
    user --> role2(Role Two)
    role2 --> group1(Group One)
    role1 --> group2(Group Two)
    group1 --> permissions_rw
    group2 --> permissions_owner
    group2 --> permissions_ro
    group2 --> permissions_note
    role1 --> group3(Group Three)
    group3 --> permissions_ro
    group3 --> permissions_priority

A general rule is that a group is a resource, and a role provides permissions to a resource.

In the rest of this chapter we will discuss how to use groups and rolls to manage access to different parts of the system and to create teams.

.. toctree::
   :maxdepth: 2
   
   groups/index
   roles/index
   users/index
   customer_users/index
   user_backends/index
