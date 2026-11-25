.. meta::
   :description: Znuny Customer Interface — a self-service portal for creating, viewing, answering and searching tickets and starting processes, with self-registration and password reset.
   :keywords: znuny customer interface, customer portal, self service, customer user, ticket portal, create ticket, customer dashboard

Customer Interface
##################

The customer user interface is a separate interface meant to provide access to resources such as, but not limited to, tickets. If self-registration is enabled, customer users can register with your system and begin creating requests. In addition, your customers can request automatic password resets from the login page, if they've forgotten their password. In this section we want to dive into the customer interface and it's functions.

.. versionchanged:: 7.5.1

    Customer self-registration is disabled by default. Enable it with the system configuration setting ``CustomerPanelCreateAccount``. The registration only accepts the fields listed in ``CustomerPanelCreateAccount::AllowedFields`` (default: title, first name, last name and email address). The login and the customer ID are taken from the email address. Registrations are rate-limited per IP address: ``CustomerPanelCreateAccount::RateLimitMaxAttempts`` attempts (default ``5``, ``0`` disables the limit) within ``CustomerPanelCreateAccount::RateLimitWindow`` seconds (default ``600``).

The main interface components are:

Header
  Includes a customizable logo and company headline.
User menu
  Access to logout and user preferences.
Navigation menu
  Access to all available modules.
Content area
  Where the selected module will display its content.

Customer User Navigation
************************

The full navigation menu, as seen below, may vary from your system depending on configuration and add-ons. Each add-on installed can bring new menu items with it. The functions are described in more detail in the following sections.

Create Process Ticket
Create Ticket
My Tickets
Company Tickets
Ticket Search

Customer User Functions
***********************

Using the provided interface can be a great enhancement for your customer service experience, as it gives your customers more control over their tickets and replaces the need for keeping old emails, by providing online access to their entire history of communication with your organization. Collecting required data during process start or ticket creation is just one of the benefits. The following features are offered out-of-the-box:


.. toctree::
    :maxdepth: 2

    customer_user_dashboard/index
    customer_user_preferences/index
    starting_processes/index
    process_categories/index
    creating_tickets/index
    viewing_tickets/index
    answering_tickets/index
    searching_tickets/index
