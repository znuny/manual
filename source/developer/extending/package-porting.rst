Package Porting
################

**From ((OTRS)) Community Edition 5 to Znuny LTS or the Feature Releases of Znuny 6.x:**

DateTime
********

In Znuny LTS, a new module for date and time calculation was added: ``Kernel::System::DateTime``. The module ``Kernel::System::Time`` is now deprecated and should not be used for new code anymore.

The main advantage of the new ``Kernel::System::DateTime`` module is the support for real time zones like ``Europe/Berlin`` instead of time offsets in hours like ``+2``. Note that also the old ``Kernel::System::Time`` module has been improved to support time zones. Time offsets have been completely dropped. This means that any code that uses time offsets for calculations has to be ported to use the new ``DateTime`` module instead. Code that doesn't fiddle around with time offsets itself can be left untouched in most cases. You just have to make sure that upon creation of a ``Kernel::System::Time`` object a valid time zone will be given.

Here's an example for porting time offset code to time zones:

.. code-block:: perl

   my $TimeObject     = $Kernel::OM->Get('Kernel::System::Time'); # Assume a time offset of 0 for this time object
   my $SystemTime     = $TimeObject->TimeStamp2SystemTime( String => '2004-08-14 22:45:00' );
   my $UserTimeZone   = '+2'; # normally retrieved via config or param
   my $UserSystemTime = $SystemTime + $UserTimeZone * 3600;
   my $UserTimeStamp  = $TimeObject->SystemTime2TimeStamp( SystemTime => $UserSystemTime );
                        

Code using the new ``Kernel::System::DateTime`` module:

.. code-block:: perl

   my $DateTimeObject = $Kernel::OM->Create('Kernel::System::DateTime'); # This implicitly sets the configured OTRS time zone
   my $UserTimeZone   = 'Europe/Berlin'; # normally retrieved via config or param
   $DateTimeObject->ToTimeZone( TimeZone => $UserTimeZone );
   my $SystemTime    = $DateTimeObject->ToEpoch(); # note that the epoch is independent from the time zone,
                                                   # it's always calculated for UTC
   my $UserTimeStamp = $DateTimeObject->ToString();
                        

Please note that the returned time values with the new ``Get()`` function in the ``Kernel::System::DateTime`` module are without leading zero instead of the old ``SystemTime2Date()`` function in the ``Kernel::System::Time`` module. In the new ``Kernel::System::DateTime`` module the function ``Format()`` returns the date/time as string formatted according to the given format.

Drag and Drop
*************

Starting at framework version 6, a multi attachment upload functionality was added. To implement the multi attachment upload in other extensions it is necessary to remove the attachment part from the template file, also the ``JSOnDocumentComplete`` parts (``AttachmentDelete`` and ``AttachmentUpload``). Please keep in mind, in some cases the JavaScript parts are already outsourced in ``Core.Agent.XXX`` files.

.. note::

   Please note that this is currently only applicable for places where it actually makes sense to have the possibility to upload multiple files (like ``AgentTicketPhone``, ``AgentTicketCompose``, etc.). This is not usable out of the box for admin screens.

To include the new multi attachment upload in the template, replace the existing ``input type="file"`` with the following code in your ``.tt`` template file:

.. code-block:: html

   <label>[% Translate("Attachments") | html %]:</label>
   <div class="Field">
   [% INCLUDE "FormElements/AttachmentList.tt" %]
   </div>
   <div class="Clear"></div>
               

It is also necessary to remove the ``IsUpload`` variable and all other ``IsUpload`` parts from the Perl module. Code parts like following are not needed anymore:

.. code-block:: perl

   my $IsUpload = ( $ParamObject->GetParam( Param => 'AttachmentUpload' ) ? 1 : 0 );
                        

Additional to that, the attachment layout block needs to be replaced:

.. code-block:: perl

   $LayoutObject->Block(
         Name => 'Attachment',
         Data => $Attachment,
   );
                        

Replace it with this code:

.. code-block:: programlisting

   push @{ $Param{AttachmentList} }, $Attachment;
                        

If the module where you want to integrate multi upload supports standard templates, make sure to add a section to have a human readable file size format right after the attachments of the selected template have been loaded (see e.g. ``AgentTicketPhone`` for reference):

