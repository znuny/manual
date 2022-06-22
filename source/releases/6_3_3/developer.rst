Relevant Changes For Developers
###############################

Here are some relevant changes for system integrators and developers.

- Deactivated Perl code execution for Template::Toolkit. Thanks to Sven Oesterling (OTOBO).
- Kernel::System::DynamicField::Webservice::DisplayValueGet() now also searches for the stored value to retrieve the display value.
- Deprecated structures in SysConfig option Package::RepositoryList (e.g. from old ITSM packages) will now be ignored instead of throwing an error.