Znuny 7.2.1
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 20-AUG-2025                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Minor version release                                        |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.2.1.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_2_1>`_           |
+---------------------+--------------------------------------------------------------+

Features
********
- Added Outh2 Client Credentials Flow
- Added Microsoft Graph as an available protocol for fetching and sending emails.
- Integrated the addon SMTPRatelimit
- Replaced the CKEditor 4 with CKEditor 5
- A graphical, categorized overview was added to select processes from, aka the process shop.
- Import, export, copy, and delete functionality for auto responses, salutations, signatures, and templates.
- New communication channel web for articles created via he customer portal.
- Integrated the addon Znuny-Translations to edit custom translations in the admin area.
- Article colors for the article overview of the ticket details view can now be modified in the admin area.

Changes
*******
- Added missing sort parameter for the mention view.
- Users mentioned in quoted articles will not be notified again.


Fixed Issues
************
- Improved the handling of mentions for archived tickets. Thanks for reporting to `@Fainsy <https://github.com/Fainsy>`_. (`#620 <https://github.com/znuny/Znuny/issues/620>`_)
- Fixed displaying the customer name in the customer ticket overview.
- Fixed the order of the mention toolbar icons and changed their priority to prevent display collision with other toolbar icons.
- Fixed the handling of attachments when processing an invoker's response. `#694 <https://github.com/znuny/Znuny/issues/694>`_)
- Fixed the tree view icon for dynamic fields of the type drop-down and multiselect.
- Fixed the TLD of check email addresses in S/MIME certificates. Thanks for reporting to `@dsm-museum-it <https://github.com/dsm-museum-it>`_.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_2_1/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_2_1>`_ for a list of all changes.
