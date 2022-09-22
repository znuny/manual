Requester
#########

HTTP::REST options
******************

There are some features added to the HTTP::REST transport:

SSL hostname verification
=========================

Sometimes it is required to disable the verification of the hostname for SSL connections. This should setting be only enabled if you're 100% certain.

Content-Type
============

By default the outgoing request will be JSON. For special use-cases the request can be transformed into the content-type `application/x-www-form-urlencoded`.
Since version 6.2 the content-type `text/xml` is also available.

Additional Request Headers
==========================

If needed, custom HTTP headers can be added to the request. They can also overwrite the default headers which are generated, like `Content-Type`. This option might be useful for certain situation where you need additional headers. Authentication with API keys might be on scenario. The value can be a literal, a system configuration (<OTRS_CONFIG_*>) or a combination of both.


.. image:: images/webservice_Requester-Transport.png
         :name: Requester Transport
         :width: 100%
         :alt: HTTP::REST Transport Settings

Authentication Methods
**********************
.. _AuthenticationMethod generic_interface_invoker:

There are now four ways to authenticate with a provider service.

Client Certificate
    Use a certicifcate and password to authenticate.

.. image:: images/auth_certificate.png
    :alt: Client Cert Settings Image

BasicAuth
    Use a username and password to authenticate.

.. image:: images/auth_basic.png
    :alt: Basic Auth Settings Image

API Key
    Use an additional request header.

.. image:: images/auth_oauth_header.png
    :alt: Header Setting Image

OAuth
    Use an OAuth token.

.. image:: images/auth_oauth.png
    :alt: OAuth Settings Image

.. versionadded:: v6.4.3

    OAuth2 Token authentication