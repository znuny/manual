Manage User Backends
####################
.. _PageNavigation admin_usermanagment_user_backends:

There are different backend types available for configuration all of which are found in the default configuration file ``Kernel/Config/Defaults.pm``. You may have up to 11 of each. Each backend can be used for either authentication or data. These backends are listed, as well as their examples, below. The backends can be also added multiple times by suffixing the appropriate key with a number, the first backend has no suffix.

i.e. AuthBackend1, CustomerUser2, etc.

Authentication Backends
***********************

An agent or customer user can be authenticated via HTTP BasicAuth, a database, or directory server. HTTP BasicAuth is the basis for single sign on authentication against an identity provider. 

.. note::

    HTTP BasicAuth is not discussed in detail as it is mainly an Apache httpd (web server) configuration.

Agent Authentication LDAP Example

.. code-block::

    # This is an example configuration for an LDAP auth. backend.
    # (take care that Net::LDAP is installed!)
    $Self->{AuthModule} = 'Kernel::System::Auth::LDAP';
    $Self->{'AuthModule::LDAP::Host'} = 'ldap.example.com';
    $Self->{'AuthModule::LDAP::BaseDN'} = 'dc=example,dc=com';
    $Self->{'AuthModule::LDAP::UID'} = 'uid';

    # Check if the user is allowed to auth in a posixGroup
    # (e. g. user needs to be in a group xyz to use )
    $Self->{'AuthModule::LDAP::GroupDN'} = 'cn=znuny-allow,ou=posixGroups,dc=example,dc=com';
    $Self->{'AuthModule::LDAP::AccessAttr'} = 'memberUid';
    # for ldap posixGroups objectclass (just uid)
    $Self->{'AuthModule::LDAP::UserAttr'} = 'UID';
    # for non ldap posixGroups objectclass (with full user dn)
    $Self->{'AuthModule::LDAP::UserAttr'} = 'DN';

.. seealso::

    `AuthBackend in Defaults.pm <https://github.com/znuny/Znuny/blob/dev/Kernel/Config/Defaults.pm#L406>`_

User Synchronization Backend
*****************************

Users are stored locally to ensure they can always log into the system. Synchronization of user data from a directory server to the database is possible. If the data is not synchronized users must then be added manually before they can authenticate against directory service.

Example Synchronization Backend

.. code-block::

    # --------------------------------------------------- #
    # authentication sync settings                        #
    # (enable agent data sync. after succsessful          #
    # authentication)                                     #
    # --------------------------------------------------- #
    # This is an example configuration for an LDAP auth sync. backend.
    # (take care that Net::LDAP is installed!)
    $Self->{'AuthSyncModule'} = 'Kernel::System::Auth::Sync::LDAP';
    $Self->{'AuthSyncModule::LDAP::Host'} = 'ldap.example.com';
    $Self->{'AuthSyncModule::LDAP::BaseDN'} = 'dc=example,dc=com';
    $Self->{'AuthSyncModule::LDAP::UID'} = 'uid';

    # The following is valid but would only be necessary if the
    # anonymous user do NOT have permission to read from the LDAP tree
    $Self->{'AuthSyncModule::LDAP::SearchUserDN'} = '';
    $Self->{'AuthSyncModule::LDAP::SearchUserPw'} = '';

    # in case you want to add always one filter to each ldap query, use
    # this option. e. g. AlwaysFilter => '(mail=*)' or AlwaysFilter => '(objectclass=user)'
    # or if you want to filter with a logical OR-Expression, like AlwaysFilter => '(|(mail=*abc.com)(mail=*xyz.com))'
    $Self->{'AuthSyncModule::LDAP::AlwaysFilter'} = '';

    # AuthSyncModule::LDAP::UserSyncMap
    # (map if agent should create/synced from LDAP to DB after successful login)
    # you may specify LDAP-Fields as either
    #  * list, which will check each field. first existing will be picked ( ["givenName","cn","_empty"] )
    #  * name of an LDAP-Field (may return empty strings) ("givenName")
    #  * fixed strings, prefixed with an underscore: "_test", which will always return this fixed string
    $Self->{'AuthSyncModule::LDAP::UserSyncMap'} = {
        # DB -> LDAP
        UserFirstname => 'givenName',
        UserLastname  => 'sn',
        UserEmail     => 'mail',
    };

