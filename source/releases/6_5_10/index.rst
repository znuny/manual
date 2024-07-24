Znuny LTS 6.5.10
################

**Release Information:**

+--------------+--------------------------------------------------------------+
| Release Date | 24-JUL-2024                                                  |
+--------------+--------------------------------------------------------------+
| Release Type | Patchlevel                                                   |
+--------------+--------------------------------------------------------------+
| Download     | `<https://download.znuny.org/releases/znuny-6.5.10.tar.gz>`_ |
+--------------+--------------------------------------------------------------+
| GitHub       | `<https://github.com/znuny/Znuny/tree/rel-6_5_10>`_          |
+--------------+--------------------------------------------------------------+

Changes
*******
- GenericInterface: Omitted fields now apply to the whole data passed through invokers.
- GenericInterface: TicketCreate and TicketUpdate operations now accept multiple articles.

Fixed Issues
************
- Updated JavaScript dependencies Moment.js and jQueryUI.
- Improved and fixed links to the CustomerUser and Customer Information Center in several views.
- Fixed missing translations on title hovers on the generic dashboard.
- Removed outdated directives from the HTTP header Content-Security-Policy.
- Last mention date is now displayed in the correct timezone and format.
- Fixed autocompletion search for dynamic fields webservice in the ticket search screen.
- Fixed event registration regular expressions in the system configuration Thanks to Paweł Bogusławski (@pboguslawski) for reporting. `#440 <https://github.com/znuny/Znuny/issues/440>`_


Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_10/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_10>`_ for a list of all changes.