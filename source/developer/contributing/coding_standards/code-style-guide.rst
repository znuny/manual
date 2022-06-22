.. _PageNavigation code-style-guide:

Code Style Guide
#################

Use the following guidelines to tidy or write your code to conform to the official coding style, as recommended and used by the framework development team. Code checking with the code policy tool (ZnunyCodePolicy) can catch and clean up where possible or inform where necessary, but here are the standards as a primer for good coding.

General Formatting
******************

**Line Length**

Lines should generally not be longer than 120 characters.

**Indentation**

We use 4 spaces instead of a tab for the reason that this is way its always been done :)

Why “Spaces and not tabs?”
   A tab could be a different number of columns depending on your environment, but a space is always one column.

Perl Guide
**********
:ref:`- jump top - <PageNavigation code-style-guide>`

This section addresses the desired coding style used in the Perl code for the software.

Formatting
==========
:ref:`- jump top - <PageNavigation code-style-guide>`

**Whitespace and Braces**

Here is a code example for using whitespace with braces to increase readability.

.. code-block:: perl

   if ($Condition) {
       Foo();
   }
   else {
       Bar();

   while ($Condition == 1) {
       Foo();
   }

**Whitespace and Parentheses**

Here is a code example for using whitespace between keywords and opening parenthesis to increase readability.

.. code-block:: perl

   if ()...
   for ()...


.. note:: Exception

   Conditions containing one variable contain no space.

   .. code-block:: perl

      # Single Condition

      if ($Condition) { ... }

      # Multiple Condition

      if ( $Condition && $ABC ) { ... }

   .. warning:: Built-in Variables

      For Perl built-in-, no parenthesis are used.

      .. code-block:: perl

         chomp $Variable;

**Header Information**

Attach the following header to every source file. Source files are UTF-8.

.. code-block:: bash

   # --
   # Copyright (C) 2012-2021 Znuny GmbH, http://znuny.org/
   # --
   # This software comes with ABSOLUTELY NO WARRANTY. For details, see
   # the enclosed file COPYING for license information (AGPL). If you
   # did not receive this file, see http://www.gnu.org/licenses/agpl.txt.
   # --


**Header for Executable**

Executable files (``*.pl``) have a special header.

.. code-block:: perl

   #!/usr/bin/env perl
   # --
   # Copyright (C) 2021 Znuny GmbH, https://znuny.org/
   # --
   # This program is free software: you can redistribute it and/or modify
   # it under the terms of the GNU General Public License as published by
   # the Free Software Foundation, either version 3 of the License, or
   # (at your option) any later version.
   #
   # This program is distributed in the hope that it will be useful,
   # but WITHOUT ANY WARRANTY; without even the implied warranty of
   # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   # GNU General Public License for more details.
   #
   # You should have received a copy of the GNU General Public License
   # along with this program. If not, see https://www.gnu.org/licenses/gpl-3.0.txt.
   # --

Control flow
=============
:ref:`- jump top - <PageNavigation code-style-guide>`

**Conditions**

Because of the complexity of conditions, when chaining them (linked with logical 'or' or 'and'  operations), you have to be aware of several situations within the software.

Perl Best Practices says: High precedence operators (``&&`` and ``||``) shouldn't be confused with low precedence operators (``and`` and ``or``). To avoid confusion, we always use the high precedence operators.

`(read more in the perldoc for perlop) <https://perldoc.perl.org/perlop>`_

Correct:

.. code-block:: perl

   if ( $Condition1 && $Condition2 ) { ... }

Incorrect:

.. code-block:: perl

   if ( $Condition and $Condition2 ) { ... }

.. important::

   Parenthesis may still be necessary to order precedence.

**Long Conditions**

For conditions longer that 120 characters.

Correct:

.. code-block:: perl

   if (
       $Condition1
       && $Condition2
       )
   { ... }

Incorrect:

.. code-block:: perl

   if ( $Condition1
       && $Condition2
       )
   { ... }

.. note:: Multi-line Conditions and Ending Parenthesis

   The right parenthesis of the ``if`` condition is placed on a line on its own.

More examples:

.. code-block:: perl

   if (
       $XMLHash[0]->{otrs_stats}[1]{StatType}[1]{Content}
       && $XMLHash[0]->{otrs_stats}[1]{StatType}[1]{Content} eq 'static'
       )
   { ... }

   if ( $TemplateName eq 'AgentTicketCustomer' ) {
       ...
   }

   if (
       ( $Param{Section} eq 'Xaxis' || $Param{Section} eq 'All' )
       && $StatData{StatType} eq 'dynamic'
       )
   { ... }

   if (
       $Self->{TimeObject}->TimeStamp2SystemTime( String => $Cell->{TimeStop} )
       > $Self->{TimeObject}->TimeStamp2SystemTime(
           String => $ValueSeries{$Row}{$TimeStop}
       )
       || $Self->{TimeObject}->TimeStamp2SystemTime( String => $Cell->{TimeStart} )
       < $Self->{TimeObject}->TimeStamp2SystemTime(
           String => $ValueSeries{$Row}{$TimeStart}
       )
       )
   { ... }

**Postfix ``if``**

Generally, we use postfix ``if`` statements to reduce the amount of levels.

For multi-line statements, don't use a postfix ``if`` unless the statement involves a return statement in a functons, or to end a loop, or to go the next iteration.

Correct:

.. code-block:: perl

   next ITEM if !$ItemId;

Incorrect:

.. code-block:: perl

   return $Self->{LogObject}->Log(
       Priority => 'error',
       Message  => 'ItemID needed!',
   ) if !$ItemId;

Here's the corrected code:

.. code-block:: perl

  if( !$ItemId ) {
       $Self->{LogObject}->Log( ... );
       return;
   }

Correct:

.. code-block:: perl

   for my $Needed ( 1 .. 10 ) {
       next if $Needed == 5;
       last  if $Needed == 9;
   }

Incorrect:

.. code-block:: perl

    my $Var = 1 if $Something == 'Yes';

Subroutine Restrictions
========================
:ref:`- jump top - <PageNavigation code-style-guide>`

Adhere to the following standards of subroutine usage.

Forbidden for use in ``.pm`` files are:

* ``die``
* ``exit``
* ``print``

Forbidden for use in Released Files is:

* ``Dumper``

Replaced built-in functions are:

* Use ``Main::Require()`` instead of ``required``

.. important:: General Information

   Use the framework functions before built-in. An great example is the framework's ``DateTimeObject``. This objects functions replace those of the built-in functions like ``time()``, ``localtime()``.

Regular Expressions
===================
:ref:`- jump top - <PageNavigation code-style-guide>`

This section covers how the software uses regular expressions and how you should use them.

* Always use the ``m//`` operator with curly braces as delimiters.
* Default modifiers used are:
    * ``x`` allows you to comment your regex and use spaces to visually separate logical groups.
    * ``m``
    * ``s``

.. code-block:: perl

    $Date =~ m{ \A \d{4} - \d{2} - \d{2} \z }xms
    $Date =~ m{
        \A      # beginning of the string
        \d{4} - # year
        \d{2} - # month
        [^\n]   # everything but newline
        #..
    }xms;


.. important:: Spaces and Meaning

   As the space no longer has a special meaning, you have to use a character class to match a single space (``[ ]``). If you want to match any whitespace character you can use ``\s``.

   .. code-block:: perl

      $Text =~ m{
          Test
          [ ]    # there must be a space between 'Test' and 'Regex'
          Regex
      }xms;

**Dot and Newline**

In a regular expression, the dot ``.`` includes the newline. Whereas in a regular expression without the ``s`` modifier, the dot means "everything but newline". If you want to match anything but newline, you have to use the negated single character class (``[^\n]``).

**User Supplied Regular Expressions**

An exception to the convention above applies to all cases where a regular expression is not static, but instead the expression is *supplied by a user* as a system configuration or postmaster filter, for example. Any evaluation of such a regular expression has to be done without any modifiers(e.g. ``$Variable =~ m{$Regex}``), in order to match the expectation of less advanced users and also provide backwards compatibility.

If modifiers are strictly necessary for user supplied regular expressions, it's always possible to use embedded modifiers (e.g. ``(?:(?i)SmAlL oR lArGe)``). For details, please see `perlretut <http://perldoc.perl.org/perlretut.html#Embedding-comments-and-modifiers-in-a-regular-expression>`__.

**Using String Parts in Variables**

If you need to extract part of a string into another variable, usage of the ``r`` modifier is encouraged. This modifier keeps the matched variable intact and instead provides the substitution result as a return value.

Good:

.. code-block:: perl

   my $NewText = $Text =~ s{
       \A
       Prefix
       (
           Text
       )
   }
   {NewPrefix$1Postfix}xmsr;

Poor:

.. code-block:: perl

   my $NewText = $Text;
   $NewText =~ s{
       \A
       Prefix
       (
           Text
       )
   }
   {NewPrefix$1Postfix}xms;

.. note:: Beginning and End

   To match the a *string*'s boundary, you should generally use ``\A`` and ``\z`` instead of the more generic ``^`` and ``$``. Use the ``^`` and ``$`` to match tho boundaries of *lines* within a multiline string.

   .. code-block:: perl

      $Text =~ m{
         \A      # beginning of the string
         Content # some string
         \z      # end of the string
      }xms;

      $MultilineText =~ m{
         \A                      # beginning of the string
         .*
         (?: \n Content $ )+      # one or more lines containing the same string
         .*
         \z                      # end of the string
      }xms;

**Capture Groups**

Named capture groups provide improved readability, are easier to understand, prevent mix-ups when matching more than one capture group, and enable extension without risking accidental bugs. Usage of named capture groups is encouraged particularly for multi-matches.

Good:

.. code-block:: perl

   $Contact =~ s{
       \A
       [ ]*
       (?'TrimmedContact'
           (?'FirstName' \w+ )
           [ ]+
           (?'LastName' \w+ )
       )
       [ ]+
       (?'Email' [^ ]+ )
       [ ]*
       \z
   }
   {$+{TrimmedContact}}xms;
   my $FormattedContact = "$+{LastName}, $+{FirstName} ($+{Email})";

Poor:

.. code-block:: perl

   $Contact =~ s{
       \A
       [ ]*
       (
           ( \w+ )
           [ ]+
           ( \w+ )
       )
       [ ]+
       ( [^ ]+ )
       [ ]*
       \z
   }
   {$1}xms;

   my $FormattedContact = "$3, $2 ($4)";

Naming Convention
=================
:ref:`- jump top - <PageNavigation code-style-guide>`

* Names and comments are written in English.
* Variables, objects, and methods are descriptive nouns or noun phrases with the first letter set upper case (`CamelCase <https://en.wikipedia.org/wiki/CamelCase>`_).

.. important::

   Names should be as descriptive as possible. A reader should be able to say what is meant by a name without digging too deep into t.. code-block. E.g. use ``$ConfigItemID`` instead of ``$ID``. Examples: ``@TicketIDs``, ``$Output``, ``StateSet()``, etc.

Variables
~~~~~~~~~

**Declaration**
   If you have several variables, you can declare them in one line if they "belong together":

   .. code-block:: perl

      my ( $Minute, $Hour, $Year );

   Otherwise break it into separate lines:

   .. code-block:: perl

      my $Minute;
      my $ID;

   Do not set to ``undef`` or ``''`` in the declaration. This can mask mistakes.

   .. code-block:: perl

      my $Variable = undef;

      # is the same as

      my $Variable;

.. important:: Exception

   You can set a variable to ``''`` if you want to concatenate strings:

   .. code-block:: perl

      my $SqlStatement = '';

      for my $Part (@Parts) {
          $SqlStatement .= $Part;
      }

   Otherwise you would get an "uninitialized" warning.

Subroutines
===========
:ref:`- jump top - <PageNavigation code-style-guide>`

**Handling of parameters**

To fetch the parameters passed to subroutines, the hash ``%Param`` (not ``%Params``) is usually used. This leads to more readable code. Every time we use ``%Param`` in the subroutine we know it is the parameter hash passed to the subroutine.

Just in some exceptions a regular list of parameters should be used.

Correct:

.. code-block:: perl

   sub TestSub {
       my ( $Self, %Param ) = @_;
   }

Incorrect:

.. code-block:: perl

   sub TestSub {
       my ( $Self, $Param1, $Param2 ) = @_;
   }

.. note:: Advantages

   * No need to change the code when a new parameter is required.
   * Calling a function with named parameters is more readable.

**Multiple named parameters**

If a function call requires more than one named parameter, split them into multiple lines:

Correct:

.. code-block:: perl

   $Self->{LogObject}->Log(
       Priority => 'error',
       Message  => "Need $Needed!",
   );

Incorrect:

.. code-block:: perl

   $Self->{LogObject}->Log( Priority => 'error', Message  => "Need $Needed!", );

**Using ``return`` statements**

Subroutines have to have a ``return`` statement. The explicit ``return`` statement is preferred over the implicit way (result of last statement in subroutine) as this clarifies what the subroutine returns.

**``undef`` return:**

.. code-block:: perl

   sub TestSub {
       ...
       return; # return undef, but not the result of the last statement
   }

Explicit return:

Explicit return values means that you should not have a ``return`` statement followed by a subroutine call.

Good:

.. code-block:: perl

   return $Self->{DBObject}->Do( ... );

The following example is better as this says explicitly what is returned. With the example above the reader doesn't know what the return value is as he might not know what ``Do()`` returns.

Better:

.. code-block:: perl

   return if !$Self->{DBObject}->Do( ... );
   return 1;

If you assign the result of a subroutine to a variable, a good variable name indicates what was returned:

Best:

.. code-block:: perl

   my $SuccessfulInsert = $Self->{DBObject}->Do( ... );
   return $SuccessfulInsert;

Module Requirements
===================
:ref:`- jump top - <PageNavigation code-style-guide>`

**Required ``use`` statements**

* ``use strict`` and ``use warnings`` have to be the first two "use"s in a module.

Correct:

.. code-block:: perl

   package Kernel::System::ITSMConfigItem::History;

   use strict;
   use warnings;

   use Kernel::System::User;
   use Kernel::System::DateTime;

Incorrect:

.. code-block:: perl

   package Kernel::System::ITSMConfigItem::History;

   use Kernel::System::User;
   use Kernel::System::DateTime;

   use strict;
   use warnings;

Objects and Allocation
=======================
:ref:`- jump top - <PageNavigation code-style-guide>`

Many objects are available in the framework. You should not use every object in every file. Separate front-end from back-end wherever possible!

This means that ``DBObject`` is valid for core modules (``Kernel/System``), whereas ``LayoutObject`` and ``ParamObject`` are for use in frontend modules (``Kernel/Modules``).

Documentation Good Practice
***************************
:ref:`- jump top - <PageNavigation code-style-guide>`

This section aims at helping you create good documentation for your code and the project.

Using Perldoc
=============
.. _CodeStyleGuide UsingPerldoc:

:ref:`- jump top - <PageNavigation code-style-guide>`

**Documenting backend modules**

'NAME' section
   This section includes the module name, ' - ' as separator, and a brief description of the module purpose.

   .. code-block:: perl

      =head1 NAME

      Kernel::System::MyModule - Functions to read from and write to files

'SYNOPSIS' section
   This section shows usage example of commonly used module functions.

   Usage of this section is optional.

   .. code-block:: perl

      =head1 SYNOPSIS

      my $Object = $Kernel::OM->Get('Kernel::System::MyModule');

         Read data

            my $FileContent = $Object->Read(
                File => '/tmp/testfile',
            );

         Write data

            $Object->Write(
                Content => 'my file content',
                File    => '/tmp/testfile',
            );

'DESCRIPTION' section
   This section should give more in-depth information about the module. This will help shorten the 'NAME' section.

   Usage of this section is optional.

   .. code-block:: perl

      =head1 DESCRIPTION

      This module does not only handle files.

      It is also able to:

          * brew coffee
          * turn lead into gold
          * bring world peace

'PUBLIC INTERFACE' section
   This section marks the begin of all functions that are part of the API and therefore meant to be used by other modules.

.. code-block:: perl

      =head1 PUBLIC INTERFACE

'PRIVATE FUNCTIONS' section
   This section marks the begin of private functions.

   Functions below are not part of the API, to be used only within the module and therefore not considered stable.

   It is advisable to use this section whenever one or more private functions exist.

   .. code-block:: perl

      =head1 PRIVATE FUNCTIONS

**Documenting subroutines**

Subroutines should always be documented. The documentation contains a general description about what the subroutine does, a sample subroutine call and what the subroutine returns. It should be in this order and preceed the subroutine in the module code.

Correct:

.. code-block:: perl

   =head2 LastTimeObjectChanged()

      Calculates the last time the object was changed. It returns a hash reference with information about the object and the time.

      my $Info = $Object->LastTimeObjectChanged(
         Param => 'Value',
      );

      This returns something like:

      my $Info = {
         ConfigItemID    => 1234,
         HistoryType     => 'foo',
         LastTimeChanged => '08.10.2009',
      };

   =cut

   sub LastTimeObjectChanged {

.. note:: Expert Tip

   You can copy and paste a ``Data::Dumper`` output for the return values.

Database Interaction
********************
:ref:`- jump top - <PageNavigation code-style-guide>`

**Declaration of SQL statements**

Use the ``Prepare`` function for static SQL statements. This places the SQL statement and the bind parameters closer together.

Good:

.. code-block:: perl

   return if !$Self->{DBObject}->Prepare(
       SQL => '
           SELECT art.id
           FROM article art, article_sender_type ast
           WHERE art.ticket_id = ?
               AND art.article_sender_type_id = ast.id
               AND ast.name = ?
           ORDER BY art.id',
       Bind => [ \$Param{TicketID}, \$Param{SenderType} ],
   );


This code is easy to read and modify. The currently supported RDBMS can handle whitespace. For automatically generated SQL, such as that of the ``TicketSearch`` function, this indentation is not necessary.

**Returning on Errors**

Whenever you use database functions you should handle errors. If anything goes wrong, return from subroutine:

.. code-block:: perl

   return if !$Self->{DBObject}->Prepare( ... );

**Using Limit**

Use ``Limit => 1`` if you expect just one row to be returned.

.. code-block:: perl

   $Self->{DBObject}->Prepare(
       SQL   => 'SELECT id FROM users WHERE username = ?',
       Bind  => [ \$Username ],
       Limit => 1,
   );

**``while`` Loop Usage**

Always use the ``while`` loop to ensure the statement handle is released. This prevents weird bugs.

JavaScript
**********
:ref:`- jump top - <PageNavigation code-style-guide>`

All JavaScript is loaded in all browsers (no browser hacks in the template files). The code takes care of browser compatibility issues..

Directory Structure
====================
:ref:`- jump top - <PageNavigation code-style-guide>`

Directory structure inside the ``js/`` folder:

.. code-block:: 

   * js
       * thirdparty              # thirdparty libs always have the version number inside the directory
           * ckeditor-3.0.1
           * jquery-1.3.2
       * Core.Agent.*            # stuff specific to the agent interface
       * Core.Customer.*         # customer interface
       * Core.*                  # common API

**Thirdparty Code**

Every thirdparty module gets its own subdirectory: "module name"-"version number" (e.g. ckeditor-3.0.1, jquery-1.3.2). Inside of that, file names should not have a version number or postfix included (wrong: ``jquery/jquery-1.4.3.min.js``, right: ``jquery-1.4.3/jquery.js``).

Variables
==========
:ref:`- jump top - <PageNavigation code-style-guide>`

Variable names should be CamelCase, just like in Perl.

.. note::

   Variables that hold a jQuery object should start with ``$``, for example: ``$Tooltip``.

Functions
==========
:ref:`- jump top - <PageNavigation code-style-guide>`

Function names should be CamelCase, just like in Perl.

Event Handling
===============
:ref:`- jump top - <PageNavigation code-style-guide>`

* Always use ``$.on()`` instead of the event-shorthand methods of jQuery for better readability (wrong: ``$SomeObject.click(...)``, right: ``$SomeObject.on('click', ...``).
* If you ``$.on()`` events, make sure to ``$.off()`` them beforehand, to make sure that events will not be bound twice, should t.. code-block be executed another time.
* Make sure to use ``$.on()`` with namespacing, such as ``$.on('click.<Name>')``.

HTML
****
:ref:`- jump top - <PageNavigation code-style-guide>`

* Use HTML 5 notation. 
* Avoid self-closing tags for non-void elements (such as div, span, etc.).
* Use proper indentation. 
* Place elements which contain other non-void child elements on a new level.
* Use the proper CSS classes instead of empty HTML elements for proper spacing.
* All CSS should either be added by using predefined classes or using JavaScript.
* Include JavaScript in the proper module or global library. Use ``$LayoutObject->AddJSData()`` to pass data to the front-end, if necessary.

CSS
***
:ref:`- jump top - <PageNavigation code-style-guide>`

* Minimum resolution is 1024x768px.
* The layout is liquid meaning all available space is dynamically be used.
* Absolute size measurements are in *px* for cross-browser consistency.
* As documentation is made with CSSDOC, a CSSDOC comment is required for all logical blocks.

CSS Writing Rules
=================
:ref:`- jump top - <PageNavigation code-style-guide>`

* All definitions have a ``{`` in the same line as the selector, all rules are defined in one row per rule, the definition ends with a row with a single ``}`` in it. See the following example:

.. code-block:: css

   #Selector {
       width: 10px;
       height: 20px;
       padding: 4px;
   }

* Between ``:`` and the rule value, there is a space.
* Every rule has an indent of 4 spaces.
* If multiple selectors are specified, separate them with comma and put each one on an own line:

.. code-block:: css

   #Selector1,
   #Selector2,
   #Selector3 {
       width: 10px;
   }

* If rules are combinable, combine them (e.g. combine ``background-position``, ``background-image``, ... into ``background``).
* Rules should be in a logical order within a definition (all color specific rule together, all positioning rules together, ...).
* All IDs and names are written in CamelCase notation:

.. code-block:: html

   <div class="NavigationBar" id="AdminMenu"></div>

.. important:: **Frontend Architecture**

   We follow the `Object Oriented CSS <http://wiki.github.com/stubbornella/oocss/>`__ approach. In essence, this means that the layout is achieved by combining different generic building blocks to realize a particular design.

   Wherever possible, module specific design should not be used. Therefore we also do not work with IDs on the ``body`` element, for example, if it can be avoided.

Code Commenting
***************
:ref:`- jump top - <PageNavigation code-style-guide>`

In general, your code should be readable and self-explaining. Don't write a comment to explain the code, this is unnecessary duplication. Good comments should explain *why* the code is there, any possible side effects, and anything that might be special or unusually complicated.

Please adhere to the following guidelines:

* Make code readable that comments are not needed.
* Use precisely named variable and functions.
* Adhere to: Don't repeat yourself (`DRY Programming <https://en.wikipedia.org/wiki/Don't_repeat_yourself>`_)

Perl Examples
=============
:ref:`- jump top - <PageNavigation code-style-guide>`

DRY Infraction:

.. code-block:: perl

   # get config object
   my $ConfigObject = $Kernel::OM->Get('Kernel::Config');

Usually code comments should explain the *purpose* of the code, not how it works in detail. There might be exceptions for specially complicated code, but in this case also a refactoring to make it more readable could be commendable.

.. important:: Golden Rule

   * Document everything that is unclear, tricky, or which puzzled you during development.


* Use full-line sentence-style comments to document algorithm paragraphs. Always use full sentences (uppercase first letter and final period). Subsequent lines of a sentence should be indented.

.. code-block:: perl

   # Check if object name is provided.
   if ( !$_[1] ) {
       $_[0]->_DieWithError(
           Error => "Error: Missing parameter (object name)",
       );
   }

   # Record the object we are about to retrieve to potentially build better error messages.
   # Needs to be a statement-modifying 'if', otherwise 'local' is local
   #   to the scope of the 'if'-block.
   local $CurrentObject = $_[1] if !$CurrentObject;


* Use short end-of-line comments to add detail information. These can either be a complete sentence (capital first letter and period) or just a phrase (lowercase first letter and no period).

.. code-block:: perl

   $BuildMode = oct $Param{Mode};   # *from* octal, not *to* octal

   # or

   $BuildMode = oct $Param{Mode};   # Convert *from* octal, not *to* octal.

JavaScript
==========
:ref:`- jump top - <PageNavigation code-style-guide>`

The `commenting guidelines for Perl <code-style-guide.html#code-style-guide-perl-code-comments>`_ also apply to JavaScript.

* Single line comments are done with ``//``.
* Longer comments are done with ``/* ... */``.
* If you comment out parts of your JavaScri.. code-block, only use ``//`` because ``/* ... */`` can cause problems with Regular Expressions in the code.