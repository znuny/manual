Screen Configuration
####################

Each screen in Znuny can be configured to show different fields, blocks, and options. This allows you to customize the user interface to better fit your business processes and user needs. Many of the screens have common configuration options, such as the ability to show or hide certain fields, set defaults for the fields, and make them mandatory. In this chapter, we will cover the basics of screen configuration and provide examples of how to customize different screens in Znuny. Note that all screen configuration happens in the system configuration, so you will need to have the appropriate permissions to access and modify these settings.

Navigate to Admin -> System Configuration. Here you will find a list of all the screens that can be configured. Use the navigation tree on the left to find the screen you want to configure. There are under, for example:

Frontend => Agent => View => TicketFreeText

The screens which share common settings are:

- **AgentTicketClose** - :ref:`pagenavigation ticketviews_agentticketactionclose` 
- **AgentTicketCustomer** - :ref:`pagenavigation ticketviews_agentticketcustomer` 
- **AgentTicketFreeText** - :ref:`pagenavigation ticketviews_agentticketfreetext` 
- **AgentTicketNote** - :ref:`pagenavigation ticketviews_agentticketnote` 
- **AgentTicketOwner** - :ref:`pagenavigation ticketviews_agentticketowner` 
- **AgentTicketPending** - :ref:`pagenavigation ticketviews_agentticketreminder` 
- **AgentTicketPriority**  - :ref:`pagenavigation ticketviews_agentticketpriority` 
- **AgentTicketResponsible**  - :ref:`pagenavigation ticketviews_agentticketresponsible` 

.. important:: 
    
    For all other screens, see the options by using the system configuration navigation menu.


Once you have selected, you will see a list of configuration options for that screen. You can click on each option to expand it and see more details about what it does and how to use it. Some options may have additional settings that you can configure, such as default values or validation rules. Make sure to save your changes after configuring the screen to apply the new settings. Here a list of the most common options you will find in the screen configuration:

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Description**
  Displayed in the sidebar as additional information.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Permission**
  Required permissions to use the ticket free text screen in the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###RequiredLock**
  Defines if a ticket lock is required in the ticket free text screen of the agent interface (if the ticket isn't locked yet, the ticket gets locked and the current agent will be set automatically as its owner).

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###TicketType**
  Sets the ticket type in the ticket free text screen of the agent interface (Ticket::Type needs to be enabled).

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Service**
  Sets the service in the ticket free text screen of the agent interface (Ticket::Service needs to be enabled).

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###ServiceMandatory**
  Sets if service must be selected by the agent.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###SLAMandatory**
  Sets if SLA must be selected by the agent.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Queue**
  Sets the queue in the ticket free text screen of a zoomed ticket in the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###QueueMandatory**
  Sets if queue must be selected by the agent.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###CustomerUser**
  Sets the customer user field in the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###CustomerUserMandatory**
  Sets the customer user field as mandatory.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###CustomerIDReadOnly**
  Controls if CustomerID is read-only in the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Owner**
  Sets the ticket owner in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###OwnerMandatory**
  Sets if ticket owner must be selected by the agent.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Responsible**
  Sets the responsible agent of the ticket in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###ResponsibleMandatory**
  Sets if ticket responsible must be selected by the agent.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###State**
  Sets the state of a ticket in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###StateMandatory**
  Sets if state must be selected by the agent.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###StateType**
  Defines the next state of a ticket after adding a note, in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###StateDefault**
  Defines the default next state of a ticket after adding a note, in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Note**
  Allows adding notes in the ticket free text screen of the agent interface. Can be overwritten by Ticket::Frontend::NeedAccountedTime.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###NoteMandatory**
  Sets if note must be filled in by the agent. Can be overwritten by Ticket::Frontend::NeedAccountedTime.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Subject**
  Defines the default subject of a note in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Body**
  Defines the default body of a note in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###InvolvedAgent**
  Shows a list of all the involved agents on this ticket, in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###InformAgent**
  Shows a list of all the possible agents (all agents with at least ro permissions on the queue/ticket) to determine who should be informed about this note, in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###IsVisibleForCustomerDefault**
  Defines if the note in the ticket free text screen of the agent interface is visible for the customer by default.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Priority**
  Shows the ticket priority options in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###PriorityDefault**
  Defines the default ticket priority in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Title**
  Shows the title field in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###FormDraft**
  Allows to save current work as draft in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###HistoryType**
  Defines the history type for the ticket free text screen action, which gets used for ticket history.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###HistoryComment**
  Defines the history comment for the ticket free text screen action, which gets used for ticket history.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Widgets###Description**
  TicketActionCommon widget that displays the current action description.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Widgets###TicketInformation**
  TicketActionCommon widget that displays ticket information.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###Widgets###CustomerInformation**
  TicketActionCommon widget that displays customer information.

* **Loader::Module::AgentTicket<SCREEN_NAME>###002-Ticket**
  Loader module registration for the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###DynamicField**
  Dynamic fields shown in the ticket free text screen of the agent interface.

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###RichTextWidth**
  Defines the width for the rich text editor component for this screen. Enter number (pixels) or percent value (relative).

* **Ticket::Frontend::AgentTicket<SCREEN_NAME>###RichTextHeight**
  Defines the height for the rich text editor component for this screen. Enter number (pixels) or percent value (relative).
