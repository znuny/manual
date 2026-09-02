.. meta::
   :description: Znuny glossary — plain-language definitions of agents, customers, queues, states, SLAs, and ITIL service management terms as they apply to Znuny.
   :keywords: znuny glossary, ticket system terms, itil znuny, service desk terms, agent, queue, sla, escalation, znuny definitions

.. _PageNavigation glossary_index:

Glossary
########

Plain-language definitions of the terms used throughout Znuny, together with notes on how ITIL and IT service desk concepts map to Znuny features.

----

Core Ticket Concepts
********************

Ticket
    The central record in Znuny. A ticket represents a single request, incident, task, or case from creation through to resolution. Every piece of communication, every state change, and every assignment is recorded against the ticket. In ITIL terms a ticket may represent an *incident record*, a *service request*, or a *change record* depending on how the system is configured.

Ticket Number (TN)
    A unique, system-generated reference number assigned to every ticket at creation (for example, ``2024011234567890``). Ticket numbers are shown in the UI, included in email subjects, and used by customers to reference their requests. The format is configurable via SysConfig.

Article
    A single communication record attached to a ticket. An article may be an inbound email, an outbound reply, a phone-call note, an internal note, or a chat message. The full conversation history on a ticket is its collection of articles. In service desk terms an article is equivalent to a *journal entry* or *work note*.

Internal Note
    An article that is visible to agents only and is not shown in the customer portal. Used for internal team communication about a ticket. Equivalent to a *private note* or *work note* in other service desk tools.

External Note
    An article that is visible to both agents and the customer in the portal. Used when you want to record information that the customer should also be able to read.

Follow-up
    A reply or additional communication sent to a ticket after it has been closed. Depending on queue configuration, a follow-up may reopen the ticket, create a new ticket, or be rejected. Configurable per queue via the *Follow-up possible* setting.

Merge
    The action of combining two tickets into one. All articles and history from the source ticket are moved to the target ticket. The source ticket is then closed with state type *merged* and a cross-reference is added.

Split
    The action of creating a new ticket from an existing article. The new ticket inherits the article as its first communication. Used to separate unrelated issues that arrived in the same conversation thread.

Pending Time
    A point in time set on a ticket in a *pending* state. Depending on the state type, the pending time either triggers a reminder notification to the owner (``pending reminder``) or automatically transitions the ticket to another state (``pending auto``).

Archive Flag
    A flag that marks a ticket as archived. Archived tickets are excluded from standard views and queue counts but remain accessible via search. Used to move old, resolved tickets out of the active working view.

Reply / Respond
    The action of composing and sending an outbound email from a ticket, directed at the customer or the original sender. Creating a reply generates a new article on the ticket and resets the first-response or update escalation clock if one was running. Also referred to as *Respond* in some ticket screens.

Forward
    The action of sending an existing article — typically an inbound email — on to a third party who is not the original sender. Forwarding creates a new outbound article on the ticket but does not change the ticket state or reset escalation clocks. Useful for escalating to an external team or supplier.

Bounce
    The action of re-sending an email article to a different address as if it had originally come from that address. Unlike a forward, a bounced message preserves the original sender headers, making it appear to the recipient as though the message came directly from the customer. Used when a ticket has been received in the wrong queue and needs to be redirected externally.

Watching / Watcher
    An agent who has subscribed to receive notifications about a ticket without being its owner or responsible agent. Equivalent to *following* a record in other tools. Managed via the ticket watcher feature.

----

Ticket Lifecycle (States)
*************************

State
    The current lifecycle position of a ticket. Every ticket has exactly one state at any given time. States are configured by administrators. Common default states include *new*, *open*, *pending reminder*, *closed successful*, and *closed unsuccessful*.

State Type
    The behavioural category of a state. State types are fixed by the system and control how the ticket behaves regardless of the display name of the state. Administrators assign state types when creating or editing states.

    The standard state types are:

    - **new** — Ticket has been created but not yet worked on.
    - **open** — Ticket is actively being worked on.
    - **pending reminder** — Ticket is on hold; a notification fires at the pending time.
    - **pending auto** — Ticket transitions automatically to another state at the pending time.
    - **closed** — Ticket is resolved and no longer active.
    - **removed** — Ticket is hidden from normal views (soft-deleted).
    - **merged** — Ticket has been combined into another ticket.

