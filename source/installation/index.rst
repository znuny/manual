.. _PageNavigation installupdate_install:

Installation Instructions
#########################

To install Znuny you need:

* A database of your choice:

  * MySQL 8.0 or MySQL 8.4
  * MariaDB 10.3 or newer
  * Postgresql 12 or newer
  * Oracle 19 or newer

* A webserver (Apache)
* Some additional Perl modules, depending on the distribution you are using
* Disabled SELinux when using Red Hat Linux, Rocky Linux, etc.

.. note::

  This manual is based on the assumption that you are installing on a fresh and empty system using MariaDB.

The installation instructions mention Linux distributions. Debian based refers to Debian, Ubuntu and similar. RHEL based refers to Red Hat Enterprise Linux, Rocky Linux, Alma Linux and similar. We use mostly Debian 12 and Rocky Linux 9 in our tests.

Basics
******

.. important::

  For RHEL based distributions SELinux needs to be disabled or set to permissive.

Some basic packages are needed to get going.
This includes the web server, database (MariaDB in this case), cpanminus to install additional Perl modules and Tar to extract the source.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block:: bash

        dnf update -y
        dnf install -y epel-release httpd mariadb mariadb-server cpanminus gcc make dnf-plugins-core tar bash-completion perl-core
        crb enable
      ..

  .. tab-item:: Debian based
    :sync: debian

      .. code-block:: bash

        apt update -y
        apt install -y apache2 mariadb-client mariadb-server tar bash-completion
      ..

.. tab-set::
  .. tab-item:: RPM installation for RHEL based systems

    The installation via RPM

    .. code-block::

      dnf install -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.1.3-01.noarch.rpm


  .. tab-item:: Installation from source archive
  
    The installation from the source takes some more steps:

    .. code-block::

      # Download Znuny
      cd /opt
      wget https://download.znuny.org/releases/znuny-latest-7.3.tar.gz

      # Extract
      tar xfz znuny-latest-7.3.tar.gz

      # Create a symlink
      ln -s /opt/znuny-7.1.3 /opt/znuny

      # Add user for RHEL
      useradd -d /opt/znuny -c 'Znuny user' -g apache -s /bin/bash -M -N znuny

      # Add user for Debian/Ubuntu
      useradd -d /opt/znuny -c 'Znuny user' -g www-data -s /bin/bash -M -N znuny

      # Copy default Config.pm
      cp /opt/znuny/Kernel/Config.pm.dist /opt/znuny/Kernel/Config.pm

      # Set permissions
      /opt/znuny/bin/znuny.SetPermissions.pl

      # As Znuny user - create default cronjobs
      su - znuny
      cd var/cron
      for foo in *.dist; do cp $foo `basename $foo .dist`; done

Install Required Perl Modules
*****************************

Based on your distribution there are several different was to install the needed modules.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      Some of the needed Perl modules are installed, when installing the RPM. You just need
      to complete the missing ones.

      .. code-block::

        yum install -y "perl(Moo)"  "perl(Text::CSV_XS)" "perl(YAML::XS)" "perl(ModPerl::Util)" "perl(Mail::IMAPClient)" "perl(JSON::XS)" "perl(Encode::HanExtra)" "perl(Crypt::Eksblowfish::Bcrypt)" "perl(Data::UUID)" "perl(Date::Format)" "perl(DateTime::TimeZone)" "perl(DateTime)" "perl(DBD::mysql)" "perl(DBI)" "perl(Hash::Merge)" "perl(Net::LDAP)" "perl(Net::DNS)" "perl(Template)" "perl(Template::Stash::XS)" "perl(XML::LibXML)" "perl(XML::LibXSLT)" "perl(XML::Parser)" "perl(Spreadsheet::XLSX)" "perl(Package::Stash)"

        cpanm JavaScript::Minifier::XS CSS::Minifier::XS iCal::Parser

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::

        apt -y install libapache2-mod-perl2 libdbd-mysql-perl libtimedate-perl libnet-dns-perl libnet-ldap-perl libio-socket-ssl-perl libpdf-api2-perl libsoap-lite-perl libtext-csv-xs-perl libjson-xs-perl libapache-dbi-perl libxml-libxml-perl libxml-libxslt-perl libyaml-perl libarchive-zip-perl libcrypt-eksblowfish-perl libencode-hanextra-perl libmail-imapclient-perl libtemplate-perl libdatetime-perl libmoo-perl bash-completion libyaml-libyaml-perl libjavascript-minifier-xs-perl libcss-minifier-xs-perl libauthen-sasl-perl libauthen-ntlm-perl libhash-merge-perl libical-parser-perl libspreadsheet-xlsx-perl libdata-uuid-perl

Database Configuration
**********************

MySQL and Maria DB needs some configuation modifications. If you are using
PostgreSQL you can skip this step:


Create a new configuration file for MariaDB:

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block::

        vi /etc/my.cnf.d/znuny_config.cnf

  .. tab-item:: Debian based
    :sync: debian

      .. code-block::

        vi /etc/mysql/mariadb.conf.d/50-znuny_config.cnf
      ..



.. code-block::
  :caption: Content for the configuration file

  [mysql]
  max_allowed_packet=256M
  [mysqldump]
  max_allowed_packet=256M


  [mysqld]
  innodb_log_file_size = 256M
  max_allowed_packet=256M


.. important::

  The web installer requires a password. Check your Linux distributions manual how to set a passwort for the database admin user.

Restart the MariaDB database to apply the changes

.. code-block::

  systemctl restart mariadb

Webserver Configuration
***********************

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      The Apache config is already in place if you used the RPM install, for the source install create a symbolic link:

      .. code-block:: bash

        ln -s /opt/znuny/scripts/apache2-httpd.include.conf /etc/httpd/conf.d/znuny.conf

      Enable MPM prefork module:

      .. code-block:: bash

        sed -i '/^LoadModule mpm_event_module modules\/mod_mpm_event.so/s/^/#/' /etc/httpd/conf.modules.d/00-mpm.conf
        sed -i '/^#LoadModule mpm_prefork_module modules\/mod_mpm_prefork.so/s/^#//' /etc/httpd/conf.modules.d/00-mpm.conf


  .. tab-item:: Debian based
    :sync: debian


      To enable the Znuny Apache configuration you need to create a symlink to our included configuration file.

      .. code-block:: bash

        ln -s /opt/znuny/scripts/apache2-httpd.include.conf /etc/apache2/conf-available/znuny.conf


      Enable the needed Apache modules and configuration:

      .. code-block:: bash

        a2dismod mpm_event
        a2enmod mpm_prefork headers filter perl
        a2enconf znuny


Start / Restart the web server to apply the changes.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel

      .. code-block:: bash

        systemctl restart httpd

  .. tab-item:: Debian based
    :sync: debian

      .. code-block:: bash

        systemctl restart apache2


Now start the web based installer:

``http://HOSTNAME/znuny/installer.pl``

Start-up Configuration
***********************

You should enable the web server and the database to get started on boot.

.. tab-set::
  :sync-group: distribution

  .. tab-item:: RHEL based
    :sync: rhel


      .. code-block:: bash

        systemctl enable mariadb httpd

  .. tab-item:: Debian based
    :sync: debian


      .. code-block:: bash

        systemctl enable mariadb apache2

Enable Znuny Cron
*****************

Switch to the znuny user and fill the crontab

.. code-block:: bash

  su - znuny
  bin/Cron.sh start
