Theming
#######
.. _Theming PageNavigation:

Own Themes
===========

You can create your own themes so as to use the layout you like in the OTRS web frontend. To create custom themes, you should customize the output templates to your needs. More information on the syntax and structure of output templates can be found in the :ref:`templating section <HowItWorks Templating>`.

As an example, perform the following steps to create a new theme called "Company":

* Create a directory called ``Kernel/Output/HTML/Templates/Company`` and copy all files that you like to change from ``Kernel/Output/HTML/Templates/Standard`` into the new folder.

.. important::
   
   Only copy over the files you're planning to change. The framework will automatically load missing files from the Standard theme. This will make upgrading at a later stage much easier.

* Customize the files in the directory ``Kernel/Output/HTML/Templates/Company`` and change the layout to your needs.
* Activate the new theme by add them in system configuration under ``Frontend::Themes``.

Now the new theme should be usable. You can select it via your personal preferences.

.. warning::
   
   Do not change the theme files in-place since these changes will be lost after an update. Create new themes as described above.

.. note::

   You should package your themes. See ::ref:`Packaging Code <PackageBuilding PackagingCode>`