Priority
    A classification of a ticket's urgency or importance. Priorities are configurable and are displayed in colour-coded lists. In ITIL terms priority is typically derived from a combination of *impact* and *urgency*; in Znuny it is a single selectable attribute. Default priorities range from 1 (very low) to 5 (very high).

Ticket Type
    An optional classification that describes the category of work the ticket represents. Ticket types must be enabled via SysConfig (``Ticket::Type``) before they appear in ticket screens. Common examples: *Incident*, *Service Request*, *Change Request*, *Problem*.

Escalation
    An automatic alert triggered when a ticket has not been responded to, updated, or resolved within its SLA time limits. Znuny tracks three independent escalation clocks: *first response time*, *update time*, and *solution time*. When a clock expires, the ticket is marked as escalated and configured notifications are sent.

First Response Time
    The maximum elapsed time from ticket creation to the first agent response. Defined per queue and SLA. Tracked via the ``escalation_response_time`` field on the ticket.

Update Time
    The maximum elapsed time since the last agent response before an update is due. Defined per queue and SLA.

Solution Time
    The maximum elapsed time from ticket creation to resolution. Defined per queue and SLA. Tracked via the ``escalation_solution_time`` field on the ticket.

----

People
******

Agent
    A member of staff who works tickets in the Znuny agent interface. Agents have logins, belong to groups (directly or via roles), and can own, respond to, and close tickets. In ITIL terms an agent is a *service desk analyst*, *resolver*, or *technician* depending on their role.

Owner
    The agent currently responsible for working a ticket. A ticket has exactly one owner at any time. Assigning ownership is how work is distributed between agents.

Responsible Agent
    An optional secondary agent assigned to a ticket who is accountable for its resolution even if another agent is doing the hands-on work. Useful for supervisory or accountability scenarios.

Customer
    In Znuny, *customer* refers to a customer organisation — the company or entity that is receiving support. Equivalent to an *account* or *company* in CRM terminology. Stored in the ``customer_company`` table.

Customer User
    An individual contact person associated with a customer organisation. The customer user is the person who raises and tracks tickets via the customer portal. In ITIL terms the customer user is the *user* or *end user*. Stored in the ``customer_user`` table.

    .. note::

        Znuny distinguishes between *customer* (the organisation) and *customer user* (the individual). A single customer organisation can have many customer user contacts.

----

Interfaces and Screens
**********************

Agent Interface
    The web-based application used by agents to work tickets, run reports, manage the calendar, and access administrative functions. Accessed at ``/index.pl`` by default. Also referred to as the *Agent Portal*. In ITIL terms this is the *service desk application* or *resolver interface*.

Customer Interface
    The self-service web portal where customer users log in to create tickets, check status, reply to agents, and track their requests. Accessed at ``/customer.pl`` by default. Also referred to as the *Customer Portal* or *Self-Service Portal*.

Public Interface
    A limited web interface accessible without authentication. The public interface typically exposes only a ticket status check (so customers can look up a ticket by number without logging in) and can optionally serve a public FAQ. Accessed at ``/public.pl`` by default.

Screen
    A specific page or form within one of the Znuny interfaces. Examples include the *New Phone Ticket* screen, the *Ticket Zoom* screen, and the *Close Ticket* screen. Screens are configurable — administrators can control which fields appear, which are mandatory, and which are hidden using SysConfig settings. The set of fields shown on a given screen is called its *layout*.

Ticket Zoom
    The primary screen for working a ticket. The ticket zoom shows all articles in the conversation thread, the ticket's current attributes (state, priority, queue, owner), and provides action buttons for replying, forwarding, adding notes, and changing ticket properties.

Dashboard
    The landing page of the agent interface. The dashboard displays configurable widgets — queue overviews, ticket lists, statistics graphs, and calendar events — giving each agent a summary of their work at a glance. Each agent can personalise their own dashboard widget layout.

