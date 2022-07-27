Contribute to Znuny
####################

The best way to contribute to the project is by adding functionality in package form. When your package is ready, you can promote it on `OPAR <https://opar.perl-services.de/>`_

Creating an Add-on (Hello World)
*********************************
.. _ContributeZnuny HelloWorld:

To get started let's program a module, as an add-on, that displays a text: "Hello World". 

Firstly create a directory structure for your ``Hello World`` package.

.. code-block::

    mkdir -p ~/src/HelloWorld
    cd ~/src/HelloWorld

In this directory, create all needed framework directories. Each module should at least contain the following directories:                        

.. code-block::

    mkdir -p Kernel/System
    mkdir -p Kernel/Modules
    mkdir -p Kernel/Output/HTML/Templates/Standard
    mkdir -p Kernel/Config/Files/XML/
    mkdir -p Kernel/Language

Default Configuration File
==========================

The creation of a module registration facilitates the display of the new module in the software. Therefore we create a file ``Kernel/Config/Files/XML/HelloWorld.xml``. In this file, we create a new config element. The impact of the various settings is described in the chapter :ref:`Config Mechanism <HowItWorks ConfigMechanism>`.

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" ?>
    <otrs_config version="2.0" init="Application">
        <Setting Name="Frontend::Module###AgentHelloWorld" Required="1" Valid="1">
            <Description Translatable="1">FrontendModuleRegistration for HelloWorld module.</Description>
            <Navigation>Frontend::Agent::ModuleRegistration</Navigation>
            <Value>
                <Item ValueType="FrontendRegistration">
                    <Hash>
                        <Item Key="Group">
                            <Array>
                                <Item>users</Item>
                            </Array>
                        </Item>
                        <Item Key="GroupRo">
                            <Array>
                            </Array>
                        </Item>
                        <Item Key="Description" Translatable="1">HelloWorld.</Item>
                        <Item Key="Title" Translatable="1">HelloWorld</Item>
                        <Item Key="NavBarName">HelloWorld</Item>
                    </Hash>
                </Item>
            </Value>
        </Setting>
        <Setting Name="Loader::Module::AgentHelloWorld###002-Filename" Required="0" Valid="1">
            <Description Translatable="1">Loader module registration for the agent interface.</Description>
            <Navigation>Frontend::Agent::ModuleRegistration::Loader</Navigation>
            <Value>
                <Hash>
                    <Item Key="CSS">
                        <Array>
                        </Array>
                    </Item>
                    <Item Key="JavaScript">
                        <Array>
                        </Array>
                    </Item>
                </Hash>
            </Value>
        </Setting>
        <Setting Name="Frontend::Navigation###AgentHelloWorld###002-Filename" Required="0" Valid="1">
            <Description Translatable="1">Main menu item registration.</Description>
            <Navigation>Frontend::Agent::ModuleRegistration::MainMenu</Navigation>
            <Value>
                <Array>
                    <DefaultItem ValueType="FrontendNavigation">
                        <Hash>
                        </Hash>
                    </DefaultItem>
                    <Item>
                        <Hash>
                            <Item Key="Group">
                                <Array>
                                    <Item>users</Item>
                                </Array>
                            </Item>
                            <Item Key="GroupRo">
                                <Array>
                                </Array>
                            </Item>
                            <Item Key="Description" Translatable="1">HelloWorld.</Item>
                            <Item Key="Name" Translatable="1">HelloWorld</Item>
                            <Item Key="Link">Action=AgentHelloWorld</Item>
                            <Item Key="LinkOption"></Item>
                            <Item Key="NavBar">HelloWorld</Item>
                            <Item Key="Type">Menu</Item>
                            <Item Key="Block"></Item>
                            <Item Key="AccessKey"></Item>
                            <Item Key="Prio">8400</Item>
                        </Hash>
                    </Item>
                </Array>
            </Value>
        </Setting>
    </otrs_config>
                        
Frontend Module
===============

After creating the links and executing the Sysconfig, a new module with the name 'HelloWorld' is displayed. When calling it up, an error message is displayed as the matching frontend module is not yet found. This is the next thing to be created. To do so, we create the following file:

.. code-block:: perl

    # --
    # Kernel/Modules/AgentHelloWorld.pm - frontend module
    # Copyright (C) (year) (name of author) (email of author)
    # --
    # This software comes with ABSOLUTELY NO WARRANTY. For details, see
    # the enclosed file COPYING for license information (GPL). If you
    # did not receive this file, see https://www.gnu.org/licenses/gpl-3.0.txt.
    # --

    package Kernel::Modules::AgentHelloWorld;

    use strict;
    use warnings;

    # Frontend modules are not handled by the ObjectManager.
    our $ObjectManagerDisabled = 1;

    sub new {
        my ( $Type, %Param ) = @_;

        # allocate new hash for object
        my $Self = {%Param};
        bless ($Self, $Type);

        return $Self;
    }

    sub Run {
        my ( $Self, %Param ) = @_;
        my %Data = ();

        my $HelloWorldObject = $Kernel::OM->Get('Kernel::System::HelloWorld');
        my $LayoutObject     = $Kernel::OM->Get('Kernel::Output::HTML::Layout');

        $Data{HelloWorldText} = $HelloWorldObject->GetHelloWorldText();

        # build output
        my $Output = $LayoutObject->Header(Title => "HelloWorld");
        $Output   .= $LayoutObject->NavigationBar();
        $Output   .= $LayoutObject->Output(
            Data         => \%Data,
            TemplateFile => 'AgentHelloWorld',
        );
        $Output   .= $LayoutObject->Footer();

        return $Output;
    }

    1;

Core Module
============

Next, we create the file for the core module ``/HelloWorld/Kernel/System/HelloWorld.pm`` with the following content:

.. code-block:: perl

    # --
    # Kernel/System/HelloWorld.pm - core module
    # Copyright (C) (year) (name of author) (email of author)
    # --
    # This software comes with ABSOLUTELY NO WARRANTY. For details, see
    # the enclosed file COPYING for license information (GPL). If you
    # did not receive this file, see https://www.gnu.org/licenses/gpl-3.0.txt.
    # --

    package Kernel::System::HelloWorld;

    use strict;
    use warnings;

    # list your object dependencies (e.g. Kernel::System::DB) here
    our @ObjectDependencies = (
        # 'Kernel::System::DB',
    );

    =head1 NAME

    HelloWorld - Little "Hello World" module

    =head1 DESCRIPTION

    A simple module to display the text 'Hello World'.

    =head2 new()

    Create an object. Do not use it directly, instead use:

        my $HelloWorldObject = $Kernel::OM->Get('Kernel::System::HelloWorld');

    =cut

    sub new {
        my ( $Type, %Param ) = @_;

        # allocate new hash for object
        my $Self = {};
        bless ($Self, $Type);

        return $Self;
    }

    =head2 GetHelloWorldText()

    Return the "Hello World" text.

        my $HelloWorldText = $HelloWorldObject->GetHelloWorldText();

    =cut

    sub GetHelloWorldText {
        my ( $Self, %Param ) = @_;

        # Get the DBObject from the central object manager
        # my $DBObject = $Kernel::OM->Get('Kernel::System::DB');

        my $HelloWorld = $Self->_FormatHelloWorldText(
            String => 'Hello World',
        );

        return $HelloWorld;
    }

    =begin Internal:

    =head2 _FormatHelloWorldText()

    Format "Hello World" text to uppercase

        my $HelloWorld = $Self->_FormatHelloWorldText(
            String => 'Hello World',
        );

    =cut

    sub _FormatHelloWorldText{
        my ( $Self, %Param ) = @_;

        my $HelloWorld = uc $Param{String};

        return $HelloWorld;

    }

    =end Internal:

    1;
                        

Template File
==============

The last thing missing before the new module can run is the relevant HTML template. Thus, we create the following file:

.. code-block:: shell

    # --
    # Kernel/Output/HTML/Templates/Standard/AgentHelloWorld.tt - overview
    # Copyright (C) (year) (name of author) (email of author)
    # --
    # This software comes with ABSOLUTELY NO WARRANTY. For details, see
    # the enclosed file COPYING for license information (GPL). If you
    # did not receive this file, see https://www.gnu.org/licenses/gpl-3.0.txt.
    # --
    <h1>[% Translate("Overview") | html %]: [% Translate("HelloWorld") %]</h1>
    <p>
        [% Data.HelloWorldText | Translate() | html %]
    </p>
                        

         The module is working now and displays the text 'Hello World'
         when called.

 Language File
 =============

If the text 'Hello World!' is to be translated into for instance German, you can create a translation file for this language in ``HelloWorld/Kernel/Language/de_AgentHelloWorld.pm``. Example:

.. code-block:: perl

    package Kernel::Language::de_AgentHelloWorld;

    use strict;
    use warnings;

    sub Data {
        my $Self = shift;

        $Self->{Translation}->{'Hello World!'} = 'Hallo Welt!';

        return 1;
    }
    1;
            
Summary
********

The above example proves that it is not too difficult to write a new module for Znuny. It is important though to make sure that the module and file names are unique and thus do not interfere with the framework or other expansion modules. 

After module development, OPM package building (see chapter :ref:`Package Building <PackageBuilding PageNavigation>`) is the next step.

