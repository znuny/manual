E-Mail Headers
##############

Using special and standard headers, an administrator can set ticket data using the PostMaster filters to set ticket attributes during inbound email processing automatically.
The headers that can be used in the set criteria of the PostMaster filters are listed below in the table.

Trust Level
***********

As a security measure, it's not possible to process X-OTRS headers of an inbound message, without verifying the trust level. The trust level for an email is set at the mailbox level. Therefore they can be set using a PostMaster filter.

.. seealso:: :ref:`Configure Mailbox Collection <PageNavigation email_postmaster_mail_account>`

For local mail delivery via procmail, trust is assumed and can be selectively disabled where necessary with procmail configuration not covered here.

If an account is trusted, X-OTRS headers found in a mail message will automatically be applied.

Header Format
*************

There are two different types of headers that can be used in automatic processing of email.the initial header has the form ``X-OTRS-Key``. For follow-up information the format is ``X-OTRS-FollowUp-Key``.

A follow-up key will be applied, only if the email was successfully detect as a follow-up to an existing ticket.

Header Configuration
********************

All headers which are to be considered in email processing are configured under ``PostmasterX-Header`` in the system configuration. These headers are only listed here without the FollowUp counterparts, but can be used as FollowUp as well.

Default Header Table:

+-----------------------------+---------------+------------------------------------------------------------------------+
| Key                         | Example Value | Description                                                            |
+=============================+===============+========================================================================+
| X-OTRS-Priority             | 1 very low    | Any valid system priority.                                             |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Queue                | Postmaster    | Any valid system queue.                                                |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Lock                 | lock          | Any valid ticket lock.                                                 |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Ignore               | Yes           | Ignore mail (Yes) keep mail (Default: No)                              |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-State                | open          | Any valid ticket state.                                                |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Type                 | Unclassified  | Any valid ticket type.                                                 |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Service              | Service Name  | Any valid ticket service.                                              |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-SLA                  | SLA Name      | Any valid ticket SLA.                                                  |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-CustomerUser         | customer      | Any valid customer user login.                                         |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-CustomerNo           | customer_id   | Any valid customer id.                                                 |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-SenderType           | agent         | Any valid sender type.                                                 |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-IsVisibleForCustomer | 1             | Visible (Default: 1) or not visible (0)                                |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-DynamicField-Field   | Value         | Value depends on dynamic field type. Must be a field of object Ticket. |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Loop                 | 1             | Suppress auto-replies if set to 1/true                                 |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-FollowUp-State-Keep  | 1             | Keep the last set ticket state (1) (Default: 0)                        |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-AttachmentExists     | 1             | Has attachment (1) has none (0).                                       |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-AttachmentCount      | 4             | Has a specified number of attachments.                                 |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Owner                | agent         | Any valid user login.                                                  |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-OwnerID              | 45            | Any valid user id.                                                     |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Responsible          | agent         | Any valid user login.                                                  |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-ResponsibleID        | 48            | Any valid user id.                                                     |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-Title                | Title         | Any text.                                                              |
+-----------------------------+---------------+------------------------------------------------------------------------+
| X-OTRS-BodyDecrypted        | 1             | Store body decrypted.                                                  |
+-----------------------------+---------------+------------------------------------------------------------------------+

.. note::

   Headers can be manually extended to support own headers, and they already support all standard headers as well for the filter criteria.

List of included headers. See `this resource <https://www.iana.org/assignments/message-headers/message-headers.xhtml>`_ for more info.

* From
* To
* Cc
* Reply-To
* ReplyTo
* Subject
* Message-ID
* Message-Id
* Resent-To
* Resent-From
* Precedence
* Mailing-List
* List-Id
* List-Archive
* Errors-To
* References
* In-Reply-To
* Auto-Submitted
* X-Loop
* X-Spam
* X-Spam-Flag
* X-Spam-Level
* X-Spam-Score
* X-Spam-Status
* X-No-Loop
* X-Priority
* Importance
* X-Mailer
* User-Agent
* Organization
* X-Original-To
* Delivered-To
* Envelope-To
* X-Envelope-To
* Return-Path