Admin Interface
    The administration section of the agent interface, accessible to agents with the appropriate group permissions. The admin interface provides access to all system configuration modules including queues, users, SLAs, dynamic fields, web services, and system configuration.

Activity (Web Notification)
    A real-time, in-browser alert shown to agents while they are logged into the agent interface. Activity notifications appear via the bell icon in the top navigation bar and cover events such as being mentioned in a note, being assigned a ticket, or receiving a new message. Unlike email *notifications* (which are sent regardless of whether the agent is online), activity alerts are displayed live in the browser session and do not require an email to be sent. Agents can review their recent activity from the notification centre without leaving the current screen.

Rich Text Editor / Auto-completion
    The rich text editor used when composing email articles and notes in Znuny is built on CKEditor. It provides text formatting (bold, italic, lists, tables, links), spell-check, and image embedding. Several fields in the agent interface also support **auto-completion**: as an agent begins typing a customer name, agent name, or email address in a recipient or owner field, the system queries the database and displays matching suggestions in a dropdown. Selecting a suggestion populates the field without the agent needing to type the full value. Auto-completion is active on the *To*, *Cc*, and *Bcc* fields of email articles and on owner/responsible assignment fields.

----

Organisation and Routing
************************

Queue
    The primary organisational unit for routing tickets. Every ticket belongs to exactly one queue. Queues define which agents can work a ticket (via group permissions), which email address sends replies, which escalation times apply, and how follow-ups are handled. In ITIL terms a queue is equivalent to an *assignment group* or *support group*.

Group
    A permission scope that controls which agents can access which queues and admin modules. Groups do not appear directly in ticket screens — they work behind the scenes. Every queue is associated with exactly one group. Agents gain access to a queue by having the appropriate permission on its group.

Role
    A named collection of group permissions that can be assigned to multiple agents. Roles are the recommended way to manage permissions at scale: instead of assigning each agent to groups individually, assign agents to roles, and configure the group permissions on the role.

Service
    An optional classification that links a ticket to a specific IT service being provided to the customer. Services can be associated with SLAs and with specific customer users or customer companies. Must be enabled in SysConfig before appearing in ticket screens.

SLA (Service Level Agreement)
    A configured set of response and resolution time targets that apply to a ticket. SLAs can be associated with services and/or queues. When a ticket's SLA times are exceeded, escalation rules fire. In ITIL terms an SLA is an agreement between the service provider and the customer about service quality.

Calendar (SLA / Business Hours Calendar)
    A working-hours schedule used to calculate SLA and escalation times. Calendars define which hours of the day and which days of the week count as business hours, the time zone, and any public holidays. SLA clocks only advance during the business hours defined in the assigned calendar. Configured in *Admin → Calendars*. Not to be confused with the *Appointment Calendar* feature.

Appointment Calendar
    A scheduling and resource-management feature that allows agents to create, view, and share calendar appointments — similar to a shared team calendar in Outlook or Google Calendar. Appointment calendars are separate from SLA calendars: they manage team schedules, meeting bookings, and on-call rotas rather than SLA time calculations. Appointments can be linked to tickets. Configured in *Admin → Appointment Calendar Management*.

Working Hours
    The hours within a business day during which SLA and escalation time counts. Defined as part of an SLA *Calendar*. Outside of working hours — evenings, weekends, and public holidays — escalation clocks are paused. Working hours are configured per calendar, allowing different teams or customers to operate on different schedules.

System Address
    The email address that a queue uses to send outbound messages and receive inbound ones. A queue must have a system address configured in order to handle email.

Salutation / Signature
    Configurable text blocks that are automatically prepended (salutation) or appended (signature) to agent email replies. Assigned per queue.

----

Communication
*************

Communication Channel
    The medium through which an article was created or received. Standard channels are: *Email* (MIME), *Phone* (phone-call note), *Internal* (internal note), and *Chat*. The channel determines which storage backend is used for the article's content.

Auto Response
    An automatic reply sent to the customer when a defined event occurs — for example, when a ticket is created, a follow-up is received, or a ticket is rejected. Auto responses are configured per queue and per event type.

