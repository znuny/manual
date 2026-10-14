Znuny LTS 6.5.26
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 14-OCT-2026                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel with security fixes                               |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.26.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_26>`_          |
+---------------+--------------------------------------------------------------+


Security Fixes
**************
- Form IDs for attachment uploads are now generated and handled securely. Thanks to `@kta1kri <https://github.com/kta1kri>`_ for reporting.

Bug Fixes
*********
- Fixed the password policy check for the option "minimum 2 characters" (``PasswordMin2Characters``) being slightly off.
- Fixed the notification to the agent who created the ticket not working for some ticket types.
- Fixed ``AdminDynamicFieldScreenConfiguration`` listing dynamic fields of all object types.
- Fixed regular file attachments being unintentionally copied to newly created tickets/articles when using ``<OTRS_FIRST_ARTICLE_Body>`` or ``<OTRS_LAST_ARTICLE_Body>`` in a transition action, even without ``Attachments``/``AttachmentIDs``/``AttachmentsReuse`` configured.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_26/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_26>`_ for a list of all changes.
