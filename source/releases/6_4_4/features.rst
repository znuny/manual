New Features
############

Improvements
************
* Added ReadOnly option for CustomerCompany to the Defaults.pm for reference.
* Added System Configuration options to control more settings of CKEditor (Thanks @SectorNord).
* Added input field for OAuth2 token scope to admin dialog.
* Added FilterViews for FilterAppointments function.
* Improved Migration Script for Generic Interface for renamed invoker.
* Improved usability* AgentTicketBulk* Set DynamicField_NAME. Used checkbox to true if it is set before or if dynamic field is mandatory.
* Index S/MIME keys now runs during the migration.

Bugs Fixed
**********

* Fixed overlapping input list in search dialog.
* Fixed displayed value for dynamic field type Webservice Text when placeholder <OTRS_TICKET_DynamicField_*_Value> is being used.
* Fixed sorting of System Configuration entity value types.
* Fixed SQL condition in Kernel::System::CustomerUser::DB::CustomerSearch.
* Fixed TransitionValidation CheckValueGet().
* Fixed Bug in SupportDataCollector plugin for default user.


Read about all changes in the `CHANGES.md <https://github.com/znuny/Znuny/blob/rel-6_4_4/CHANGES.md>`_