.. seealso::

    `AuthSyncBackend in Defaults.pm <https://github.com/znuny/Znuny/blob/dev/Kernel/Config/Defaults.pm#L522>`_

.. versionadded:: 6.4

    LDAP nested group search in the *AuthSyncModule*. ``$Self->{'AuthSyncModule::LDAP::NestedGroupSearch'} = 1;``.


Customer User
*************

Database
=========

The database option is configured per default. Modifying the defaults can be done by copying the information from the ``Default.pm`` to the ``Config.pm`` and addition of new backends can be done as shown below in the directory server example, by suffixing the key name with a number.

Directory Server
=================

Data Source
~~~~~~~~~~~~

Below you will see an example of the configuration required for a directory server connection for customer user data mapping.

.. important::

    In our example I've made the customer user backend a secondary backend by adding a 1 to the key CustomerUser.

Example Configuration

.. code-block::

    # CustomerUser
    # (customer user ldap backend and settings)
        $Self->{CustomerUser1} = {
            Name => 'LDAP Backend',
            Module => 'Kernel::System::CustomerUser::LDAP',
            Params => {
                # ldap host
                Host => 'bay.csuhayward.edu',
                # ldap base dn
                BaseDN => 'ou=seas,o=csuh',
                # search scope (one|sub)
                SSCOPE => 'sub',
                # The following is valid but would only be necessary if the
                # anonymous user does NOT have permission to read from the LDAP tree
                UserDN => '',
                UserPw => '',
                # in case you want to add always one filter to each ldap query, use
                # this option. e. g. AlwaysFilter => '(mail=*)' or AlwaysFilter => '(objectclass=user)'
                AlwaysFilter => '',
                # if the charset of your ldap server is iso-8859-1, use this:
                # SourceCharset => 'iso-8859-1',
                # die if backend can't work, e. g. can't connect to server
                Die => 0,
                # Net::LDAP new params (if needed - for more info see perldoc Net::LDAP)
                Params => {
                    port    => 389,
                    timeout => 120,
                    async   => 0,
                    version => 3,
                },
            },
            # customer unique id
            CustomerKey => 'uid',
            # customer #
            CustomerID => 'mail',
            CustomerUserListFields => ['cn', 'mail'],
            CustomerUserSearchFields => ['uid', 'cn', 'mail'],
            CustomerUserSearchPrefix => '',
            CustomerUserSearchSuffix => '*',
            CustomerUserSearchListLimit => 250,
            CustomerUserPostMasterSearchFields => ['mail'],
            CustomerUserNameFields => ['givenname', 'sn'],
            # Configures the character for joining customer user name parts. Join single space if it is not defined.
            CustomerUserNameFieldsJoin => '',
            # show customer user and customer tickets in customer interface
            CustomerUserExcludePrimaryCustomerID => 0,
            # add a ldap filter for valid users (expert setting)
            # CustomerUserValidFilter => '(!(description=locked))',
            # admin can't change customer preferences
            AdminSetPreferences => 0,
            # cache time to live in sec. - cache any ldap queries
            CacheTTL => 0,
            Map => [
                # note: Login, Email and CustomerID needed!
                # var, frontend, storage, shown (1=always,2=lite), required, storage-type, http-link, readonly, http-link-target, link class(es)
                [ 'UserTitle',       Translatable('Title or salutation'), 'title',               1, 0, 'var', '', 1, undef, undef ],
                [ 'UserFirstname',   Translatable('Firstname'),           'givenname',           1, 1, 'var', '', 1, undef, undef ],
                [ 'UserLastname',    Translatable('Lastname'),            'sn',                  1, 1, 'var', '', 1, undef, undef ],
                [ 'UserLogin',       Translatable('Username'),            'uid',                 1, 1, 'var', '', 1, undef, undef ],
                [ 'UserEmail',       Translatable('Email'),               'mail',                1, 1, 'var', '', 1, undef, undef ],
                [ 'UserCustomerID',  Translatable('CustomerID'),          'mail',                0, 1, 'var', '', 1, undef, undef ],
                # [ 'UserCustomerIDs', Translatable('CustomerIDs'),         'second_customer_ids', 1, 0, 'var', '', 1, undef, undef ],
                [ 'UserPhone',       Translatable('Phone'),               'telephonenumber',     1, 0, 'var', '', 1, undef, undef ],
                [ 'UserAddress',     Translatable('Address'),             'postaladdress',       1, 0, 'var', '', 1, undef, undef ],
                [ 'UserComment',     Translatable('Comment'),             'description',         1, 0, 'var', '', 1, undef, undef ],

                # this is needed, if "SMIME::FetchFromCustomer" is active
                # [ 'UserSMIMECertificate', 'SMIMECertificate', 'userSMIMECertificate', 0, 1, 'var', '', 1, undef, undef ],

                # Dynamic field example
                # [ 'DynamicField_Name_X', undef, 'Name_X', 0, 0, 'dynamic_field', undef, 0, undef, undef ],
            ],
        };

