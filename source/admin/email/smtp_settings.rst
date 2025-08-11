.. _admin_smtp_settings:

SMTP Settings
#############

Sending emails via SMTP is a common requirement for many installations. 
In this section, we will cover how to configure SMTP settings in your application.

SMTP Configuration
******************

The settings for SMTP are configured in the system configuration. 

1. Navigate to Admin -> System Configuration.
2. Use the navigation, select **Core -> Email**

Configure the following settings:


* ``SendmailModule``: Set this to `Kernel::System::Email::SMTP` to enable SMTP. (SMTPS or SMTPTLS based on your requirements)
* ``SendmailModule::AuthUser``: The username for SMTP authentication.
* ``SendmailModule::AuthenticationType``: The type of authentication used by your SMTP server (e.g., `password`, `OAuth2 token`).
* ``SendmailModule::AuthPassword``: Password for the SMTP authentication.
* ``SendmailModule::OAuth2TokenConfigName``: The name of the OAuth2 token configuration when used.
* ``SendmailModule::Host``: The hostname of your SMTP server.
* ``SendmailModule::Port``: The port number for your SMTP server (usually 25, 465, or 587).

MS-Graph API
************

Znuny can send and retrieve emails via Microsoft Graph. An OAuth2 token (see :ref:`pagenavigation authenticate_token_index`) is the basis for authentication.
Both *authorization code* and the *client credentials* flow are supported. The following permissions are required for the Microsoft Graph application:

Mail.ReadWrite
    Retrieval of emails

Mail.Send
    Sending emails

Sending E-Mails via Microsoft Graph
====================================

.. important::
    
    Before configuring dispatch via Graph, all mails that are still in the mail queue must be sent, otherwise they will be sent with encoding errors.
    see ::ref:`pagenavigation console_maintenance` 

System Specific Settings
~~~~~~~~~~~~~~~~~~~~~~~~

These system-wide configurable settings are used for sending an receiving emails:

* ``WebUserAgent::Proxy``
* ``WebUserAgent::NoProxy``
* ``WebUserAgent::Timeout``
* ``WebUserAgent::DisableSSLVerification``


Example Configuration
=====================

SendmailEncodingForce
    Must be activated and set to 8bit, otherwise encoding errors will occur when sending.

SendmailModule
    Kernel::System::Email::MSGraph

SendmailModule::Host
    graph.microsoft.com

SendmailModule::AuthUser
    mymail@mydomain.onmicrosoft.com

.. note:: 
    
    The "AuthUser" account requires SendAs permissions for all email addresses to be used for sending.

SendmailModule::AuthenticationType
    oauth2_token

SendmailModule::OAuth2TokenConfigName
    OAuth2TokenName


.. _sending_rate_limits:

Sending Rate Limits
*******************

When sending a large number of emails, it is important to manage the rate at which they are sent to avoid being flagged as spam or overwhelming the SMTP server.

To limits the number of emails that can be sent at once, which is occasionally necessary depending upon the email providers such as Microsoft Office 365,  the following settings can be modified as needed. It works for every possible ``SendmailModule``.

* ``SendmailModule::RateLimit``: Limits the amount of emails which are sent within one batch. Disable this setting to have no limit.
* ``SendmailModule::RateLimitPerSenderAddress``: Applies the limit defined in 'SendmailModule::RateLimit' per sender address.


.. seealso:: 

    For receiving mail, please use the :ref:`pagenavigation email_postmaster_mail_account` configuration module.