.. code-block:: perl

   for my $Attachment (@TicketAttachments) {
         $Attachment->{Filesize} = $LayoutObject->HumanReadableDataSize(
            Size => $Attachment->{Filesize},
         );
   }
                        

When adding selenium unit tests for the modules you ported, please take a look at ``Selenium/Agent/MultiAttachmentUpload.t`` for reference.

Administration Screens Improvements
***********************************

Administration Navigation Breadcrumbs
=====================================

All admin modules should have a breadcrumb. The breadcrumb only needs to be added on the ``.tt`` template file and should be placed right after the h1 headline on top of the file. Additionally, the headline should receive the class ``InvisibleText`` to make it only *visible* for screen readers.

.. code-block:: html

   <div class="MainBox ARIARoleMain LayoutFixedSidebar SidebarFirst">
         <h1 class="InvisibleText">[% Translate("Name of your module") | html %]</h1>
   [% BreadcrumbPath = [
            {
               Name => Translate('Name of your module'),
            },
         ]
   %]
   [% INCLUDE "Breadcrumb.tt" Path = BreadcrumbPath %]
   ...
                           

Please make sure to add the correct breadcrumb for all
levels of your admin module (e.g. ``Subaction``\ s):

.. code-block:: html

   [% BreadcrumbPath = [
            {
               Name => Translate('Module Home Screen'),
               Link => Env("Action"),
            },
            {
               Name => Translate("Some Subaction"),
            },
         ]
   %]

   [% INCLUDE "Breadcrumb.tt" Path = BreadcrumbPath %]
                     
*Save* and *Save and finish*
=============================

Admin modules in OTRS 6 should not only have a *Save* button, but also a *Save and finish* button. *Save* should leave the user on the same edit page after saving, *Save and finish* should lead back to the overview of the entity the user is currently working on. Please see existing OTRS admin screens for reference.

.. code-block:: html

   <div class="Field SpacingTop SaveButtons">
         <button class="Primary CallForAction" id="SubmitAndContinue" type="submit" value="[% Translate("Save") | html %]"><span>[% Translate("Save") | html %]</span></button>
         [% Translate("or") | html %]
         <button class="Primary CallForAction" id="Submit" type="submit" value="[% Translate("Save") | html %]"><span>[% Translate("Save and finish") | html %]</span></button>
         [% Translate("or") | html %]
         <a href="[% Env("Baselink") %]Action=[% Env("Action") %]"><span>[% Translate("Cancel") | html %]</span></a>
   </div>
                               
Migrate Configuration
*********************

XML File Format
===============

Framework 6 uses a new `XML configuration file format :ref:<HowItWorks ConfigMechanism>` and the location of configuration files moved from ``Kernel/Config/Files`` to ``Kernel/Config/Files/XML``. To convert existing XML configuration files to the new format and location, you can use the following tool:

.. code-block:: screen

   bin/otrs.Console.pl Dev::Tools::Migrate::ConfigXMLStructure --source-directory Kernel/Config/Files
   Migrating configuration XML files...
   Kernel/Config/Files/Calendar.xml -> Kernel/Config/Files/XML/Calendar.xml... Done.
   Kernel/Config/Files/CloudServices.xml -> Kernel/Config/Files/XML/CloudServices.xml... Done.
   Kernel/Config/Files/Daemon.xml -> Kernel/Config/Files/XML/Daemon.xml... Done.
   Kernel/Config/Files/Framework.xml -> Kernel/Config/Files/XML/Framework.xml... Done.
   Kernel/Config/Files/GenericInterface.xml -> Kernel/Config/Files/XML/GenericInterface.xml... Done.
   Kernel/Config/Files/ProcessManagement.xml -> Kernel/Config/Files/XML/ProcessManagement.xml... Done.
   Kernel/Config/Files/Ticket.xml -> Kernel/Config/Files/XML/Ticket.xml... Done.

   Done.
                               
Perl Configuration File Format
==============================

File loading performance increased by dropping support for the old configuration format which just used sequential Perl code and had to be run by ``eval``. We instead are enforcing the new package-based format (1.1) for Perl configuration files. Znuny can only load files with this format, please make sure to convert any custom developments to it (see ``Kernel/Config/Files/ZZZ*.pm`` for examples). Every Perl configuration file needs to contain a package with a ``Load()`` method.

