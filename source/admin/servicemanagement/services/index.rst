Managing Services
#################
.. _PageNavigation admin_servicemanagement_services_index:

ITIL 4 defines a service as: “A means of enabling value co-creation by facilitating outcomes that customers want to achieve, without the customer having to manage specific costs and risks.” You can create a service catalog for assignment to tickets and ::ref:`service level agreements <Definition  service_level_agreement>`.

Create a Service
****************

A service is added under Admin > Services.

Service assignment
******************

Under Admin > Customer Users <-> Services you may assign individual customers a service, or set a default service list.

Default Services

If you assign default services, these services will be available for all registered customers. If a customer user has any individual services, then the only these services will be available to them. Customer users with individual services cannot see default services. it is possible to allow default services to be assigned to unknown customers. This can be done in the system configuration. ``Ticket::Service::Default::UnknownCustomer``.

.. note::

    SLA validation can delete an SLA when just the service is updated via a web service TicketUpdate operation, if the current SLA of the ticke does not contain the service updated by the web service.