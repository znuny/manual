.. meta::
   :description: Configure Znuny SMTP sending — set SendmailModule, host, port, OAuth2 or password authentication and choose between SMTP, SMTPS, SMTPTLS, MSGraph or Sendmail.
   :keywords: znuny smtp, sendmail module, smtps, smtptls, oauth2 smtp, msgraph email, smtp authentication, email sending

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

Available SMTP Modules
**********************

It is possible to use different SMTP modules for sending emails. The following modules are available:

* ``Kernel::System::Email::DonNotSendEmail``: A module that simulates email sending without actually sending emails, useful for testing.
* ``Kernel::System::Email::MSGraph``: An SMTP module that uses the Microsoft Graph API for sending emails.
* ``Kernel::System::Email::MultiSendmail``: A module to provide multiple sendmail configurations for different sender addresses.
* ``Kernel::System::Email::Sendmail``: A module that uses the sendmail command for sending emails.
* ``Kernel::System::Email::SMTP``: The standard SMTP module for sending emails.
* ``Kernel::System::Email::SMTPS``: An SMTP module that supports SSL/TLS encryption.
* ``Kernel::System::Email::SMTPTLS``: An SMTP module that supports STARTTLS encryption.
* ``Kernel::System::Email::Test``: A module for testing email sending without actually sending emails. Mails are saved to the var/tmp/Cache/EmailTest directory.

Test SMTP Configuration
***********************

``bin/znuny.Console.pl  Dev::Tools::TestEmails`` Reads the mails send to the Kernel::System::Email::Test module and outputs them to the console. This is useful for testing the SMTP configuration without sending actual emails. Once read by the console command, the mails are removed from the var/tmp/Cache/EmailTest directory. You can redirect the output to a file for further analysis, e.g., ``bin/znuny.Console.pl  Dev::Tools::TestEmails > test_emails_output.txt``.

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
    
    Before configuring dispatch via Microsoft Graph, all mails that are still in the mail queue must be sent, otherwise they will be sent with encoding errors. The Mail Queue can be managed using the console command. See more :ref:`pagenavigation console_index`.

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

Multiple SMTP Configurations
****************************

See :ref:`pagenavigation outbound_email_profiles` for information on how to set up multiple SMTP configurations for different sender addresses or purposes.