In the past, Perl configuration files were sometimes misused as an auto-load mechanism to override code in existing packages. This is not necessary any more. The framework features a dedicated ``Autoload`` mechanism. Please see ``Kernel/Autoload/Test.pm`` for a demonstration on how to use this mechanism to add a method in an existing file.

Perldoc Structure
=================

The structure of POD in Perl files was slightly improved and should be adapted in all files. POD is now also enforced to be syntactically correct.

What was previously called ``SYNOPSIS`` is now changed to ``DESCRIPTION``, as a synopsis typically provides a few popular code usage examples and not a description of the module itself. An additional synopsis can be provided, of course.

The second important change is that functions are now documented as ``=head2`` instead of the previously used ``=item``.

Read our :ref:`coding style guide <CodeStyleGuide UsingPerldoc>` for more information. 

.. important:: 

   In case the ``DESCRIPTION`` does not add any value to the line in the ``NAME`` section, it should be rewritten or removed altogether.

These changes lead to an improved online API documentation.

Improvements Templates and JavaScript
=======================================

**JavaScript removed from templates:**

In framework version 6 all JavaScript - especially located in ``JSOnDocumentComplete`` blocks - is removed from template files and moved to JavaScript files instead. Only in very rare conditions JavaScript needs to be placed within template files. For all other occurrences, place the JS code in module-specific JavaScript files. An ``Init()`` method within such a JavaScript file is executed automatically on file load (for the initialization of event bindings etc.) if you register the JavaScript file at the OTRS application. This is done by executing ``Core.Init.RegisterNamespace(TargetNS,                 'APP_MODULE');`` at the end of the namespace declaration within the JavaScript file.

**Template files for rich text editor:**

Along with the refactoring of the JavaScript within template files (see above), the template files for the rich text editor (``RichTextEditor.tt`` and ``CustomerRichTextEditor.tt``) were removed as they are no longer necessary.

Typically, these template files were included in the module-specific template files within a block:

.. code-block:: html

   [% RenderBlockStart("RichText") %]
   [% InsertTemplate("RichTextEditor.tt") %]
   [% RenderBlockEnd("RichText") %]
                               

This is no longer needed and can be removed. Instead of calling this block from the Perl module, it is now necessary to set the needed rich text parameters there. Instead of:

.. code-block:: perl
   
   $LayoutObject->Block(
         Name => 'RichText',
         Data => \%Param,
   );
                 
**You now have to call:**

.. code-block:: perl

   $LayoutObject->SetRichTextParameters(
         Data => \%Param,
   );
                               

Same rule applies for customer interface. Remove RichText blocks from ``CustomerRichTextEditor.tt`` and apply following code instead:

.. code-block:: perl

   $LayoutObject->CustomerSetRichTextParameters(
         Data => \%Param,
   );
                               
**Translations in JavaScript files:**

Adding translatable strings in JavaScript was quite difficult. The string had to be translated into Perl or in the template and then sent to the JavaScript function. Now translation of strings is possible directly in the JavaScript file. All other workarounds, especially blocks in the templates only for translating strings, should be removed.

Instead, the new JavaScript translation namespace ``Core.Language`` should be used to translate strings directly in the JS file:

.. code-block:: javascript

   Core.Language.Translate('The string to translate');
                               

**It is also possible to handover JS variables to be replaced in the string directly:**

.. code-block:: javascript

   Core.Language.Translate('The %s to %s', 'string', 'translate');
                               

Every ``%s`` is replaced by the variable given as extra parameter. There is no limit to the number of parameters.

**Handover data from Perl to JavaScript:**

To achieve template files without JavaScript code, some other workarounds had to be replaced with an appropriate solution. Besides translations, also the handover of data from Perl to JavaScript has been a problem in OTRS. The workaround was to add a JavaScript block in the template in which JavaScript variables were declared and filled with template tags based on data handed over from Perl to the template.

The handover process of data from Perl to JavaScript is now much easier in OTRS 6. To send specific data as variable from Perl to JavaScript, one only has to call a function on Perl-side. The data is than automatically available in JavaScript.

In Perl you only have to call:

.. code-block:: perl

   $Self->{LayoutObject}->AddJSData(
         Key   => 'KeyToBeAvailableInJS',
         Value => $YourData,
   );
                               

