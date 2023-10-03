.. _PageNavigation admin_usermanagement_user_synchronization_index:

Synchronization Options
#######################

In the chapter :ref:`pagenavigation admin_usermangement_user_backends_usersyncbackend_config`, you see the basic setup needed for synchronization of users. If you do not use this, you will possibly be authenticated, but have no user data. In order to prevent this, you should always use the ``#    $Self->{'AuthModule::UseSyncBackend'} = '';`` in your backends, and add which synchronization backend should be used. The basic synchronization is:

- UserLogin
- UserFirstname
- UserLastname

If you desire, you can also map other attributes, or even use plain text elements.

.. note:: Other mappings are sent directly to the user preferences and are not shown in the administration area.

.. warning:: 
    
    Once synchronization is active, if the authenticated user has no roles or groups, then they will have no access to modules and objects in Znuny. A user who is authorized and matches the criteria for synchronization, is always first stripped of role and groups, and reassigned at login. This also means that temporary manual changes will be overwritten when the user login out and in.


Filters and Options
*******************

When synchronizing groups and roles based on LDAP server attributes or security objects. It's important to know that you can use different common options. These common options are: 

Group Restriction
=================

LDAP\:\:GroupDN
    Distinguished name of a group where the user needs to be member to be synchronized.
LDAP\:\:AccessAttr
    Name of the attribut if ``LDAP\:\:GroupDN`` where the members are stored, default is ``memberUID``.
LDAP\:\:UserAttr
    Defines what is value of ``LDAP::GroupDN``, default is ``DN``.

LDAP Filters
============

LDAP\:\:AlwaysFilter
    Only LDAP objects matching this filter are processed, optional setting.

.. important:: 

    An important use of the filter is the application of nested groups (see `Microsoft Documentation <https://learn.microsoft.com/en-us/windows/win32/adsi/search-filter-syntax?redirectedfrom=MSDN>`_ )

Attributes vs. Groups
=====================

LDAP\:\:UserSyncAttribute*Definition
    Use attributes for synchronization purposes.
LDAP\:\:UserSync*Definition
    Use security objects for synchronization purposes.  

Synchronizing Groups
********************

.. important:: 
    
    For both groups and roles, you will need to have pre-defined the groups, and roles, to which you will match.

Synchronization of groups is much less common than synchronization of roles. If you do choose to synchronize your user groups, you can also use a further option when synchronizing them to ensure that the users all have a common set of groups.

LDAP\:\:UserSyncInitialGroups
    Define a list of default groups to which a user should have access. 

**UserSyncGroupsDefinition Example:**

.. code-block:: perl

    # AuthSyncModule::LDAP::UserSyncGroupsDefinition
    # (If "LDAP" was selected for AuthModule and you want to sync LDAP
    # groups to Znuny groups, define the following.)
    #    $Self->{'AuthSyncModule::LDAP::UserSyncGroupsDefinition'} = {
    #        # ldap group
    #        'cn=agent,o=znuny' => {
    #            # znunys group
    #            'admin' => {
    #                # permission
    #                rw => 1,
    #                ro => 1,
    #            },
    #            'faq' => {
    #                rw => 0,
    #                ro => 1,
    #            },
    #        },
    #        'cn=agent2,o=znuny' => {
    #            'users' => {
    #                rw => 1,
    #                ro => 1,
    #            },
    #        }
    #    };

**UserSyncAttributeGroupsDefinition Example:**

.. code-block:: perl

    # AuthSyncModule::LDAP::UserSyncAttributeGroupsDefinition
    # (If "LDAP" was selected for AuthModule and you want to sync LDAP
    # attributes to Znuny groups, define the following.)
    #    $Self->{'AuthSyncModule::LDAP::UserSyncAttributeGroupsDefinition'} = {
    #        # ldap attribute
    #        'LDAPAttribute' => {
    #            # ldap attribute value
    #            'LDAPAttributeValue1' => {
    #                # znuny group
    #                'admin' => {
    #                    # permission
    #                    rw => 1,
    #                    ro => 1,
    #                },
    #                'faq' => {
    #                    rw => 0,
    #                    ro => 1,
    #                },
    #            },
    #        },
    #        'LDAPAttribute2' => {
    #            'LDAPAttributeValue' => {
    #                'users' => {
    #                    rw => 1,
    #                    ro => 1,
    #                },
    #            },
    #         }
    #    };

Synchronizing Roles
*******************

.. important:: 

    For both groups and roles, you will need to have pre-defined the groups, and roles, to which you will match.

**UserSyncRolesDefinition Example:**

.. code-block:: perl

    # AuthSyncModule::LDAP::UserSyncRolesDefinition
    # (If "LDAP" was selected for AuthModule and you want to sync LDAP
    # groups to Znuny roles, define the following.)
    #    $Self->{'AuthSyncModule::LDAP::UserSyncRolesDefinition'} = {
    #        # ldap group
    #        'cn=agent,o=znuny' => {
    #            # znunt role
    #            'role1' => 1,
    #            'role2' => 0,
    #        },
    #        'cn=agent2,o=znuny' => {
    #            'role3' => 1,
    #        }
    #    };

**UserSyncRolesAttributeDefinition Example:**

.. code-block:: perl

    # AuthSyncModule::LDAP::UserSyncAttributeRolesDefinition
    # (If "LDAP" was selected for AuthModule and you want to sync LDAP
    # attributes to Znuny roles, define the following.)
    #    $Self->{'AuthSyncModule::LDAP::UserSyncAttributeRolesDefinition'} = {
    #        # ldap attribute
    #        'LDAPAttribute' => {
    #            # ldap attribute value
    #            'LDAPAttributeValue1' => {
    #                # Znuny role
    #                'role1' => 1,
    #                'role2' => 1,
    #            },
    #        },
    #        'LDAPAttribute2' => {
    #            'LDAPAttributeValue1' => {
    #                'role3' => 1,
    #            },
    #        },
    #    };
