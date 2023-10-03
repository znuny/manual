.. _PageNavigation annex_stat_values:

Statistics Attributes
#####################

Here's a table to show you different types of values returned by the Ticket Dynamic List, and what they mean within the system.

.. list-table:: Attributes of the ticket list object
   :widths: 20 65 15
   :header-rows: 1

   * - Attribute
     - Description
     - Example value
   * - Accounted time
     - Sum of the accounted time of the ticket's article.
     - 263
   * - Age
     - Age of the ticket in human readable format.
     - 10 d 5 h
   * - Created
     - Create time of the ticket.
     - 2023-02-12 09:12:82
   * - Close Time
     - Time when the ticket was **last** closed.
     -
   * - Customer ID
     - The customer id of the ticket.
     - Example, Inc.
   * - Customer User
     - The id of the ticket's customer user.
     - john.doe@example.com
   * - EscalationDestinationDate
     - The date and time when the ticket is escalated.
     - 2023-10-12 12:45:00
   * - EscalationDestinationIn
     - The relative time from the now to the time of escalation.
     - 4h 30m
   * - EscalationResponseTime
     - Unix timestamp of the response time escalation.
     -
   * - EscalationSolutionTime
     - Unix timestamp of the solution time escalation.
     -
   * - EscalationTime
     - Seconds until the nearest escalation time. Independet from the ecalation type response,update or solution.
     -
   * - EscalationTimeWorkingTime
     - Time in seconds within the defined working time until an escalation.
     -
   * - EscalationUpdateTime
     - Unix timestamp of the update time escalation.
     -
   * - FirstLock
     - Date and time of the first lock and only set when the ticket was locked at least once.
     -
   * - FirstResponse
     - Date and time of the first response.
     -
   * - FirstResponseDiffInMin
     - The difference in minutes between the specified and real first response time.
     -
   * - FirstResponseInMin
     - Time in minutes from the ticket creation until the first response.
     -
   * - FirstResponseTime
     - The timestamp of first response.
     - 
   * - FirstResponseTimeDestinationDate
     - Date and time of the first response escalation.
     -
   * - FirstResponseTimeDestinationTime
     - Unix timestamp of the first response escalation.
     -
   * - FirstResponseTimeEscalation
     - Indicates if there was a first response time escalation with the value 1.
     -
   * - FirstResponseTimeNotification
     - Shows if the defined escalation notification time is activated or not.
     -
   * - FirstResponseTimeWorkingTime
     - Time in seconds within the defined working time until an first response escalation.
     -
   * - Last Changed
     - Last time the ticket has changed.
     - 2022-07-12 21:23:00
   * - Lock
     - Value of the ticket's lock.
     - unlock
   * - Number
     - Current number of this entry in a report.
     - 42
   * - Priority
     - Name of the ticket's priority.
     - 4 high
   * - Queue
     - Name of the queue where the ticket belongs to.
     - Postmaster
   * - RealTillTimeNotUsed
     - Unix timestamp of the pending time.
     - 1696343400
   * - SolutionInMin
     - Time in minutes until the solution escalation.
     -
   * - SolutionTime
     - The time in seconds until a solution time escalation.
     -
   * - SolutionTimeDestinationTime
     - Unix timestamp of SolutionTime.
     -
   * - SolutionDiffInMin
     - The difference in minutes between the specified and real solution time.
     -
   * - SolutionTimeEscalation
     - Shows if the solution time escalation happened with the value 1, and 0 for no esclation.
     -
   * - SolutionTimeNotification
     - Shows if the defined escalation notification time is activated or not.
     -
   * - SolutionTimeDestinationDate
     - Date of the solution time escalation.
     -
   * - SolutionTimeDestinationTime
     - Unix timestamp of the solution time escalation.
     -
   * - SolutionTimeWorkingTime
     - Time in seconds within the defined working time until an solution time escalation.
     -
   * - State
     - The state of the ticket.
     - pending reminder
   * - StateType
     - State type of the ticket.
     - pending auto
   * - TicketID
     - The id of the ticket.
     - 115561
   * - Ticket#
     - The ticket number.
     - 421305912
   * - Title
     - Ticket title.
     -
   * - Type
     - The type of the ticket.
     - Unclassified
   * - UnlockTimeout
     - Time in seconds until the ticket will be unlocked.
     - 872
   * - UntilTime
     - Time in secondes until the pending time of a pending state is reached.
     - 120
   * - UpdateTime
     - Seconds until the update escalation.
     - 
   * - UpdateTimeDestinationDate
     - Date of the update time escalation.
     -
   * - UpdateTimeDestinationTime
     - Unix timestamp of the update time escalation.
     -
   * - UpdateTimeEscalation
     - Indicates with a value of 1 the update time escalated or not (value 0).
     -
   * - UpdateTimeNotification
     - Shows if the defined escalation notification time is activated or not.
     -
   * - UpdateTimeWorkingTime
     - Time in seconds within the defined working time until an update escalation.
     -

..