The ``Value`` parameter is automatically converted to a JSON object and can also contain complex data.

In JavaScript you can get the data with:

.. code-block:: javascript

   Core.Config.Get('KeyToBeAvailableInJS');
                           

JavaScript in template files is now only allowed in very rare conditions (see above). Please remove all previous workarounds.

HTML templates for JavaScript
==============================

A new JavaScript template API is available with ``Core.Template`` class. You can use it in your JavaScript code in a similar way to ``TemplateToolkit`` from Perl code.

Here's an example for porting existing ``jQuery``-based code to new template API:

.. code-block:: javascript

   var DivID = 'MyDiv',
         DivText = 'Hello, world!';

   $('<div />').addClass('CSSClass')
         .attr('id', DivID)
         .text(DivText)
         .appendTo('body');
                               

First, make sure to create a new template file under ``Kernel/Output/JavaScript/Templates/Standard`` folder. In doing this, you should keep following in mind:

* Create a subfolder with name of your ``Module``.
* You may reuse any existing subfolder structure but only if it makes sense for your component (e.g. ``Agent/MyModule/`` or ``Agent/Admin/MyModule/``).
* Use ``.html.tmpl`` as extension for template file.
* Name templates succinctly and clearly in order to avoid confusion (i.e. good: ``Agent/MyModule/SettingsDialog.html.tmpl``, bad: ``Agent/SettingsDialogTemplate.html.tmpl``).

Then, add your HTML to the template file, making sure to use placeholders for any variables you might need:

.. code-block:: javascript

   <div id="{{ DivID }}" class="CSSClass">
         {{ DivText | Translate }}
   </div>
                               

Then, just get rendered HTML by calling ``Core.Template.Render`` method with template path (without extension) and object containing variables for replacement:

.. code-block:: javascript

   var DivHTML = Core.Template.Render('Agent/MyModule/SettingsDialog', {
         DivID: 'MyDiv',
         DivText: 'Hello, world!'
   });

   $(DivHTML).appendTo('body');
                               

Internally, ``Core.Template`` uses Nunjucks engine for parsing templates. Essentially, any valid Nunjucks syntax is supported, please see `their documentation <https://mozilla.github.io/nunjucks/templating.html>`_ for more information.

Here are some tips:

* You can use ``| Translate`` filter for string translation to current language.
* All ``{{ VarName }}`` variable outputs are HTML escaped by default. If you need to output some existing HTML, please use ``| safe`` filter to bypass escaping.
* Use ``| urlencode`` for encoding URL parameters.
* Complex structures in replacement object are supported, so feel free to pass arrays or hashes and iterate over them right from template. For example, look at ``{% for %}`` syntax in `Nunjucks documentation <https://mozilla.github.io/nunjucks/templating.html#for>`__.

User Permissions
****************

User permissions were stored in the session and passed to the ``LayoutObject`` as attributes, which were then in turn accessed to determine user permissions like 

.. code-block:: screen

   ``if ($LayoutObject->{'UserIsGroup[admin]'}) { ... }``.

Permissions are no longer stored in the session and also not passed to the ``LayoutObject``. Please switch your code to the method ``PermissionCheck()`` (``Kernel::System::Group`` (for agents) or ``Kernel::System::CustomerGroup`` (for customers)). 

**Here's an example:**

.. code-block:: perl

   my $HasPermission = $Kernel::OM->Get('Kernel::System::Group')->PermissionCheck(
   UserID    => $UserID,
   GroupName => $GroupName,
   Type      => 'move_into',
   );
                        
Ticket API changes
*******************

TicketGet() Method
===================

All extensions need to be checked and ported from ``$Ticket{SolutionTime}`` to ``$Ticket{Closed}`` if ``TicketGet()`` is called with the ``Extended`` parameter.

Additionally, the database column ``ticket.create_time_unix`` was removed, and likewise the value ``CreateTimeUnix`` from the ``TicketGet()`` result data. Please use the value ``Created`` (database column ``ticket.create_time``) instead.

``LinkObject`` Events
=====================

Removed Events
~~~~~~~~~~~~~~~

Older ticket-specific ``LinkObject`` events have been dropped:

