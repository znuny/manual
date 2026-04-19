.. meta::
   :description: Install Znuny Ready2Adopt web services with one click — preconfigured GenericTicketConnectorREST, Mattermost, MS Teams, OutOfOffice and TimeAccounting templates.
   :keywords: ready2adopt web service, znuny web service template, generictticketconnectorrest, mattermost template, ms teams template, webservice quick start

Web Service Quick Start (Ready2Adopt)
#####################################

The ReadyToAdopt Template Web Services are pre-configured web service definitions designed to simplify integration between Znuny and external adoption platforms. These templates provide a structured starting point for connecting Znuny to the ReadyToAdopt API, enabling shelters and adoption agencies to manage pet data and adoption workflows efficiently.

.. important:: 
    
    You will need to adapt them to fit your needs.

The templates include (depending upon use-case)

- predefined operations (Znuny as Provider)
- predefined invokers (Znuny as Request)
- data mappings

By using these templates, you can quickly customize the web service to  facilitate tasks such as retrieving listings, updating ticket statuses, and external notifications to name a few scenarios.

Currently the following templates are available:

- GenericTicketConnectorREST (See Example :ref:`Example Web Service GenericTicketConnectorREST`)
- MattermostNotification (See Example :ref:`Example Web Service Mattermost`)
- MS Teams Notifications (See Example :ref:`Example Web Service MS Teams`)
- OutOfOffice
- TimeAccountingREST
- TimeAccountingSOAP

.. warning:: 
    
    Due to ever changing APIs of the other platforms, these templates may require updates to remain compatible. Always refer to the latest API documentation of the respective platforms when implementing or modifying these templates.

Use a Template
**************

To use a template, follow these steps:

1. Navigate to the Web Service Management in the Admin area.
2. Click on "Add Web Service".
3. Select the desired template from the list of available templates.
4. Click on the button below to import the predefined web service.
5. Configure the web service according to your requirements, including setting up the necessary endpoints, authentication, and data mappings.
6. Test the web service to ensure it functions as expected.
7. Use the debugging tools to troubleshoot any issues that arise during testing.

.. note::

    It may be necessary to adjust pre-configured or add your own XSLT mappings to fit your specific data structure and requirements.

    Log level Debug is recommended when testing and debugging web services. In the examples, the log level is generally set to *Error* to reduce log volume.
