Installation
############
.. PageNavigation installupdate_install:

To install Znuny or Znuny LTS you need:

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
This includes the web server, database (MariaDB in this case), cpanminus to install additional.
Perl modules and tar to extract the source.

**CentOS / Red Hat / Rocky Linux**

.. code-block::

  dnf update -y
  # Enable Powertools
  dnf config-manager --set-enabled powertools
  ## CentOS / RHEL / Rocky Linux 9
  dnf config-manager --enable crb
  dnf install -y epel-release httpd cpanminus gcc dnf-plugins-core
  # If you will use mariadb
  dnf install -y mariadb mariadb-server
  
  ## Set selinux to Permissive
  vi /etc/selinux/config

  # This file controls the state of SELinux on the system.
  # SELINUX= can take one of these three values:
  #     enforcing - SELinux security policy is enforced.
  #     permissive - SELinux prints warnings instead of enforcing.
  #     disabled - No SELinux policy is loaded.
  # See also:
  # https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-selinux/#getting-started-with-selinux-selinux-states-and-modes
  #
  # NOTE: In earlier Fedora kernel builds, SELINUX=disabled would also
  # fully disable SELinux during boot. If you need a system with SELinux
  # fully disabled instead of SELinux running with no policy loaded, you
  # need to pass selinux=0 to the kernel command line. You can use grubby
  # to persistently set the bootloader to boot with selinux=0:
  #
  #    grubby --update-kernel ALL --args selinux=0
  #
  # To revert back to SELinux enabled:
  #
  #    grubby --update-kernel ALL --remove-args selinux
  #
  SELINUX=permissive
  # SELINUXTYPE= can take one of these three values:
  #     targeted - Targeted processes are protected,
  #     minimum - Modification of targeted policy. Only selected processes are protected.
  #     mls - Multi Level Security protection.
  SELINUXTYPE=targeted

  reboot

**Ubuntu / Debian**

.. code-block::

  apt update
  apt install -y apache2 mariadb-client mariadb-server cpanminus

RPM Install
***********

Install the RPM via `YUM <https://en.wikipedia.org/wiki/Yum_(software)>`_

.. code-block::

  # Znuny LTS (modify version to latest see: https://download.znuny.org/releases/RPMS/rhel/7/)
  yum install -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-6.5.7-01.noarch.rpm

  # Znuny 6.5
  yum install -y https://download.znuny.org/releases/RPMS/rhel/7/znuny-6.5.7-01.noarch.rpm


Install From Source
*******************

The installation from the source takes some more steps:

.. code-block::

  # Download Znuny
  cd /opt
  wget https://download.znuny.org/releases/znuny-latest-6.5.tar.gz  

  # Extract
  tar xfz znuny-latest-6.5.tar.gz

  # Create a symlink 
  sudo ln -s /opt/znuny-6.5.7 /opt/otrs

  # Add user for RHEL/CentOS
  useradd -d /opt/otrs -c 'Znuny user' -g apache -s /bin/bash -M -N otrs

  # Add user for Debian/Ubuntu
  useradd -d /opt/otrs -c 'Znuny user' -g www-data -s /bin/bash -M -N otrs

  # Copy Default Config
  cp /opt/otrs/Kernel/Config.pm.dist /opt/otrs/Kernel/Config.pm

  # Set permissions
  /opt/otrs/bin/otrs.SetPermissions.pl

  # As otrs User - Rename default cronjobs
  su - otrs
  cd /opt/otrs/var/cron
  for foo in *.dist; do cp $foo `basename $foo .dist`; done

Install Required Perl Modules
*****************************

Based on your distribution, there are several different was to install the needed modules.

To see which modules are missing but required, verify these with the following command.

.. code-block::

  ~otrs/bin/otrs.CheckModules.pl --all

**CentOS / Red Hat / Rocky Linux**

Some of the needed Perl Modules are installed, when installing the RPM. You just need
to complete the missing ones.