* ``TicketSlaveLinkAdd``
* ``TicketSlaveLinkDelete``
* ``TicketMasterLinkDelete``

Target Events
~~~~~~~~~~~~~

Any event handlers listening on these events should be ported to two new events instead:

* ``LinkObjectLinkAdd``
* ``LinkObjectLinkDelete``

These new events will be triggered any time a link is added or deleted by ``LinkObject``, regardless of the object type. ``Data`` parameter will contain all information your event handlers might need for further processing, e.g.:

Event Data
^^^^^^^^^^^

``SourceObject``
   Name of the link source object (e.g. ``Ticket``).

``SourceKey``
   Key of the link source object (e.g. ``TicketID``).

``TargetObject``
   Name of the link target object (e.g. ``FAQItem``).

``TargetKey``
   Key of the link target object (e.g. ``FAQItemID``).

``Type``
   Type of the link (e.g. ``ParentChild``).

``State``
   State of the link (``Valid`` or ``Temporary``).

With these new events in place, any events specific for custom ``LinkObject`` module implementations can be dropped, and all event handlers ported to use them  instead. Since source and target object names are provided in the event itself, it would be trivial to make them run only in specific situations.

Register New Event Handler
~~~~~~~~~~~~~~~~~~~~~~~~~~

To register your event handler for these new events, make sure to add a registration in the configuration, for example:

.. code-block:: xml

   <!-- OLD STYLE -->
   <ConfigItem Name="LinkObject::EventModulePost###1000-SampleModule" Required="0" Valid="1">
         <Description Translatable="1">Event handler for sample link object module.</Description>
         <Group>Framework</Group>
         <SubGroup>Core::Event::Package</SubGroup>
         <Setting>
            <Hash>
               <Item Key="Module">Kernel::System::LinkObject::Event::SampleModule</Item>
               <Item Key="Event">(LinkObjectLinkAdd|LinkObjectLinkDelete)</Item>
               <Item Key="Transaction">1</Item>
            </Hash>
         </Setting>
   </ConfigItem>

   <!-- NEW STYLE -->
   <Setting Name="LinkObject::EventModulePost###1000-SampleModule" Required="0" Valid="1">
         <Description Translatable="1">Event handler for sample link object module.</Description>
         <Navigation>Core::Event::Package</Navigation>
         <Value>
            <Hash>
               <Item Key="Module">Kernel::System::LinkObject::Event::SampleModule</Item>
               <Item Key="Event">(LinkObjectLinkAdd|LinkObjectLinkDelete)</Item>
               <Item Key="Transaction">1</Item>
            </Hash>
         </Value>
   </Setting>
                     
Article API Changes
*******************

In preparations for new *Omni Channel* infrastructure, changes have been made to the article API.

Meta Article API
=================

Article object now provides top-level article functions that do not involve back-end related data.

Following methods related to articles have been moved to ``Kernel::System::Ticket::Article`` object:

* ``ArticleFlagSet()``
* ``ArticleFlagDelete()``
* ``ArticleFlagGet()``
* ``ArticleFlagsOfTicketGet()``
* ``ArticleAccountedTimeGet()``
* ``ArticleAccountedTimeDelete()``
* ``ArticleSenderTypeList()``
* ``ArticleSenderTypeLookup()``
* ``SearchStringStopWordsFind()``
* ``SearchStringStopWordsUsageWarningActive()``

If you are referencing any of these methods with the ``Kernel::System::Ticket`` object in your code, please switch to the article object and use it instead. 

**For example:**

.. code-block:: perl

   my $ArticleObject = $Kernel::OM->Get('Kernel::System::Ticket::Article');

   my %ArticleSenderTypeList = $ArticleObject->ArticleSenderTypeList();
                               

New ``ArticleList()`` method is now provided by the article object, and can be used for article listing and locating. This method implements filters and article numbering and returns article meta data only as an ordered list. For example:

.. code-block:: perl

   my @Articles = $ArticleObject->ArticleList(
         TicketID             => 123,
         CommunicationChannel => 'Email',            # optional, to limit to a certain CommunicationChannel
         SenderType           => 'customer',         # optional, to limit to a certain article SenderType
         IsVisibleForCustomer => 1,                  # optional, to limit to a certain visibility
         OnlyFirst            => 1,                  # optional, only return first match, or
         OnlyLast             => 1,                  # optional, only return last match
   );
                     

