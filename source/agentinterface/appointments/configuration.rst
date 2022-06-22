Appointment Configuration Options
#################################

Ticket Creation
***************

Some defaults and settings are available in the system configuration.

Ticket::Frontend::AgentAppointmentEdit###StateType
    Defines the next possible ticket states for calendar based tickets.
    
Ticket::Frontend::AgentAppointmentEdit###StateDefault
    Defines the default next state.
    
Ticket::Frontend::AgentAppointmentEdit###PriorityDefault
    Defines the default ticket priority for calendar based tickets.
    
Ticket::Frontend::AgentAppointmentEdit###ProcessTreeView
    Defines if the processes should be displayed in TreeView.
    
Ticket::Frontend::AgentAppointmentEdit###Group
    Enables calendar based ticket creation feature only for the listed groups.
    
Znuny4OTRSCalendarBasedTicketCreation###Title
    Defines the default ticket title for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###Body
    Defines the default ticket body for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###ArticleChannelName
    Defines the default article channel name for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###ArticleIsVisibleForCustomer
    Defines the default visibility of articles for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###SenderType
    Defines the default sender type for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###From
    Defines the default from for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###HistoryType
    Defines the default history type for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###HistoryComment
    Defines the default history comment for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation###ContentType
    Defines the default content type for calendar based tickets.
    
Znuny4OTRSCalendarBasedTicketCreation::TicketCreationCatchUpThreshold
    Threshold (in minutes) for catching up with ticket creation for appointments. Tickets for due appointments will only be created if their planned creation date is not older than the configured amount of minutes. This prevents creation of tickets for e. g. recurring appointments if the ticket creation will be executed some time later.
    
Daemon::SchedulerCronTaskManager::Task###Znuny4OTRSCalendarBasedTicketCreation
    Creates the calendar-based tickets regularly.
    
Daemon::SchedulerCronTaskManager::Task###Znuny4OTRSCalendarBasedTicketCreationCleanup
    Cleans up the calendar-based tickets regularly.
    
Frontend::Output::FilterElementPost###Znuny4OTRSCalendarBasedTicketCreation
    Registers an Output filter to add the additional input fields for the calendar-based ticket creation.
    
Frontend::Module###AgentZnuny4OTRSCalendarBasedTicketCreationAJAX
    Frontend module registration for the agent interface.
    
Frontend::Navigation###AgentZnuny4OTRSCalendarBasedTicketCreationAJAX###003-Znuny4OTRSCalendarBasedTicketCreation
    Main menu item registration.
    
Znuny4OTRSDatabaseBackend::Znuny4OTRSCalendarBasedTicketCreation::CacheTTL
    Defines the cache settings for the Znuny4OTRS-DatabasBackend (default: 1 day)
    
AutoloadPerlPackages###100-Znuny4OTRSCalendarBasedTicketCreationAppointment
    Autoloading of Znuny4OTRSCalendarBasedTicketCreationAppointment extensions.
    
Loader::Module::AgentAppointmentCalendarOverview###999-Znuny4OTRSCalendarBasedTicketCreation
    Loader module registration for AgentAppointmentCalendarOverview.
    


