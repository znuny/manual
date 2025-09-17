Znuny 7.2.2
###########

**Release Information:**

+---------------------+--------------------------------------------------------------+
| Release Date        | 17-SEP-2025                                                  |
+---------------------+--------------------------------------------------------------+
| Release Type        | Patchlevel                                                   |
+---------------------+--------------------------------------------------------------+
| Download            | `<https://download.znuny.org/releases/znuny-7.2.2.tar.gz>`_  |
+---------------------+--------------------------------------------------------------+
| GitHub              | `<https://github.com/znuny/Znuny/tree/rel-7_2_2>`_           |
+---------------------+--------------------------------------------------------------+


Fixed Issues
************
- Fixed installer failure due to wrong database credentials. Thanks for reporting to `@Alexos1998 <https://github.com/Alexos1998>`_. (`#710 <https://github.com/znuny/Znuny/issues/710>`_)
- Fixed the handling of the new responsible in ACLs.
- Fixed the outgoing email check in the installer.
- Fix for duplicate favourites in the admin menu. Thanks to SectorNord AG. (`PR#705 <https://github.com/znuny/Znuny/pull/705>`_)
- Fixed the column length for the article color in the table article_color. Thanks for reporting to `@StuxForce <https://github.com/StuxForce>`_. (`#707 <https://github.com/znuny/Znuny/issues/707>`_)
- Updated the Google OAuth2 template always to request an access token when needed. Thanks for reporting to `@AeonJJohnson <https://github.com/AeonJJohnson>`_. (`#709 <https://github.com/znuny/Znuny/issues/709>`_)
- Article colors does not invert anymore when the dark mode is active.
- Prevent deleting valid web services. They need to be set not to be valid before being deleted.
- Fixed: Enter/Ctrl+Enter leads to saving the draft instead of submitting the form. Thanks to SectorNord AG. (`PR#704 <https://github.com/znuny/Znuny/pull/704>`_)
- Fixed the visibility of plain/text articles in the customer portal.
- Fixed a migration issue when using PostgreSQL and Oracle. Thanks for reporting to `@AVONON-DST <https://github.com/AVONON-DST>`_. (`#706 <https://github.com/znuny/Znuny/issues/706>`_)

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_2_2/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_2_2>`_ for a list of all changes.
