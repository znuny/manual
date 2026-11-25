.. meta::
   :description: Reference of all X-Znuny email headers — automatically set ticket attributes during inbound email processing via PostMaster filters, gated by mailbox trust levels.
   :keywords: znuny x-znuny headers, znuny x-otrs headers, email headers, postmaster filter, trust level, x-otrs, header reference

.. _PageNavigation annexes_headers_index:

E-Mail Headers
##############

Using special and standard headers, an administrator can set ticket data using the PostMaster filters to set ticket attributes during inbound email processing automatically.
The headers that can be used in the set criteria of the PostMaster filters are listed below in the table.

Trust Level
***********

As a security measure, it's not possible to process X-Znuny headers of an inbound message, without verifying the trust level. The trust level for an email is set at the mailbox level. Therefore they can be set using a PostMaster filter.

.. seealso:: :ref:`Configure Mailbox Collection <PageNavigation email_postmaster_mail_account>`

For local mail delivery via procmail, trust is assumed and can be selectively disabled where necessary with procmail configuration not covered here.

If an account is trusted, X-Znuny headers found in a mail message will automatically be applied.

Header Format
*************

There are two different types of headers that can be used in automatic processing of email. The initial header has the form ``X-Znuny-Key``. For follow-up information the format is ``X-Znuny-FollowUp-Key``.

.. versionchanged:: 7.5.1

    The headers have been renamed from ``X-OTRS-*`` to ``X-Znuny-*``. Incoming emails with ``X-OTRS-*`` headers are still processed, and PostMaster filters can match and set both variants. During the update, the system configuration settings ``PostmasterX-Header`` and ``KeepStateHeader``, the PostMaster filter modules and the PostMaster filters are migrated to the new names.

A follow-up key will be applied, only if the email was successfully detect as a follow-up to an existing ticket.

Header Configuration
********************

All headers which are to be considered in email processing are configured under ``PostmasterX-Header`` in the system configuration. These headers are only listed here without the FollowUp counterparts, but can be used as FollowUp as well.

Default Header Table:

+------------------------------+---------------+------------------------------------------------------------------------+
| Key                          | Example Value | Description                                                            |
+==============================+===============+========================================================================+
| X-Znuny-Priority             | 1 very low    | Any valid system priority.                                             |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-PriorityID           | 3             | Any valid priority id.                                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Queue                | Postmaster    | Any valid system queue.                                                |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-QueueID              | 4             | Any valid queue id.                                                    |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Lock                 | lock          | Any valid ticket lock.                                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Ignore               | Yes           | Ignore mail (Yes) keep mail (Default: No)                              |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-State                | open          | Any valid ticket state.                                                |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-StateID              | 4             | Any valid state id.                                                    |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-State-PendingTime    | +2d           | Pending time for pending states, absolute or relative.                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Type                 | Unclassified  | Any valid ticket type.                                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-TypeID               | 1             | Any valid type id.                                                     |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Service              | Service Name  | Any valid ticket service.                                              |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-ServiceID            | 2             | Any valid service id.                                                  |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-SLA                  | SLA Name      | Any valid ticket SLA.                                                  |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-SLAID                | 1             | Any valid SLA id.                                                      |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-CustomerUser         | customer      | Any valid customer user login.                                         |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-CustomerNo           | customer_id   | Any valid customer id.                                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-SenderType           | agent         | Any valid sender type.                                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-IsVisibleForCustomer | 1             | Visible (Default: 1) or not visible (0)                                |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-DynamicField-Field   | Value         | Value depends on dynamic field type. Must be a field of object Ticket. |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Loop                 | 1             | Suppress auto-replies if set to 1/true                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-FollowUp-State-Keep  | 1             | Keep the last set ticket state (1) (Default: 0)                        |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-AttachmentExists     | 1             | Has attachment (yes) has none (no).                                    |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-AttachmentCount      | 4             | Has a specified number of attachments.                                 |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Owner                | agent         | Any valid user login.                                                  |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-OwnerID              | 45            | Any valid user id.                                                     |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Responsible          | agent         | Any valid user login.                                                  |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-ResponsibleID        | 48            | Any valid user id.                                                     |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-Title                | Title         | Any text.                                                              |
+------------------------------+---------------+------------------------------------------------------------------------+
| X-Znuny-BodyDecrypted        | 1             | Store body decrypted.                                                  |
+------------------------------+---------------+------------------------------------------------------------------------+

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

Relevant Documentation
***********************

:ref:`pagenavigation admin_automation_postmaster_filter_index`
 
