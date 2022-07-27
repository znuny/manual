Securing Communication
######################
.. _PageNavigation admin_security_index:

In this day of age, it is a good idea to secure your communication. It is possible to secure e-mail communication using PGP or S/MIME.

With a few simple configurations to your system, you can use PGP or S/MIME for verification, signing, or encrypting your e-mail.

All system configuration options are found under Ticket -> Crypt

You will need, in addition to the underlying programs and paths:

* Private key(s) to sign outgoing e-mails
* Public key(s) of the recipient(s)
* Passwords for importing private keys

It is possible to administer PGP or S/MIME keys and certificates in the administration area. 


.. note::

    A keyring, for PGP, or certificates and keys, for S/MIME, may be manually loaded to the system. After doing so, you must delete the cache. 

PGP
***

Pretty Good Privacy (PGP) is an encryption program that provides cryptographic privacy and authentication for data communication. PGP is used for signing, encrypting, and decrypting texts, e-mails, etc.

.. important::
    
    Setup requires a valid tool for reading and managing the PGP Keyring. The software only provides the front-end for uploading and using the keys.

To enable PGP for use, you must enable or configure the following options:

* ``PGP`` - Activates PGP in the front-end.
* ``PGP::Bin`` - Location to pgp binary.
* ``PGP::Options`` - Location on key chain.
* ``PGP::Key::Password``- Passwords for each private key.

Acceptable File Format For Public And Private Key:

Generally a ''.key'' file. See ane (example) content.

.. code::
    
    # Valid Public Key Content

    -----BEGIN PGP PUBLIC KEY BLOCK-----

    lQWGBGLX69EBDADgLc4Po64Kx9D80VZnMOWsOR
    .....

    # Valid Private Key Content
    -----END PGP PUBLIC KEY BLOCK-----

    -----BEGIN PGP PRIVATE KEY BLOCK-----

    lQWGBGLX69EBDADgLc4Po64Kx9D80VZnMOWsOR
    .......
    
    -----END PGP PRIVATE KEY BLOCK-----

To add public and private keys, navigate to the administration module for PGP.

.. image:: images/pgp_admin_badge.png
    :alt: Admin PGP Badge


* Click on Add PGP Key.
* Select your key.

.. image:: images/pgp_admin_overview.png
    :alt: Admin PGP Overview

Once uploaded, you can download the keys by clicking on their ID. Additionally, you can download the fingerprint as a text file.

.. note::

    Passwords for using PGP for encryption and decryption are saved in the system configuration and not asked for during import. You will need the ID for the *sec* key.


S/MIME
******

S/MIME (Secure/Multipurpose Internet Mail Extensions) is a standard for public key encryption and signing of MIME data. S/MIME is on an IETF standards track and defined in a number of documents.

Acceptable Formats For Certs And Key

* .CER - DER or Base64 encoded certificate
* .CRT - DER or Base64 encoded certificate
* .DER - DER-encoded certificate
* .PEM - Base64 encoded certificate wrapped in -----BEGIN CERTIFICATE-----" and -----END CERTIFICATE-----

To enable S/MIME for use, you must enable and/or configure the options: 

* ``SMIME`` - Activates SMIME in the front-end.
* ``SMIME::Bin`` - Location to S/MIME binary.
* ``SMIME::CertPath`` - Location to public certs.
* ``SMIME::PrivatePath`` - Location to private certs.

.. note::

    Configuration errors will be shown to the administrator.

.. image:: images/smime_warning.png
    :alt: S/MIME Warning image


To add public and private keys and certificates navigate to the administration module for S/MIME.

.. image:: images/smime_admin_badge.png
    :alt: Admin S/MIME Badge


* Click on Add Private Key.
* Select your key.

.. image:: images/smime_admin_overview.png
    :alt: Admin S/MIME Overview

Once uploaded, you can download the keys by clicking on their HASH. Additionally, you can download the fingerprint as a text file.

View a Certificate:

.. image:: images/certificate.png
    :alt: Certificate Image


Manage Certificate Relations:

.. image:: images/certificate-plus.png
    :alt: Certificate Plus Image

Here you can add private signing certificates and their chain certs.

.. note::

    When adding your private key, you must enter the password. This will allow all queue users to encrypt and decrypt messages without entering the password.


.. note::
    
    When uploading private keys, you will be asked for your password.

.. versionadded:: 6.4

    Key storage has been improved with indexing, improving the performance of systems with large amounts of keys.
