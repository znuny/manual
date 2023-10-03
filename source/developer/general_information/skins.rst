Skins
######

Skinning allows the administrator to control the look and feel of the application. Whereas :ref:`themes <Theming PageNavigation>` control the layout, skins control things like: colors, padding, and spacing.

With the help of modern CSS standards, it is possible to change the display thoroughly (repositioning dialog parts, hiding elements, etc.).

Skin Basics
***********

All skins are in ``var/httpd/htdocs/skins/$SKIN_TYPE/$SKIN_NAME``. There are two types of skins: agent and customer skins.

Each of the agents can select individually which of the installed agent skins they want to "wear".

For the customer interface, a skin has to be selected globally with the config setting ``Loader::Customer::SelectedSkin``. All customers will see this skin.

Skin loading
************

It is important to note that the "default" skin will *always* be loaded *first*. If the agent selected another skin than the "default" one, then the other one will be loaded only *after* the default skin. By "loading" here we mean that OTRS will put tags into the HTML content which cause the CSS files to be loaded by the browser. Let's see an example of this:

.. code:: html

   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css-cache/CommonCSS_179376764084443c181048401ae0e2ad.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/ivory/css-cache/CommonCSS_e0783e0c2445ad9cc59c35d6e4629684.css" />
                     

Here it can clearly be seen that the default skin is loaded first, and then the custom skin specified by the agent. In this example, we see the result of the activated loader (``Loader::Enabled`` set to 1), which gathers all CSS files, concatenates and minifies them and serves them as one chunk to the browser. This saves bandwidth and also reduces the number of HTTP requests. Let's see the same example with the Loader turned off:

.. code:: html

   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Reset.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Default.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Header.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.OverviewControl.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.OverviewSmall.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.OverviewMedium.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.OverviewLarge.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Footer.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Grid.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Form.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Table.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Widget.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.WidgetMenu.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.TicketDetail.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Tooltip.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Dialog.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Print.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Agent.CustomerUser.GoogleMaps.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/default/css/Core.Agent.CustomerUser.OpenTicket.css" />
   <link rel="stylesheet" href="/otrs-web/skins/Agent/ivory/css/Core.Dialog.css" />
                     

Here we can better see the individual files that come from the skins.

There are different types of CSS files: common files which must always be loaded, and "module-specific" files which are only loaded for special modules within the OTRS framework.

In addition, it is possible to specify CSS files which only must be loaded on IE7 or IE8 (in the case of the customer interface, also IE6). This is unfortunate, but it was not possible to develop a modern GUI on these browsers without having special CSS for them.

For details regarding the CSS file types, please see the :ref:`section on the "Loader" <HowItWorks LoaderMechanism>`.

For each HTML page generation, the loader will first take all configured CSS files from the default skin, and then for each file look if it is also available in a custom skin (if a custom skin is selected) and load them after the default files.

That means that:

A. CSS files in custom skins need to have the same names as in the default skins, and
#. custom skins need not contain all default skin files

That is the big advantage of loading the default skin first: a custom skin has all default CSS rules present and only needs to change those which should result in a different display. That can often be done in a single file, like in the example above.

Another effect is, you need to be careful to overwrite all default CSS rules in your custom skins that you want to change. Let's see an example:

.. code:: css

   .Header h1 {
         font-weight: bold;
         color: #000;
   }
                     
The code above defines special headings inside of the ``.Header`` element as bold, black text. Now if you want to change that in your skin to another color and normal text, it is not enough to write this:

.. code:: css

   .Header h1 {
         color: #F00;
   }
                     

Because the original rule for ``font-weight`` still applies. You need to override it explicitly:

.. code:: css

   .Header h1 {
         font-weight: normal;
         color: #F00;
   }
                     

Create a Skin
*************

In this section, we will be creating a new agent skin which replaces the default OTRS background color (white) with a custom company color (light grey) and the default logo by a custome one. Also we will configure that skin to be the one which all agents will see by default.

There are only three simple steps we need to take to achieve this goal:

1. Create or copy skin files.
#. Configure the new logo and (optional).
#. Configure the skin for use.

Let's start by creating the files needed for our new skin. First of all, we need to create a new folder for this skin (we'll call it ``custom``). This folder will be ``var/httpd/htdocs/skins/Agent/custom``.

In there, we need to place the new CSS file in a new directory ``css`` which defines the new skin's appearance. We'll call it ``Core.Default.css`` (remember that it must have the same name as one of the files in the "default" skin). This is the code needed for the CSS file:

.. code:: css

   body {
         background-color: #c0c0c0; /* not very beautiful but it meets our purpose */
   }
                     

Now follows the second step, adding a new logo and making the new skin known to the OTRS system. For this, we first need to place our custom logo (e.g. ``logo.png``) in a new directory (e.g. ``img``) in our skin directory. Then we need to create a new config file ``Kernel/Config/Files/CustomSkin.xml``, which will contain the needed settings as follows:

.. code:: xml

   <?xml version="1.0" encoding="utf-8" ?>
   <otrs_config version="1.0" init="Changes">
         <ConfigItem Name="AgentLogo" Required="0" Valid="1">
            <Description Translatable="1">The logo shown in the header of the agent interface. The URL to the image must be a relative URL to the skin image directory.</Description>
            <Group>Framework</Group>
            <SubGroup>Frontend::Agent</SubGroup>
            <Setting>
               <Hash>
                     <Item Key="URL">skins/Agent/custom/img/logo.png</Item>
                     <Item Key="StyleTop">13px</Item>
                     <Item Key="StyleRight">75px</Item>
                     <Item Key="StyleHeight">67px</Item>
                     <Item Key="StyleWidth">244px</Item>
               </Hash>
            </Setting>
         </ConfigItem>
         <ConfigItem Name="Loader::Agent::Skin###100-custom" Required="0" Valid="1">
            <Description Translatable="1">Custom skin for the development manual.</Description>
            <Group>Framework</Group>
            <SubGroup>Frontend::Agent</SubGroup>
            <Setting>
               <Hash>
                     <Item Key="InternalName">custom</Item>
                     <Item Key="VisibleName">Custom</Item>
                     <Item Key="Description">Custom skin for the development manual.</Item>
                     <Item Key="HomePage">www.yourcompany.com</Item>
               </Hash>
            </Setting>
         </ConfigItem>
   </otrs_config>
               

To make this configuration active, we need to navigate to the SysConfig module in the admin area of OTRS (alternatively, you can run the script ``bin/otrs.Console.pl Maint::Config::Rebuild``). This will regenerate the Perl cache of the XML configuration files, so that our new skin is now known and can be selected in the system. To make it the default skin that new agents see before they made their own skin selection, edit the SysConfig setting ``Loader::Agent::DefaultSelectedSkin`` and set it to "custom".

In conclusion: to create a new skin in OTRS, we had to place the new logo file, and create one CSS and one XML file, resulting in three new files:

.. code:: 

   Kernel/Config/Files/CustomSkin.xml
   var/httpd/htdocs/skins/Agent/custom/img/custom-logo.png
   var/httpd/htdocs/skins/Agent/custom/css/Core.Header.css
