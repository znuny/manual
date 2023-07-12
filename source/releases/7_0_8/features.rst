Changes
#######

New
***

- Added console command to import dynamic fields and dynamic field screens configuration.
- Added information about invalid settings to AgentTicketZoom 'Ticket Information'.

Improvements
************

- Updated default user mention notifications to include salutation and signature.
- Improved popup profiles and Frontend::RichText::Settings###Width.

Issues Fixed
************

- Empty HTML bodies now properly displayed.
- From, To, Cc fields now display correctly. "Test User test@user.com"
- Line breaks in processes now shown also with richtext disabled.
- Generic agents events triggers can now be deleted.
- Fixed email address shown in user's avatar preferences when editing the preferences of another user (not the own user).
- Fixed Calendar appointment plugin AppointmentID data type.

Developer
*********

- Added new type 'HTML' to AgentTicketZoom TicketMenu. This allows additional HTML elements to be added using 'Ticket::Frontend::MenuModule###*'.
- Added SysConfig/ValueType/Entity/Webservice.pm.

Read about all changes in the `CHANGES.md <https://raw.githubusercontent.com/znuny/Znuny/rel-7_0_8/CHANGES.md>`_. For the complete list of all changes, see the commits on `GitHub <https://github.com/znuny/Znuny/commits/rel-7_0_8>`_.
