.. meta::
   :description: Znuny 7.3.8 release notes — security fix for attachment upload form IDs, new accounted time column, changes and bug fixes for this patchlevel release, released 14 October 2026.
   :keywords: znuny 7.3.8, znuny release notes, znuny changelog, 7.3.8 fixes, znuny patchlevel release, znuny update 7.3.8, znuny security fixes

Znuny 7.3.8
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 14-OCT-2026                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel with security fixes                               |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.3.8.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_3_8>`_           |
+---------------------+--------------------------------------------------------------+

Changes & Improvements
**********************
- Added the column ``TicketAccountedTime`` for the dashboard, the small ticket overview and ticket link objects. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG). (`PR#574 <https://github.com/znuny/Znuny/pull/574>`_)
- Added support for ``ZNUNY_TA_*`` tags alongside ``OTRS_TA_*`` tags in the transition action ``ArticleSend``.
- Improved error handling when sending email messages. Thanks to Paweł Bogusławski (`@pboguslawski <https://github.com/pboguslawski>`_). (`PR#375 <https://github.com/znuny/Znuny/pull/375>`_)
- Improved the information shown about incompatible versions when installing packages via the package manager.

Security Fixes
**************
- Form IDs for attachment uploads are now generated and handled securely. Thanks to `@kta1kri <https://github.com/kta1kri>`_ for reporting.

Bug Fixes
*********
- Fixed agent ticket action dialogs showing an empty state option on first load when a default state is configured.
- Fixed the OpenSearch description in the agent and customer ticket search not working in Firefox, because Firefox does not send cookies when requesting the OpenSearch description file. The session ID is now always part of that URL. Thanks to Tim Puettmanns (`@tipue-dev <https://github.com/tipue-dev>`_). (`PR#319 <https://github.com/znuny/Znuny/pull/319>`_)
- Fixed invalid UTF-8 in emails causing crashes.
- Fixed column settings filters in dashboard and overview screens extending beyond the viewport. Thanks to `@LuBroering <https://github.com/LuBroering>`_ (Lukas Bröring, Sector Nord AG). (`PR#849 <https://github.com/znuny/Znuny/pull/849>`_)
- Fixed process management: file preferences of a process (e.g. its icon) were exported as a content reference instead of Base64 if the process had been cached before, so that they could not be imported.
- Fixed the misaligned all-day checkbox label in the appointment dialog.
- Fixed the transition action ``ArticleSend`` sending an article with empty body, salutation and signature when configured to use a standard template. The usage of all ``OTRS_TA_*`` tags is fixed as well.
- Fixed form action buttons being hidden behind the Safari bottom toolbar on iOS. Thanks to `@avononit <https://github.com/avononit>`_ for reporting. (`#667 <https://github.com/znuny/Znuny/issues/667>`_)
- Fixed the "Mark article" link in the ticket zoom not working.
- Fixed ``AdminDynamicFieldScreenConfiguration`` listing dynamic fields of all object types.
- Fixed the alignment of the accounted time in the ticket details.
- Fixed notifications being shown in the background in some dialogs.
- Fixed the incorrectly indented subject field in the customer ticket process.
- Fixed the options button in the ticket details mobile view no longer responding after switching to a different article. Thanks to `@avononit <https://github.com/avononit>`_ for reporting. (`#671 <https://github.com/znuny/Znuny/issues/671>`_)
- Fixed the medium and preview ticket overview views being fully accessible and rendered on narrow/tablet screens without any restriction.
- Fixed cluster sections in the options panel being initially expanded and inconsistent caret behavior.
- Fixed article duplication and iframe reload in the small screen view of the customer ticket details.
- Fixed the password policy check for the option "minimum 2 characters" (``Min2Characters``) being too restrictive.
- Fixed the notification to the agent who created the ticket not working for some ticket types.
- Fixed images with explicit HTML width/height attributes (e.g. logos in quoted email signatures) being stretched to fill their container. Thanks to `@AVONON-DST <https://github.com/AVONON-DST>`_ for reporting. (`#743 <https://github.com/znuny/Znuny/issues/743>`_)
- Fixed the missing ``OutputFilterHook_NoTicketOptionsFallback`` in ``AgentTicketCompose`` and ``AgentTicketForward``. Thanks to `@scharfstuttgart <https://github.com/scharfstuttgart>`_ for reporting. (`#846 <https://github.com/znuny/Znuny/issues/846>`_)
- Fixed regular file attachments being unintentionally copied to newly created tickets/articles when using ``<OTRS_FIRST_ARTICLE_Body>`` or ``<OTRS_LAST_ARTICLE_Body>`` in a transition action, even without ``Attachments``/``AttachmentIDs``/``AttachmentsReuse`` configured.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_3_8/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_3_8>`_ for a list of all changes.