Notification
    A system-generated message sent to agents or customers when a ticket event occurs. Notifications are configured in the *Ticket Notifications* admin module and can be triggered by state changes, escalations, assignments, new articles, and many other events. Each notification uses a *notification template* for its subject and body, supporting placeholder variables that are resolved at send time.

Template (Standard Response Template)
    A pre-written text block that agents can insert into a reply or note. Templates save time for frequently repeated responses such as acknowledgements, instructions, or standard resolutions. Templates are assigned to queues — agents can choose from the templates available in the current ticket's queue when composing an article. Not to be confused with *auto responses* (which fire automatically) or *notification templates* (which format system-generated emails).

Postmaster Filter
    A rule that automatically processes inbound emails before they create or update tickets. Filters can set ticket fields, route to specific queues, reject mail, or trigger other actions based on email headers and content.

----

Reporting and Statistics
************************

Statistics (Stats)
    The built-in reporting module, accessible to agents via *Reports → Statistics* and configurable by administrators via *Admin → Statistics*. Statistics produce structured tabular or chart outputs from ticket data. Three report types are available:

    - **Dynamic List** — A row-per-ticket report. Each column is a ticket attribute or dynamic field. Output can be sorted, filtered by date range, and exported to CSV or Excel.
    - **Dynamic Matrix** — A pivot-style cross-tabulation. Rows and columns each represent a ticket attribute (e.g. queue × state, or month × priority), and cells contain counts or sums.
    - **Static** — A report generated by a custom Perl module, used for calculations that cannot be expressed as a dynamic list or matrix.

    Statistics can be run on demand, scheduled for automatic generation, or embedded as widgets on agent dashboards.

Report
    The output produced by running a Statistic. Reports can be viewed in the browser, downloaded as CSV or Excel files, or emailed automatically on a schedule. In Znuny the terms *report* and *statistic* are used interchangeably in the UI.

Dashboard Widget (Statistics)
    A statistics graph or ticket count summary embedded directly in the agent dashboard. Agents can add, remove, and configure which widgets appear on their personal dashboard. Common examples include a ticket count by state, a bar chart of incoming tickets per day, and an escalation overview.

----

Configuration
*************

Dynamic Field
    A custom field that extends the data recorded on a ticket, article, or customer user. Dynamic fields can be text boxes, date pickers, dropdowns, multi-select lists, and more. They are created by administrators and can be shown on ticket screens, search forms, and reports.

Generic Agent
    An automated job that runs on a schedule or in response to ticket events. Generic Agent jobs can search for tickets matching defined criteria and then automatically update their fields, send notifications, or execute custom Perl modules. Equivalent to a *business rule* or *automation rule* in other tools.

Process
    A structured workflow built using the Process Management module. A process guides a ticket through a defined sequence of activities and transitions, with conditions and automated actions at each step. Used for implementing workflows such as change approval, onboarding, or multi-stage request fulfilment.

ACL (Access Control List)
    A rule that restricts which values are available in ticket fields depending on conditions such as the current queue, state, customer, or agent. ACLs are used to enforce business rules and simplify agent screens by hiding irrelevant options.

SysConfig (System Configuration)
    The central configuration store for all Znuny settings. Administrators access it via *Admin → System Configuration*. Settings can be searched, overridden from their defaults, and deployed to the running system.

OPM
    The file format for Znuny add-on packages (*.opm*). An OPM file contains the code, database changes, configuration, and documentation for a single installable package. Packages are managed via *Admin → Package Manager*.

Valid / Invalid
    Most configuration objects in Znuny (queues, agents, states, priorities, groups, roles, etc.) carry a *validity* flag. Setting an object to *invalid* disables it without deleting it, removing it from active screens while preserving its historical data and associations.

----

Integration and Security
************************

Web Service
    A configured integration point that allows Znuny to exchange data with external systems using HTTP/HTTPS. A web service defines how Znuny acts as a *provider* (receiving calls from external systems) and/or a *requester* (making calls to external systems). Web services are configured in *Admin → Web Services*.