Following methods related to articles have been dropped all-together. If you are using any of them in your code, please evaluate possibility of alternatives.

+------------------------------+-------------------------------------------------------+--------------------------------------+
| Old Method                   | Replacement                                           | Comments                             |
+==============================+=======================================================+======================================+
| ArticleFirstArticle()        | ArticleList( OnlyFirst => 1)                          |                                      |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticleLastCustomerArticle() | ArticleList( SenderType => 'customer', OnlyLast => 1) | recommendation                       |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticleCount()               | ArticleList()                                         |                                      |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticlePage()                | none                                                  | Reimplemented in ``AgentTicketZoom`` |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticleTypeList()            | none                                                  |                                      |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticleTypeLookup()          |                                                       |                                      |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticleIndex()               | ArticleList()                                         |                                      |
+------------------------------+-------------------------------------------------------+--------------------------------------+
| ArticleContentIndex()        | none                                                  |                                      |
+------------------------------+-------------------------------------------------------+--------------------------------------+


To work with article data please use new article backend API. To get correct backend object for an article, please use:

* ``BackendForArticle(%Article)``
* ``BackendForChannel( ChannelName => $ChannelName )``


**Identifying Backends:**

``BackendForArticle()``

   Returns the correct back end for a given article, or the invalid back end, so that you can always expect a back end object instance that can be used for chain-calling.