.. code-block::

  yum install -y jq

  yum install -y "perl(Moo)"  "perl(Text::CSV_XS)" "perl(YAML::XS)" "perl(ModPerl::Util)" "perl(Mail::IMAPClient)" "perl(JSON::XS)" "perl(Encode::HanExtra)" "perl(Crypt::Eksblowfish::Bcrypt)" "perl(Data::UUID)"

  cpanm Jq JavaScript::Minifier::XS iCal::Parser Hash::Merge Crypt::JWT CSS::Minifier::XS Data::UUID Spreadsheet::XLSX Crypt::OpenSSL::X509

  # Note to install the Crypt::OpenSSL::X509, you will need to install openssl-devel

  # If you will use MySQL or MariaDB


**Ubuntu / Debian**

.. code-block::

  apt -y install apache2 mariadb-client mariadb-server cpanminus libapache2-mod-perl2 libdbd-mysql-perl libtimedate-perl libnet-dns-perl libnet-ldap-perl libio-socket-ssl-perl libpdf-api2-perl libsoap-lite-perl libtext-csv-xs-perl libjson-xs-perl libapache-dbi-perl libxml-libxml-perl libxml-libxslt-perl libyaml-perl libarchive-zip-perl libcrypt-eksblowfish-perl libencode-hanextra-perl libmail-imapclient-perl libtemplate-perl libdatetime-perl libmoo-perl bash-completion libyaml-libyaml-perl libjavascript-minifier-xs-perl libcss-minifier-xs-perl libauthen-sasl-perl libauthen-ntlm-perl libhash-merge-perl libical-parser-perl libspreadsheet-xlsx-perl libcrypt-jwt-perl libcrypt-openssl-x509-perl jq

  cpanm install Jq

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
  character-set-server  = utf8
  collation-server      = utf8_general_ci

.. important::

  The web installer requires a password. The networking "bind-address" should be localhost. By default, 127.0.0.1, a synonym for skip-networking, is set. Additionally, there is no information about the requirement for utf8 whereas the default is utf8mb4

If started, restart the MariaDB database to apply the changes otherwise enable and start the MariaDB.

.. code-block::

  systemctl restart mariadb
  # or
  systemctl enable --now mariadb 

Run mysql_secure_installation

Webserver Configuration
***********************

**CentOS / Red Hat**

The Apache config is already in place if you used the RPM install.

Enable MPM prefork module:

.. code-block:: bash

  sed -i '/^LoadModule mpm_event_module modules\/mod_mpm_event.so/s/^/#/' /etc/httpd/conf.modules.d/00-mpm.conf
  sed -i '/^#LoadModule mpm_prefork_module modules\/mod_mpm_prefork.so/s/^#//' /etc/httpd/conf.modules.d/00-mpm.conf

.. note:: In case you did a source install on an RPM based system

  To enable the Znuny Apache config you need to create a symlink to our sample config.

  .. code-block::

    ln -s /opt/otrs/scripts/apache2-httpd.include.conf /etc/httpd/conf.d/zzz_znuny.conf


**Ubuntu / Debian**

To enable the Znuny Apache config you need to create a symlink to our sample config.

.. code-block:: bash

  ln -s /opt/otrs/scripts/apache2-httpd.include.conf /etc/apache2/conf-available/zzz_znuny.conf


Enable the needed Apache modules:

.. code-block:: bash

  a2enmod perl headers deflate filter cgi
  a2dismod mpm_event
  a2enmod mpm_prefork
  a2enconf zzz_znuny

.. code-block::

  ## RHEL / CentOS / Rocky Linux
  systemctl restart httpd
  # or
  systemctl enable --now httpd
  ## Ubuntu / Debian
  systemctl restart apache2
  # or
  systemctl enable --now apache2

**CentOS / Red Hat**

.. code-block:: bash

  systemctl restart httpd

**Ubuntu / Debian**

.. code-block:: bash

  systemctl restart apache2

You should be able to access the installer script using:

``http://HOSTNAME/otrs/installer.pl``

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

Switch to the otrs user:

.. code-block:: bash

  su - otrs
  bin/Cron.sh start
