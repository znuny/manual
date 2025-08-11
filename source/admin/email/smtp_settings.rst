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
* ``SendmailModule::AuthPassword``: Password for the SMTP authentication.
* ``SendmailModule::AuthUser``: The username for SMTP authentication.
* ``SendmailModule::AuthenticationType``: The type of authentication used by your SMTP server (e.g., `password`, `OAuth2 token`).
* ``SendmailModule::Host``: The hostname of your SMTP server.
* ``SendmailModule::Port``: The port number for your SMTP server (usually 25, 465, or 587).

.. _sending_rate_limits:

Sending Rate Limits
*******************

When sending a large number of emails, it is important to manage the rate at which they are sent to avoid being flagged as spam or overwhelming the SMTP server.

To limits the number of emails that can be sent at once, which is occasionally necessary depending upon the email providers such as Microsoft Office 365,  the following settings can be modified as needed. It works for every possible ``SendmailModule``.

* ``SendmailModule::RateLimit``: Limits the amount of emails which are sent within one batch. Disable this setting to have no limit.
* ``SendmailModule::RateLimitPerSenderAddress``: Applies the limit defined in 'SendmailModule::RateLimit' per sender address.