.. code-block:: perl

   my $ArticleBackendObject = $ArticleObject->BackendForArticle( TicketID => 42, ArticleID => 123 perl


``BackendForChannel()`` 
   
   Returns the correct back end for a given communication channel.

.. code-block:: perl

   my $ArticleBackendObject = $ArticleObject->BackendForChannel( ChannelName => 'Email' );
                               

Article Back-end API
====================

All other article data and related methods have been moved to separate backends. Every communication channel now has a dedicated backend API that handles article data and can be used to manipulate it.

Default Channels:

* Email (equivalent to old ``email`` article types)
* Phone (equivalent to old ``phone`` article types)
* Internal (equivalent to old ``note`` article types)
* Chat (equivalent to old ``chat`` article types)

 .. note::
   
   While chat article backend is available it is not currently utilized.

Article data manipulation can be managed via following backend methods:

* ``ArticleCreate()``
* ``ArticleUpdate()``
* ``ArticleGet()``
* ``ArticleDelete()``

All of these methods have dropped article type parameter, which must be substituted for ``SenderType`` and ``IsVisibleForCustomer`` parameter combination. In addition, all these methods now also require ``TicketID`` and ``UserID`` parameters.

.. note::
   
   Since changes in article API are system-wide, any code using the old API must be ported for framework version 6. This includes any web service definitions which leverage these methods directly via GenericInterface for example. They will need to be re-assessed and adapted to provide all required parameters to the new API during requests and manage subsequent responses in new format.

Please note that returning hash of ``ArticleGet()`` has changed, and some things (like ticket data) might be missing. Utilize parameters like ``DynamicFields => 1`` and ``RealNames => 1`` to get more information.

In addition, attachment data is not returned any more, please use combination of following methods from the article backends:

* ``ArticleAttachmentIndex()``
* ``ArticleAttachment()``
* 
.. note::
   
   ``ArticleAttachmentIndex()`` parameters and behavior has changed. Instead of old strip parameter use combination of new ``ExcludePlainText``, ``ExcludeHTMLBody`` and ``ExcludeInline``.

As an example, here is how to get all article and attachment data in the same hash:

.. code-block:: perl

   my @Articles = $ArticleObject->ArticleList(
         TicketID => $TicketID,
   );

   ARTICLE:
   for my $Article (@Articles) {

         # Make sure to retrieve backend object for this specific article.
         my $ArticleBackendObject = $ArticleObject->BackendForArticle( %{$Article} );

         my %ArticleData = $ArticleBackendObject->ArticleGet(
            %{$Article},
            DynamicFields => 1,
            UserID        => $UserID,
         );
         $Article = \%ArticleData;

         # Get attachment index (without attachments).
         my %AtmIndex = $ArticleBackendObject->ArticleAttachmentIndex(
            ArticleID => $Article->{ArticleID},
            UserID    => $UserID,
         );
         next ARTICLE if !%AtmIndex;

         my @Attachments;
         ATTACHMENT:
         for my $FileID ( sort keys %AtmIndex ) {
            my %Attachment = $ArticleBackendObject->ArticleAttachment(
               ArticleID => $Article->{ArticleID},
               FileID    => $FileID,
               UserID    => $UserID,
            );
            next ATTACHMENT if !%Attachment;

            $Attachment{FileID} = $FileID;
            $Attachment{Content} = encode_base64( $Attachment{Content} );

            push @Attachments, \%Attachment;
         }

         # Include attachment data in article hash.
         $Article->{Atms} = \@Attachments;
   }
                               

Article Search Index
======================

To make article indexing more generic, article backends now provide information necessary for properly indexing article data. Index will be created similar to old ``StaticDB`` mechanism and stored in a dedicated article search table.

Since now every article backend can provide search on arbitrary number of article fields, use ``BackendSearchableFieldsGet()`` method to get information about them. This data can also be used for forming requests to ``TicketSearch()`` method. Coincidentally, some ``TicketSearch()`` parameters have changed their name to also include article backend information, for example:



+----------------+-------------------------+
| Old parameter  | New parameter           |
+================+=========================+
| From           | MIMEBase_From           |
+----------------+-------------------------+
| To             | MIMEBase_To             |
+----------------+-------------------------+
| Cc             | MIMEBase_Cc             |
+----------------+-------------------------+
| Subject        | MIMEBase_Subject        |
+----------------+-------------------------+
| Body           | MIMEBase_Body           |
+----------------+-------------------------+
| AttachmentName | MIMEBase_AttachmentName |
+----------------+-------------------------+


Additionally, article search indexing will be done in an async call now, in order to off-load index calculation to a separate task. While this is fine for production systems, it might create new problems in certain situations, e.g. unit tests. If you are manually creating articles in your unit test, but expect it to be searchable immediately after created, make sure to manually call the new ``ArticleSearchIndexBuild()`` method on article object.

SysConfig API Changes
*********************

Note that in framework versions 6 the system configuration API was changed, so you should check if the methods are still existing. 

For example, use a combination of the following methods as a replacement for ``ConfigItemUpdate()``:

* ``SettingLock()``
* ``SettingUpdate()``
* ``ConfigurationDeploy()``

In case that you want to update a configuration setting during a ``CodeInstall`` section of a package, you could use ``SettingsSet()``. It does all previously mentioned steps and it can be used for multiple settings at once.

.. note::
   
   Do not use ``SettingSet()`` in the SysConfig GUI itself.

.. code-block:: perl

   my $Success = $SysConfigObject->SettingsSet(
         UserID   => 1,                                      # (required) UserID
         Comments => 'Deployment comment',                   # (optional) Comment
         Settings => [                                       # (required) List of settings to update.
            {
               Name                   => 'Setting::Name',  # (required)
               EffectiveValue         => 'Value',          # (optional)
               IsValid                => 1,                # (optional)
               UserModificationActive => 1,                # (optional)
            },
            ...
         ],
   );
               
``LinkObject`` API Changes
***************************

Note that ``LinkObject`` was slightly modified in the framework version 6 and methods ``LinkList()`` and ``LinkKeyList()`` might return different result if ``Direction`` parameter is used. Consider changing ``Direction``.

**Old code:**

.. code-block:: perl

   my $LinkList = $LinkObject->LinkList(
         Object    => 'Ticket',
         Key       => '321',
         Object2   => 'FAQ',
         State     => 'Valid',
         Type      => 'ParentChild',
         Direction => 'Target',
         UserID    => 1,
   );
               

**New code:**

.. code-block:: perl

   my $LinkList = $LinkObject->LinkList(
         Object    => 'Ticket',
         Key       => '321',
         Object2   => 'FAQ',
         State     => 'Valid',
         Type      => 'ParentChild',
         Direction => 'Source',
         UserID    => 1,
   );
                  

Communication Log Support for PostMaster Filters
************************************************

As part of email handling improvements for framework version 6, a new logging mechanism was added exclusively used for incoming and outgoing communications. All PostMaster filters were enriched with this new :ref:`Communication Log Mechanism <HowItWorks CommunicationLog>` API, which means any additional filters coming with packages should also leverage the new log feature.

If your package implements additional PostMaster filters, make sure to get acquainted with this new mechanism. 

Also, you can get an example of how to implement this logging mechanism by looking the code in the ``Kernel::System::PostMaster::NewTicket``  

Process Mail Queue for Unit Tests
*********************************

As part of email handling improvements for framework version 6, all emails are now sent asynchronously, that means they are saved in a queue for future processing.

To the unit tests that depend on emails continue to work properly is necessary to force the processing of the email queue.

Make sure to start with a clean queue:

.. code-block:: perl
   
   my $MailQueueObject = $Kernel::OM->Get('Kernel::System::MailQueue');
   $MailQueueObject->Delete();
               

If for some reason you can't clean completely the queue, e.g. selenium unit tests, just delete the items created during the tests:

.. code-block:: perl

   my $MailQueueObject = $Kernel::OM->Get('Kernel::System::MailQueue');
   my %MailQueueCurrentItems = map { $_->{ID} => $_ } @{ $MailQueueObject->List() || [] };

   my $Items = $MailQueueObject->List();
   MAIL_QUEUE_ITEM:
   for my $Item ( @{$Items} ) {
      next MAIL_QUEUE_ITEM if $MailQueueCurrentItems{ $Item->{ID} };
      $MailQueueObject->Delete(
         ID => $Item->{ID},
      );
   }
               

Process the queue after the code that you expect to send emails:

.. code-block:: perl

   my $MailQueueObject = $Kernel::OM->Get('Kernel::System::MailQueue');
   my $QueueItems      = $MailQueueObject->List();
   for my $Item ( @{$QueueItems} ) {
      $MailQueueObject->Send( %{$Item} );
   }
                        

Or process only the ones created during the tests:

.. code-block:: perl

   my $MailQueueObject = $Kernel::OM->Get('Kernel::System::MailQueue');
   my $QueueItems      = $MailQueueObject->List();
   MAIL_QUEUE_ITEM:
   for my $Item ( @{$QueueItems} ) {
      next MAIL_QUEUE_ITEM if $MailQueueCurrentItems{ $Item->{ID} };
      $MailQueueObject->Send( %{$Item} );
   }
                        

Depending on your case, you may need to clean the queue after or before processing it.

Widget Handling
***************

TicketZoom
===========

he widgets in the ticket zoom screen have been improved to work in a more generic way. With framework version 6, it is now possible to add new widgets for the ticket zoom screen via the system configuration. It is possible to configure the used module, the location of the widget (e.g. Sidebar) and if the content should be loaded synchronously (default) or via AJAX.

Here is an example configuration for the default widgets:

.. code-block:: xml

   <Setting Name="Ticket::Frontend::AgentTicketZoom###Widgets###0100-TicketInformation" Required="0" Valid="1">
         <Description Translatable="1">AgentTicketZoom widget that displays ticket data in the side bar.</Description>
         <Navigation>Frontend::Agent::View::TicketZoom</Navigation>
         <Value>
            <Hash>
               <Item Key="Module">Kernel::Output::HTML::TicketZoom::TicketInformation</Item>
               <Item Key="Location">Sidebar</Item>
            </Hash>
         </Value>
   </Setting>
   <Setting Name="Ticket::Frontend::AgentTicketZoom###Widgets###0200-CustomerInformation" Required="0" Valid="1">
         <Description Translatable="1">AgentTicketZoom widget that displays customer information for the ticket in the side bar.</Description>
         <Navigation>Frontend::Agent::View::TicketZoom</Navigation>
         <Value>
            <Hash>
               <Item Key="Module">Kernel::Output::HTML::TicketZoom::CustomerInformation</Item>
               <Item Key="Location">Sidebar</Item>
               <Item Key="Async">1</Item>
            </Hash>
         </Value>
   </Setting>
               

.. note::

   With this change, the template blocks in the widget code have been removed, so you should check if you use the old widget blocks in some output filters via ``Frontend::Template::GenerateBlockHooks`` functionality, and implement it in the new fashion.

Older Versions
**************

For versions older than version 5, please consult the legacy documentation on our `download server <https://download.znuny.org/releases/doc/doc-developer/>`_. 