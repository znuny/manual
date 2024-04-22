.. _Pagenavigation admin_systemconfiguration_timezones_index:

Managing Time Zones
###################

Time zones are important and the concept of how they are implemented is just as important to understand. Applying time zone information to your instance allows users in an international environment to use and reflect data in a meaningful way.

Database Entries
****************

The following table information is always saved in UTC, regardless of other setings.

- create_time
- change_time

System Defaults
***************

For best results, the system default - ``OTRSTimeZone``, should be set to the same time as your server time. We highly recommend using UTC for your application and servers.

Personal Settings
*****************

Each user and customer user can choose their own time zone in the preferences. A user will be notified that the time zone setting has not been selected yet after the first login. The setting ``UserDefaultTimeZone`` can be used to apply time zone settings to the front end for users who've not yet set a preference.

Statistics
**********

Statistics will run using the configured time zone at run time.

Cron Schedules
**************

Application Crontab
===================

You'll confront these configurations mostly when scheduling the daemon tasks in the system configuration. These run based on the OTRSTimeZone setting.

Cron scheduling, represented as follows, will be always run according to the system clock.

.. code-block:: shell

   # ┌───────────── minute (0 - 59)
   # │ ┌───────────── hour (0 - 23)
   # │ │ ┌───────────── day of the month (1 - 31)
   # │ │ │ ┌───────────── month (1 - 12)
   # │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
   # │ │ │ │ │                                       7 is also Sunday on some systems)
   # │ │ │ │ │
   # │ │ │ │ │
   # * * * * * <command to execute>


.. note::

   Scheduled generic agents also use a cron like schedule. You can configure them to run at certain times each day. No other configuration is possible via the front end. This time is based on the operating system time, always.


System Calendars
****************

Each system calendar can be configured to use an individual time zone. This allows each of the calendars working hours to properly compute the escalation based on its calendar working hours and holidays.

Example Setup
*************

- OTRSTimeZone = Europe/Berlin
- UserDefaultTimeZone = UTC
- Personal Setting = Europe/London
- Report Configuration = America/New_York
- Queue or Service Level Esclation = When viewed, adjusted time is shown based on user settings. Calculation is done against the calendar's time zone setting.

Ticket created time is: 14:00

- All database times are written in time zone Europe/Berlin (14:00)
- The front end for new users will show 12:00 (UTC)
- The front end (for the user in the above example) will show adjusted time 13:00 (Europe/London)
- The report is shown in the selected time zone (see example above)

.. code-block::

   "Number","Ticket#","TicketID","Age","Title","Created","Last Changed","Close Time","Queue","State","Priority","Customer User","Customer ID","Accounted time","EscalationDestinationIn","EscalationDestinationDate","EscalationTimeWorkingTime","EscalationTime","FirstResponse","FirstResponseInMin","FirstResponseDiffInMin","FirstResponseTimeWorkingTime","FirstResponseTimeEscalation","FirstResponseTimeNotification","FirstResponseTimeDestinationTime","FirstResponseTimeDestinationDate","FirstResponseTime","UpdateTimeEscalation","UpdateTimeNotification","UpdateTimeDestinationTime","UpdateTimeDestinationDate","UpdateTimeWorkingTime","UpdateTime","SolutionTime","SolutionInMin","SolutionDiffInMin","SolutionTimeWorkingTime","SolutionTimeEscalation","SolutionTimeNotification","SolutionTimeDestinationTime","SolutionTimeDestinationDate","SolutionTimeWorkingTime","First Lock","Lock","StateType","UntilTime","UnlockTimeout","EscalationResponseTime","EscalationSolutionTime","EscalationUpdateTime","RealTillTimeNotUsed","Number of Articles","Process","Activity","Attachment","Ticket Calendar StartTime","Ticket Calendar EndTime","Partner"
   "1","20231016116000015","2","13 m","Test Ticket","2023-10-16 09:40:43 (America/New_York)","2023-10-16 09:40:43 (America/New_York)","","Misc","open","3 normal",,,"0","","","0","0","","0","0",,"0",,,,,"0",,"0","","0",,"","0","0",,"0",,,"",,"","unlock","open","0","0","0","0","0","0","1","","","","","",""
   "2","2021012710123456","1","5 h 34 m","Znuny says hi!","2023-10-16 04:19:48 (America/New_York)","2023-10-16 06:44:36 (America/New_York)","","Raw","new","3 normal","AC189429","Elfy.Hoyer@domain.tld","0","","","0","0","","0","0",,"0",,,,,"0",,"0","","0",,"","0","0",,"0",,,"",,"2023-10-16 06:43:42 (America/New_York)","unlock","new","0","1697460273","0","0","0","0","1","","","","","",""

Special Consideration
*********************

Out-of-office
=============

Out-of-office is just a date, which means that if you work in a follow-the-sun environment, you may not see that a colleague who is shown out-of-office earlier or later than expected, based on the server's time zone setting.

Viewable Dates
**************

Date pickers set dates based upon the ``UserTimeZone`` order. In the front end, dates will be shown adjusted and with the selected time zone.

i.e. 01/02/2024 13:13 (Europe/Berlin)
