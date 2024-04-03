Overview
########

Welcome to Znuny LTS version 6.5.5

Improvements
************

- Added links to the customer user information center to create new tickets or switch to the customer if the feature is enabled.
- Added pagination for tickets with long article lists in the ticket details view.
- Added optional caching to web service requests of dynamic field types WebserviceDropdown and WebserviceMultiselect.
- Added a parameter to enforce account selection for the Microsoft OAuth2 template.

Issues Fixed
************

- Fixed bug with customer user id over 100 characters and additional assigned customer companies.
- Improved cache handling regarding dynamic fields assigned to customer users and customer companies when updating these entities.
- Fixed error handling in invoker Ticket::Generic.
- Updated maximum length of generic agent job database fields and their input fields in dialog AdminGenericAgent to prevent errors storing values too long for the database (`#474 <https://github.com/znuny/Znuny/issues/474>`_).


Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-6_5_5/CHANGES.md>`_. See the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-6_5_5>`_ for a list of all changes.