Generic Interface
    The underlying framework in Znuny that powers web service integrations. The Generic Interface handles the transport layer (HTTP, REST, SOAP), data mapping (transforming field names and values between Znuny and the external system), and the operation or invoker logic. It is the technical name for what administrators configure through the web service admin screens.

    - **Provider** — Znuny receives an API call from an external system and performs an operation (e.g. create a ticket, update a ticket, fetch ticket data).
    - **Requester** — Znuny makes an API call to an external system in response to a ticket event (e.g. notify a third-party system when a ticket is closed).
    - **Operation** — A specific action that Znuny can perform when acting as a provider (e.g. ``TicketCreate``, ``TicketUpdate``).
    - **Invoker** — A specific call that Znuny makes to an external system when acting as a requester.
    - **Mapping** — A transformation applied to inbound or outbound data to convert field names, values, or structure between Znuny and the external system.

SAML (Security Assertion Markup Language)
    An XML-based open standard for exchanging authentication and authorisation data between an identity provider (IdP) and a service provider (SP). When SAML is configured in Znuny, users authenticate with their organisation's single sign-on (SSO) system (such as Microsoft Entra ID, Okta, or ADFS) rather than entering a Znuny-specific username and password. Znuny acts as the SAML service provider; the organisation's identity platform acts as the IdP.

OAuth 2.0
    An open authorisation framework that allows Znuny to obtain access tokens from an identity provider on behalf of a user or application. In Znuny, OAuth 2.0 is primarily used for authenticating outbound email connections (such as Microsoft 365 or Google Workspace) via the *Office 365 / Google OAuth* mail account type, replacing traditional username/password SMTP authentication. Configured in *Admin → OAuth2 Token Management*.

Two-Factor Authentication (2FA)
    A login security method that requires a second verification step in addition to a password. When 2FA is enabled in Znuny, agents must provide a time-based one-time password (TOTP) generated by an authenticator app (such as Google Authenticator or Microsoft Authenticator) after entering their username and password. 2FA can be enforced system-wide or made optional per agent via SysConfig.

----

ITIL and Service Desk Term Mapping
***********************************

