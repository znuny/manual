Provider
########
.. _PageNavigation admin_webservices_provider_index:

HTTP-Header Authentication 
**************************

To prevent revealing of information like passwords, usernames, etc, in the URL for HTTPD methods like GET it is possible to transfer the authentication fields in custom HTTP header. 

These headers are:

- X-OTRS-Header-UserLogin
- X-OTRS-Header-CustomerUserLogin
- X-OTRS-Header-SessionID
- X-OTRS-Header-Password
- X-OTRS-Header-ImpersonateAsUser


.. note:: The authentication feature `ImpersonateAsUser` is not included in this version.


Sending e-mails 
***************

When an article is created with the operation **TicketCreate** or **TicketUpdate** can now additionally be sent via e-mail.

The following parameters are available for this purpose:

.. code-block:: none
	
	ArticleSend => 1,
	To          => 'email@example.com',  # E-mail address to which the item should be sent.
	Cc          => 'email2@example.com', # Optional 
	Bcc         => 'email3@example.com', # Optional

Signing or encrypting with S/MIME or PGP is also possible:

.. code-block:: none

	# Signing and encryption, only used when ArticleSend is set to 1
	'Sign' => {
		'Type'    => 'PGP',
		'SubType' => 'Inline|Detached',
		'Key'     => '81877F5E',
		'Type'    => 'SMIME',
		'Key'     => '3b630c80',
	},
	'Crypt' => {
		'Type'    => 'PGP',
		'SubType' => 'Inline|Detached',
		'Key'     => '81877F5E',
		'Type'    => 'SMIME',
		'Key'     => '3b630c80',
	},

..


.. code-block:: JSON
	:caption: request example

	"Article": {
		"ArticleSend": "1",
		"To": "email@example.com",
		"Body": "We welcome you to Znuny, our ticketing solution...",
		"Charset": "utf-8",
		"CommunicationChannelID": "1",
		"ContentType": "text/plain; charset=utf-8",
		"IsVisibleForCustomer": "1",
		"MimeType": "text/plain",
		"Subject": "Znuny says hi!"
	}

..

Time Accounting operation
*************************

This operation returns the accounted times which a specific agent has entered. Besides the start and end date, the credentials of an agent with rw permission for the group `timeaccounting_webservice` are required. The timezone for the start and end date is the same like you system configuration setting for `OTRSTimeZone`.


.. code-block:: JSON
	:caption: request example

	{
		"TimeAccountingStart": "2021-01-01 10:00:00",
  		"TimeAccountingEnd": "2022-01-01 10:00:00",
  		"TimeAccountingUserLogin": "root@localhost",
  		"UserLogin": "user",
  		"Password": "password",
	},

..

.. code-block:: JSON
	:caption: response example

	"TimeAccountingResult": [
	        {
	            "TicketNumber": 	"2021012710123456",
	            "TicketCustomerID": "CustomerUserID"
	            "TicketTitle":  	"Znuny says hi!",
	            "Queue":        	"Raw",
	            "Created":      	"2021-08-05 08:00:00",
	            "TimeUnit":     	"120.00",
	        },
	        {
	            "TicketNumber": 	"2021012710123456",
	            "TicketCustomerID": "CustomerUserID"
	            "TicketTitle":  	"Znuny says hi!",
	            "Queue":        	"Raw",
	            "Created":      	"2021-08-05 08:00:00",
	            "TimeUnit":     	"30.00",
	        },
	    ],


There is a web service ready when you add a new web service. You might choose between REST and SOAP as transport method:

.. image:: images/webservice_timeaccounting_ready.png
         :width: 100%
         :alt: prepared TimeAccounting web service selection

And to bring you up to speed, here's a small client in PowerShell:

.. code-block:: powershell

    $uri  = "https://YOURFQDN/otrs/nph-genericinterface.pl/Webservice/TimeAccountingREST"
    $headers = @{}
    $headers.Add("Accept", "application/json")
    $headers.Add("Content-Type", "application/json")
    
    $Request = @{
        UserLogin = "yourusername"
        Password  = "AverYSavePassW0rD"
        TimeAccountingUserLogin = "theagentlogin"
        TimeAccountingStart = "2021-07-01 00:00"
        TimeAccountingEnd = "2021-08-01 00:00"
    }
    $json = $Request | ConvertTo-Json
    $Response = Invoke-RestMethod -Method Post -Headers $Headers -Uri "$uri/TimeAccountingGet" -Body $json
    
    $Response | ConvertTo-Json | Write-Host

..


OutOfOffice operation
**********************

the operation **User::OutOfOffice** allows you to set and remove the out of office preferences for agents. All you need is a CVS file containing the information. Usually, this is generated with data form other system like MS Exchange, HR systems, etc.

The CSV file requires a specific header with the entries:

- **UserEmail** or **UserLogin** to specify the agent
- **EndTime** or **EndDate**
- **StartTime** or **EndData**
- **Enabled** contains a yes or no to enable or disable the out of office state

The entries should be enclosed by **"** and separated with an **,** 

.. code-block:: 
	:caption: CSV example 1

	"UserEmail","EndTime","StartTime","Enabled"
	"agent_email@your.tld","30.03.2016 01:02:03","20.03.2016 01:02:03","yes"

..

.. code-block:: 
	:caption: CSV example 2


	"UserLogin","EndDate","StartDate","Enabled"
	"agent1","2016-03-30","2016-03-20","yes"

..


Here is an example data for a valid request:

.. code-block:: JSON

	{
	  "OutOfOfficeEntriesCSVString": "UserEmail,OutOfOffice,StartDate,EndDate\r\nroot@localhost,1,,\r\njd@test.znuny.com,1,2021-08-01,2021-07-31\n",
	  "UserLogin": "user",
	  "Password": "password"
	}

...

The user in the request requires rw permission to the group admin.

.. code-block:: Powershell
	:caption: PowerShell example request for this operation

	$uri  = "https://YOURFQDN/otrs/nph-genericinterface.pl/Webservice/OutOfOffice"

	$headers = @{}
	$headers.Add("Accept", "application/json")
	$headers.Add("Content-Type", "application/json")

	$CSV = Get-Content outofoffice.csv -Raw | Out-String

	$Request = @{
	    UserLogin = "root@localhost"
	    Password  = "root"
	    OutOfOfficeEntriesCSVString = $CSV
	}
	$json = $Request | ConvertTo-Json
	$Response = Invoke-RestMethod -Method Post -Headers $Headers -Uri "$uri/OutOfOffice" -Body $json

	$Response | ConvertTo-Json | Write-Host

..
