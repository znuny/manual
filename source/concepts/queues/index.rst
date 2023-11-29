What are Queues
###############

A queue is a permission object which contains tickets. These are assigned to a specific group of users based upon your organizational requirements. It could be your team is organized by:

- department
- service
- product
- country

You can view the tickets in a queue by navigating to the **Queue view** under the **Ticket** menu. Users can prefer queues In Znuny, a queue is a collection of tickets that are grouped together based on a common attribute, such as a department or a service. You can view the tickets in a queue by navigating to the **Queue view** under the **Ticket** menu. By default, this list aggregates all queues selected as **My Queues** under the **Personal Settings** menu. You may further filter tickets by drilling down the queue structure.

Communication between teams, is done by moving or splitting a ticket, into another queue. Each queue has its own unique set of identifying features and options used to create a team of users for servicing customer users.

Here a typical queue structure:

.. mermaid:: 

    graph TD

        SD[Service Desk] --> SL[Second Level]
        SD[Service Desk] --> OB[On-Boarding]
        DEV[Development] --> 3L[Third Level]
        SALES[Sales] --> EMEA[Europe]
        SALES[Sales] --> US[North America]

Typical Workflow
*****************

An email is received by service@example.com and delivered to the Service Desk queue. It is then moved to the service desk team's second level department for further assistance.