The table below maps common ITIL Foundation and general IT service desk terms to their Znuny equivalents.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - ITIL / Service Desk Term
     - Znuny Equivalent
     - Notes
   * - Incident
     - Ticket (type: Incident)
     - Requires the ``Ticket::Type`` SysConfig setting to be enabled. The *Incident* type is not created by default — an administrator must create it.
   * - Service Request
     - Ticket (type: Service Request)
     - Same as above. Service Requests are often fulfilled via Znuny *Processes* for structured approval workflows.
   * - Problem Record
     - Ticket (type: Problem)
     - Znuny has no native Problem Management module. Problem records are typically implemented as a ticket type, sometimes with dynamic fields to capture root cause and known errors.
   * - Change Record
     - Ticket (type: Change) or Process
     - Simple changes can use a ticket type. Structured changes with approval gates are better implemented as a *Process* in the Process Management module.
   * - Known Error
     - Ticket with a custom dynamic field or state
     - No native Known Error Database. Typically implemented with a custom dynamic field or a dedicated queue.
   * - Service Catalog
     - Services + Processes
     - The *Service* module provides a catalogue of IT services. Structured request forms are built with *Processes*.
   * - Assignment Group
     - Queue
     - A queue routes work to a set of agents. Group permissions control which agents can access the queue.
   * - Resolver / Analyst / Technician
     - Agent
     - The person working the ticket.
   * - End User / User
     - Customer User
     - The person who raised the ticket and is receiving support.
   * - Customer / Account
     - Customer (organisation)
     - The company or entity that the customer user belongs to.
   * - Requester
     - Customer User
     - The customer user is the requester — the person who opened the ticket.
   * - Priority
     - Priority
     - Direct equivalent. In ITIL, priority is derived from impact × urgency. In Znuny it is set directly; impact and urgency can be modelled as dynamic fields if needed.
   * - Urgency
     - Dynamic Field (custom)
     - Not a built-in field. Implement as a Dropdown dynamic field if your process requires separate urgency and impact inputs.
   * - Impact
     - Dynamic Field (custom)
     - Same as urgency — no built-in equivalent.
   * - Escalation
     - Escalation
     - Direct equivalent. Znuny tracks three clocks: first response, update, and solution.
   * - SLA
     - SLA
     - Direct equivalent. Linked to services and queues; enforced via escalation clocks.
   * - OLA (Operational Level Agreement)
     - Queue SLA / internal SLA
     - Model OLAs using separate SLA records assigned to internal queues.
   * - UC (Underpinning Contract)
     - External SLA record
     - No dedicated UC concept. Model as an SLA record with a descriptive name indicating it covers a third-party supplier.
   * - CMDB / Configuration Item
     - Not built-in to Znuny base
     - A Configuration Management Database is not part of the standard Znuny package. Some add-on packages provide CMDB or asset management functionality.
   * - Work Note / Journal Entry
     - Article (internal note)
     - Internal notes are agent-only articles not visible in the customer portal.
   * - Resolution Note
     - Article (external or internal note on closure)
     - Add a note article when changing the ticket state to closed.
   * - Workaround
     - Article or dynamic field
     - Typically recorded as an article note. Can also be captured in a dedicated dynamic field.
   * - First Contact Resolution (FCR)
     - Custom report via ticket_history
     - No native FCR metric. Derive from tickets closed without a queue transfer after the first agent response.
   * - MTTR (Mean Time To Repair/Resolve)
     - Average solution time report
     - Calculate from ``ticket.create_time`` to the timestamp of the first *closed* history entry in ``ticket_history``.
   * - Business Hours
     - Calendar
     - Calendars define working hours and public holidays used for SLA time calculations.
   * - Service Desk
     - Znuny (agent interface)
     - Znuny *is* the service desk. The agent interface is where the service desk team works tickets.
   * - Self-Service Portal
     - Customer Interface
     - Customers log in via the customer portal to raise tickets, check status, and reply.
   * - Knowledge Base
     - Not built-in to Znuny base
     - A dedicated knowledge base is not part of the standard installation. FAQ add-ons are available.
   * - Ticket / Record
     - Ticket
     - Direct equivalent.
   * - Lock
     - Lock
     - Agents can lock a ticket to themselves to prevent another agent from simultaneously working it.
   * - Watching
     - Ticket Watcher
     - Agents can watch a ticket to receive its notifications without being its owner.
   * - Canned Response / Macro
     - Template (Standard Response Template)
     - Pre-written text blocks assigned to queues that agents insert into replies.
   * - SSO / Single Sign-On
     - SAML or OAuth 2.0
     - Znuny supports both SAML (browser-based SSO) and OAuth 2.0 (token-based auth for mail).
   * - MFA / Multi-Factor Authentication
     - Two-Factor Authentication (2FA)
     - Znuny supports TOTP-based 2FA for agent logins.
   * - API / Integration
     - Web Service / Generic Interface
     - The Generic Interface framework handles all inbound and outbound API calls.
   * - Agent Portal / Resolver Interface
     - Agent Interface
     - The web application at ``/index.pl`` where agents work tickets.
   * - Canned Text / Snippet
     - Template
     - Reusable text blocks available to agents when composing replies.
   * - Forward
     - Forward
     - Direct equivalent — sends an article to a third party, preserving the original content.
   * - Redirect / Re-route
     - Bounce
     - Bounce re-sends a message to a new address with the original sender headers intact.
   * - In-app / Push Notification
     - Activity (Web Notification)
     - Real-time browser alerts shown via the bell icon while an agent is logged in.
   * - Reporting / BI Reports
     - Statistics (Stats)
     - Znuny's built-in Statistics module produces dynamic list, dynamic matrix, and static reports exportable to CSV/Excel.
   * - Scheduled Report
     - Statistic with schedule
     - Statistics can be configured to run automatically and email results on a defined schedule.
   * - Business Hours / Support Hours
     - Working Hours (Calendar)
     - Working hours are defined per SLA calendar and control when escalation clocks advance.
   * - Shared Calendar / Team Calendar
     - Appointment Calendar
     - The Appointment Calendar feature provides team scheduling separate from SLA calendars.
   * - Autocomplete / Type-ahead
     - Auto-completion (CKEditor / agent fields)
     - Typing in recipient, owner, or responsible fields triggers database-backed suggestions.