Authentication
~~~~~~~~~~~~~~

The setup for authentication is very similar to that of the user authentication.

Here's an example.

.. important::

    Notice all the keys must have the numeric suffix.


.. code-block::

    # This is an example configuration for an LDAP auth. backend.
    # (take care that Net::LDAP is installed!)
    $Self->{'Customer::AuthModule1'} = 'Kernel::System::CustomerAuth::LDAP';
    $Self->{'Customer::AuthModule::LDAP::Host1'} = 'ldap.example.com';
    $Self->{'Customer::AuthModule::LDAP::BaseDN1'} = 'dc=example,dc=com';
    $Self->{'Customer::AuthModule::LDAP::UID1'} = 'uid';
   
   # Check if the user is allowed to auth in a posixGroup
   # (e. g. user needs to be in a group xyz to use Znuny)
    $Self->{'Customer::AuthModule::LDAP::GroupDN1'} = 'cn=znuny-allow,ou=posixGroups,dc=example,dc=com';
    $Self->{'Customer::AuthModule::LDAP::AccessAttr1'} = 'memberUid';
   
   # for ldap posixGroups objectclass (just uid)
    $Self->{'Customer::AuthModule::LDAP::UserAttr1'} = 'UID';
   
   # for non ldap posixGroups objectclass (full user dn)
    $Self->{'Customer::AuthModule::LDAP::UserAttr1'} = 'DN';
   
   # The following is valid but would only be necessary if the
   # anonymous user do NOT have permission to read from the LDAP tree
    $Self->{'Customer::AuthModule::LDAP::SearchUserDN1'} = '';
    $Self->{'Customer::AuthModule::LDAP::SearchUserPw1'} = '';
   
   # in case you want to add always one filter to each ldap query, use
   # this option. e. g. AlwaysFilter => '(mail=*)' or AlwaysFilter => '(objectclass=user)'
   $Self->{'Customer::AuthModule::LDAP::AlwaysFilter1'} = '';
   
   # in case you want to add a suffix to each customer login name, then
   # you can use this option. e. g. user just want to use user but
   # in your ldap directory exists user@domain.
    $Self->{'Customer::AuthModule::LDAP::UserSuffix1'} = '@domain.com';

   # Net::LDAP new params (if needed - for more info see perldoc Net::LDAP)
    $Self->{'Customer::AuthModule::LDAP::Params1'} = {
        port    => 389,
        timeout => 120,
        async   => 0,
        version => 3,
    };

.. note::

    It is recommendable to leave the default settings alone and start adding your own changes in the ``Config.pm`` using the suffixing method. This provides for a fallback solution for local configuration of test customers, customer users and customers.

.. important::

    All common configurations like AuthBackend and AuthSyncBackend or CustomerUser and CustomerAuth should share, in most cases, the same suffix. i.e. a CustomerUser1 key should have a complimentary Customer::AuthModule1 key.

Customer
********

Currently companies organizations can only be read from and written to database tables. Here you may also have up to 11 configurable backends.


.. important:: 
    
    Customer company sources can come from multiple backends, but the relationships are not bound to CustomerUser backend keys by their suffix.
