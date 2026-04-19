.. meta::
   :description: Ticket types in Znuny — categorize tickets as incident, service request, problem and more to drive workflow automation, prioritization and reporting.
   :keywords: znuny ticket type, incident, service request, problem, ticket categorization, ticket workflow automation

.. _PageNavigation concepts_types_index:

Ticket Types
############

In **Znuny**, a **ticket type** categorizes tickets based on their nature, purpose, or required handling process. 
Different ticket types allow for better **workflow automation, prioritization, and reporting**.
Types are the first of the options ticket data which should be added to any system. By default they are inactive.

**Why Use Ticket Types?**

Ticket types help in:

- **Structuring Support Requests** 
- **Defining Different Workflows** 
- **Service Based Ticketing**
- **Improving Reporting**


Activate Ticket Types
#####################

1. Navigate to Admin->System Configuration
2. Search for ``Ticket::Type`` and enable it.
3. Save
4. Deploy

Standard Ticket Types
#####################

Znuny comes with only the standard ticket type **Unclassified**, but these can be customized and here is a list of recommendations.

+---------------------+--------------------------------------------------------------------------------+
| **Ticket Type**     | **Description**                                                                |
+---------------------+--------------------------------------------------------------------------------+
| **Incident**        | A break/failure in service (e.g., "Printer not working").                      |
+---------------------+--------------------------------------------------------------------------------+
| **Service Request** | A user request for a new service (e.g., "Request new software").               |
+---------------------+--------------------------------------------------------------------------------+
| **Problem**         | A deeper issue causing multiple incidents (e.g., "Server crashes frequently"). |
+---------------------+--------------------------------------------------------------------------------+
| **Change**          | Requests for planned system changes (e.g., "Upgrade database").                |
+---------------------+--------------------------------------------------------------------------------+
| **Complaint**       | A customer dissatisfaction case (e.g., "Billing issue").                       |
+---------------------+--------------------------------------------------------------------------------+
| **Inquiry**         | A general question (e.g., "How do I reset my password?").                      |
+---------------------+--------------------------------------------------------------------------------+

Ticket Types at Work
*********************

1. Assigning a Ticket Type at Creation in the Agent or Customer frontend
2. Re-/Classification after a new ticket has been created
3. Automatic Agent Assignment via Process Management, Generic Agent or Web Service Request or Response
4. Agents can subscribe to services for notifications and work with the service view.

Customizing Ticket Types
************************

- Admins can **add, modify, or remove ticket types** in `Admin > Ticket Settings > Types`.
- New ticket types can be limited or assigned via ACLs or the Ticket Attribute Relationship function.


Ticket Types vs. Priorities vs. Queues
**************************************

Znuny differentiates **ticket types** from:

- **Priorities** (How urgent a ticket is)
- **Queues** (Which department handles the ticket)
- **States** (Open, closed, pending, etc.)

Example: A Real-Life Ticket Workflow
************************************

1. A user submits a ticket:  
   **Type:** *Incident* => **Queue:** *IT Support* → **Priority:** *5 very high*  
2. The agent priorities work on this ticket, and applies the correct SLA.
3. A workaround is offered, which is accepted by the customer.
4. A ticket of type **Problem** is split from the article with the solution.
5. The agent resolves the issue and sets the ticket to **Closed**.
6. The root cause analysis of the **Problem** ticket results in a ticket of type **Change**.
7. The **Problem** ticket is split to the new **Change** ticket and closed.
8. The **Change** is completed and closed.



Best Practices for Using Ticket Types
*************************************

- ✔ Keep types **simple and clear** (avoid too many).  
- ✔ Use **automatic assignment** where possible.
- ✔ Regularly **review types** to match business needs.
