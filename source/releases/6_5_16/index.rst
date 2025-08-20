Znuny LTS 6.5.16
################

**Release Information:**

+---------------+--------------------------------------------------------------+
| Release Date  | 20-AUG-2025                                                  |
+---------------+--------------------------------------------------------------+
| Release Type  | Patchlevel                                                   |
+---------------+--------------------------------------------------------------+
| Download      | `<https://download.znuny.org/releases/znuny-6.5.16.tar.gz>`_ |
+---------------+--------------------------------------------------------------+
| GitHub        | `<https://github.com/znuny/Znuny/tree/rel-6_5_16>`_          |
+---------------+--------------------------------------------------------------+

Features
********
- Integrated the addon SMTPRatelimit

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


Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_16/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_16>`_ for a list of all changes.