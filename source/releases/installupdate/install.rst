Installation
############
.. PageNavigation installupdate_install:

To install Znuny you need:

- A database of your choice (MySQL, MariaDB, Postgresql)
- MySQL 8 or newer requires Znuny 6.1 or newer
- A webserver (Apache)
- Some additional perl modules, depending on the distribution you are using
- Disabled SELinux when using Red Hat Linux, CentOS, Rocky Linux, etc.

.. note::

  This manual is based on the assumption that you are installing on a fresh and empty system using MariaDB.


Basics
******

Some basic packages are needed to get going.
This includes the web server, database (MariaDB in this case), cpanminus to install additional
Perl modules and TAR to extract the source.

**CentOS / Red Hat**

.. code-block::

  dnf install -y epel-release httpd mariadb mariadb-server cpanminus gcc dnf-plugins-core
  yum config-manager --set-enabled powertools

**Ubuntu / Debian**

.. code-block::

  apt update
  apt install -y apache2 mariadb-client mariadb-server cpanminus

Install an RPM
**************

The installation via RPM

.. code-block::

  # Znuny 7.0.12
  yum install -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-7.0.12-01.noarch.rpm


Install From Source
*******************

The installation from the source takes some more steps:

.. code-block::

  # Download Znuny
  cd /opt
  wget https://download.znuny.org/releases/znuny-latest-7.0.tar.gz

  # Extract
  tar xfz znuny-latest-7.0.tar.gz

  # Create a symlink
  sudo ln -s /opt/znuny-7.0.12 /opt/znuny

  # Add user for RHEL/CentOS
  useradd -d /opt/znuny -c 'Znuny user' -g apache -s /bin/bash -M -N znuny

  # Add user for Debian/Ubuntu
  useradd -d /opt/znuny -c 'Znuny user' -g www-data -s /bin/bash -M -N znuny

  # Copy default Config.pm
  cp /opt/znuny/Kernel/Config.pm.dist /opt/znuny/Kernel/Config.pm

  # Set permissions
  /opt/znuny/bin/znuny.SetPermissions.pl

  # As znuny user - Rename default cronjobs
  su - znuny
  cd /opt/znuny/var/cron
  for foo in *.dist; do cp $foo `basename $foo .dist`; done

Install Required Perl Modules
*****************************

Based on your distribution there are several different was to install the needed modules.

**CentOS / Red Hat**

Some of the needed Perl modules are installed, when installing the RPM. You just need
to complete the missing ones.

.. code-block::

  yum install -y "perl(Moo)"  "perl(Text::CSV_XS)" "perl(YAML::XS)" "perl(ModPerl::Util)" "perl(Mail::IMAPClient)" "perl(JSON::XS)" "perl(Encode::HanExtra)" "perl(Crypt::Eksblowfish::Bcrypt)"

  cpanm JavaScript::Minifier::XS CSS::Minifier::XS

**Ubuntu / Debian**

.. code-block::

  apt -y install libapache2-mod-perl2 libdbd-mysql-perl libtimedate-perl libnet-dns-perl libnet-ldap-perl libio-socket-ssl-perl libpdf-api2-perl libsoap-lite-perl libtext-csv-xs-perl libjson-xs-perl libapache-dbi-perl libxml-libxml-perl libxml-libxslt-perl libyaml-perl libarchive-zip-perl libcrypt-eksblowfish-perl libencode-hanextra-perl libmail-imapclient-perl libtemplate-perl libdatetime-perl libmoo-perl bash-completion libyaml-libyaml-perl libjavascript-minifier-xs-perl libcss-minifier-xs-perl libauthen-sasl-perl libauthen-ntlm-perl

Database Configuration
**********************

MySQL / Maria DB needs some config modifications. If you are using
postgresql you can skip this step:


Create a new file for the mysql config:

**CentOS / Red Hat**

.. code-block::

  /etc/my.cnf.d/znuny_config.cnf

**Ubuntu / Debian**

.. code-block::

  /etc/mysql/mariadb.conf.d/50-znuny_config.cnf

.. code-block::

  [mysql]
  max_allowed_packet=256M
  [mysqldump]
  max_allowed_packet=256M


  [mysqld]
  innodb_file_per_table
  innodb_log_file_size = 256M
  max_allowed_packet=256M

.. important::

  The web installer requires a password. The networking "bind-address" should be localhost. By default, 127.0.0.1, a synonym for skip-networking, is set. Additionally, there is no information about the requirement for utf8 whereas the default is utf8mb4

  character-set-server  = utf8
  collation-server      = utf8_general_ci

Restart the MariaDB database to apply the changes

.. code-block::

  systemctl start mariadb

Webserver Configuration
***********************

**CentOS / Red Hat**

The Apache config is already in place if you used the RPM install.

Enable MPM prefork module:

.. code-block:: bash

  sed -i '/^LoadModule mpm_event_module modules\/mod_mpm_event.so/s/^/#/' /etc/httpd/conf.modules.d/00-mpm.conf
  sed -i '/^#LoadModule mpm_prefork_module modules\/mod_mpm_prefork.so/s/^#//' /etc/httpd/conf.modules.d/00-mpm.conf


**Ubuntu / Debian**

To enable the Znuny Apache config you need to create a symlink to our sample config.

.. code-block:: bash

  ln -s /opt/znuny/scripts/apache2-httpd.include.conf /etc/apache2/conf-available/zzz_znuny.conf


Enable the needed Apache modules:

.. code-block:: bash

  a2enmod perl headers deflate filter cgi
  a2dismod mpm_event
  a2enmod mpm_prefork
  a2enconf zzz_znuny


Start / Restart the web server to apply the changes.

**CentOS / Red Hat**

.. code-block:: bash

  systemctl restart httpd

**Ubuntu / Debian**

.. code-block:: bash

  systemctl restart apache2

You should be able to access the installer script using:

``http://HOSTNAME/znuny/installer.pl``

Start-up Configuration
***********************

You should enable the web server and the database to get started on boot.

**CentOS / Red Hat**

.. code-block:: bash

  systemctl enable mariadb httpd

**Ubuntu / Debian**

.. code-block:: bash

  systemctl enable mariadb apache2

Enable Znuny Cron
*****************

Switch to the znuny user:

.. code-block:: bash

  su - <APP_USER>
  bin/Cron.sh start
