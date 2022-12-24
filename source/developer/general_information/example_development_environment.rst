.. _PageNavigation example_development_environment:

Getting Started
################

The following page aids you in setting up one of many different development options. Of course, as with any other project, you can develop in any text editor or IDE of your choice. The following will only show you how to get the Znuny specific tools for development. This will not discuss setting up a LAMP stack, or installing all necessary requirements for running the instance.


Developer Environment
*********************
:ref:`- jump top - <PageNavigation example_development_environment>`

To facilitate contributing to the project you will need requires a development environment and a fork of the project to develop against. For package builders, you may just clone the framework from the Znuny GitHub.

Pre-requisites
==============

* A functioning Znuny installation
* A Git client
* A Git repository

If you haven't yet, you should first `set up Git <https://docs.github.com/en/articles/set-up-git>`_. Don't forget to set up `authentication to GitHub.com from Git <https://docs.github.com/en/articles/set-up-git#next-steps-authenticating-with-github-from-git>`_ as well.

Znuny `is available on GitHub <https://github.com/Znuny/>`_ along with all additional public modules. Currently we recommend Sublime for your IDE, as we use this internally and offer a package with an array of tools to make your coding experience faster and more convenient. `Znuny4OTRS-Sublime <https://github.com/znuny/Znuny4OTRS-Sublime>`_

Clone Your Repository
=====================
:ref:`- jump top - <PageNavigation example_development_environment>`

If you are not familiar with GitHub, forking is as easy as a click of your mouse. You can even use the web-based IDE for smaller changes. For larger changes, Add a source directory to your workstation or server to store the source code. Then, switch to the new directory using the command line and check them out by using the following command:

.. important:: 
   
   Please replace ``git@github.com:znuny/Znuny.git`` with your own repository. If you complete the commands as below, you will just have a copy of the source code and will not be able to push branches or make pull requests based upon this clone. For more information about forking and working with GitHub see the section `Quick Start <https://docs.github.com/en/get-started/quickstart>`_ in the GitHub documentation.


.. code-block::

   # for git dev
   shell> git clone git@github.com:znuny/Znuny.git -b dev
   # for a specific branch like Znuny 3.3
   shell> git clone git@github.com:znuny/Znuny.git -b rel-3_3


Configure Znuny
***************
:ref:`- jump top - <PageNavigation example_development_environment>`

Please configure the Znuny system according to the chapter: `Installation From Source (Linux, Unix) <https://doc.znuny.org/doc/manual/admin/6.0/en/html/manual-installation-of-otrs.html>`_ of the administrator handbook, skipping **Step 1: Install .tar.gz**

Module Tools Checkout
=====================
:ref:`- jump top - <PageNavigation example_development_environment>`

.. _DeveloperEnvironment module-tools:

Check out ``module-tools`` (from GitHub) for your development environment. It contains useful tools for developers.

.. code-block::

   shell> git clone git@github.com:Znuny/module-tools.git


Extension Development
*********************

.. _DeveolperEnvironment ModuleTools:

:ref:`- jump top - <PageNavigation example_development_environment>`

Extending Znuny with modules should be done using the :ref:`module tools <DeveloperEnvironment module-tools>`.

Separation of the Znuny framework and modules aids developers, especially when working on a cloned repository, by clearly separating module development from framework development. Linking a module facilitates module access to the framework without dirtying the framework tree. A ``module-tools`` script takes care of the heavy lifting here, lets look at an example.

Link the FAQ
============
:ref:`- jump top - <PageNavigation example_development_environment>`

Link the modules source to the framework.

.. code-block::

   shell> ~/src/module-tools/link.pl ~/src/FAQ/ ~/src/otrs/

.. important:: Adding New Package Files

   Run ``link.pl`` each time you add a new file.

Rebuild the configuration files to complete integration in Znuny.

.. code-block::

   shell> ~/src/otrs/bin/otrs.Console.pl Maint::Config::Rebuild

.. note:: Database or Migration Tasks

   Additional changes via SQL or Perl code must be performed manually.

   **Example:**

   .. code-block::

      shell> ~/src/module-tools/DatabaseInstall.pl -m FAQ.sopm -a install
      shell> ~/src/module-tools/CodeInstall.pl -m FAQ.sopm -a install


To remove links from Znuny enter the following command:

.. code-block::

   shell> ~/src/module-tools/remove_links.pl ~/src/otrs/

Additional Tools Set
********************
:ref:`- jump top - <PageNavigation example_development_environment>`

We highly recommend using the following tools to Znuny developers.

`ZnunyCodePolicy <https://github.com/znuny/ZnunyCodePolicy>`_
`Fred <https://github.com/Znuny/Fred>`_.

Code Policy (ZnunyCodePolicy)
=============================
:ref:`- jump top - <PageNavigation example_development_environment>`

ZnunyCodePolicy is a code quality checker. It enforces good coding practices. These practices are required by our code and merge and pull requests which fail will be rejected. Therefore, to make a contribution, this tool is required and not an optional part of any development environment.

You can use it as a standalone test script or even register it as a git commit hook. Please see `the module documentation <https://github.com/znuny/ZnunyCodePolicy/blob/master/doc/en/feature.md>`_ for details.

Fred
====

:ref:`- jump top - <PageNavigation example_development_environment>`

Fred, be it installed or linked (as described below) into your development system, features several helpful optional modules.

Two Examlpe Features:

SQL Logger
   Displays all SQL statements in the front-end.
STDERR console
   Displays all STDERR messages in the front-end.

More details are documented in the `module documentation <https://github.com/znuny/Fred/blob/master/doc/en/Fred.xml>`_.

.. note:: Call to Action

   We make all of our tools open source; feel free to improve, fix, and expand theese tools as well.
   