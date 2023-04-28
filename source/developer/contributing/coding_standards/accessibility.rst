.. _PageNavigation accessibility:

Accessibility Guide
###################

This document is supposed to explain basics about accessibility issues and give guidelines for contributions to the software.

Accessibility Basics
********************
:ref:`- jump top - <PageNavigation accessibility>` 

Accessibility is a general term used to describe the degree to which a product, device, service or environment is accessible by as many people as possible. Accessibility can be viewed as the "ability to access" and possible benefit of some system or entity. Accessibility is often used to focus on people with disabilities and their right of access to entities, often through use of assistive technology.

In the context of web development, accessibility has a focus on enabling people with impairments full access to web interfaces. For example, this group of people can include partially visually impaired or completely blind people. While the former can still partially use the GUI, the latter have to completely rely on assistive technologies such as software which reads the screen to them (screen readers).

Why is it Important for Znuny
*****************************
:ref:`- jump top - <PageNavigation accessibility>` 

To enable impaired users access to the software is a valid goal in itself. It shows respect.

Furthermore, fulfilling accessibility standards is becoming increasingly important in the public sector (government institutions) and large companies, which both belong to the target markets of the software.


Common Developer Tasks
**********************
:ref:`- jump top - <PageNavigation accessibility>` 

Think Blind
============
:ref:`- jump top - <PageNavigation accessibility>` 

You may ask, "How can I successfully work on accessibility issues when I'm not disabled? Easy, Pretend to be blind.

Do this:

Close your eyes!

Try then to use the software only with a screen-reader program and your keyboard. This tactic should give you an idea of how it feels for a person of limited vision to work with the software.


Get a Screen Reader
===================
:ref:`- jump top - <PageNavigation accessibility>` 

Mac and Windows both include screen reading utilities.

Mac:
   `VoiceOver <https://support.apple.com/guide/voiceover/welcome/mac>`_
Windows:
   `Narrator <https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1>`_
Open Source Alternatives:
   While most other commercial screen readers such as JAWS (perhaps the most well-known) can be pricey, there are open source alternatives:

   * `NVDA <http://www.nvaccess.org/>`__, a screen reader for Windows.
   * `ORCA <https://wiki.gnome.org/Projects/Orca>`__, a screen reader for Gnome/Linux.



Accessibility Standards
***********************
:ref:`- jump top - <PageNavigation accessibility>` 

This section is included for reference only, you do not have to study the standards themselves to be able to work on accessibility issues in the software. We'll try to extract the relevant guidelines in this document.

Web Content Accessibility Guidelines (WCAG)
===========================================
:ref:`- jump top - <PageNavigation accessibility>` 

This W3C standard gives general guidelines for how to create 
accessible web pages.

* `WCAG 2.0 <http://www.w3.org/TR/WCAG20/>`_
* `How to Meet WCAG 2.0 <http://www.w3.org/WAI/WCAG20/quickref/>`_
* `Understanding WCAG 2.0 <http://www.w3.org/TR/UNDERSTANDING-WCAG20/>`__

WCAG has different levels of accessibility support. We currently plan to support level A, as AA and AAA deal with matters that seem not relevant for the software.

Accessible Rich Internet Application (WAI-ARIA) 1.0
===================================================
:ref:`- jump top - <PageNavigation accessibility>` 

This standard deals with the special issues arising from the shift away from static content to dynamic web applications. It deals with questions like how a user can be notified of changes in the user interface resulting from AJAX requests, for example.

* `WAI-ARIA 1.0 <https://www.w3.org/TR/wai-aria/>`_

Implementation Guidelines
*************************
:ref:`- jump top - <PageNavigation accessibility>` 

Non-text Content Alternatives
=============================
:ref:`- jump top - <PageNavigation accessibility>` 

**Goal:**
   All non-text content that is presented to the user has a text alternative that serves the equivalent purpose. (WCAG 1.1.1)

It is very important to understand that screen readers can only present textual information and available metadata to the user. To give you an example, whenever a screen reader sees ``<a href="#" class="CloseLink"></a>``, it can only read "link" to the user, but not the target of this link. With a slight improvement, it would be accessible: ``<a href="#" class="CloseLink" title="Close this widget"></a>``. In this case the user would hear "link close this widget", voila!

It is important to always formulate the text in a most "speaking" way. Just imagine it is the only information that you have. Will it help you? Can you understand its purpose just by hearing it?

Please follow these rules when working on the software:

* Wherever possible, use speaking texts and formulate in real, understandable and precise sentences. "Close this widget" is much better than "Close", because the latter is redundant.
* Links always must have either text content that is spoken by the screen reader (``<a href="#" >Delete this entry</a>``), or a ``title`` attribute (``<a href="#" title="Close this widget"></a>``).
* Images must always have an alternative text that can be read to the user (``<img src="house.png" alt="Image of a house" />``)
  
Simplifying Navigation
======================
:ref:`- jump top - <PageNavigation accessibility>` 

**Goal:**
   Allow the user to easily navigate the current page and the entire application.

The ``title`` tag is the first thing a user hears from the screen reader when opening a web page. For the software, there is also always just one ``h1`` element on the page, indicating the current page (it contains part of the information from ``title``). This navigational information helps the user to understand where they are, and what the purpose of the current page is.

Please follow these rules when working on the software:

* Always give a precise title to the page that allows the user to understand where they currently are.

Screen readers can use the built-in document structure of HTML (headings ``h1`` to ``h6``) to determine the structure of a document and to allow the user to jump around from section to section. However, this is not enough to reflect the structure of a dynamic web application. That's why ARIA defines several "landmark" roles that can be given to elements to indicate their navigational significance.

To keep the validity of the HTML documents, the ``role`` attributes (ARIA landmark roles) are not inserted into the source code directly, but instead by classes which will later be used by the JavaScript functions in ``OTRS.UI.Accessibility`` to set the corresponding ``role`` attributes on the node.

* Use WAI-ARIA Landmark Roles to structure the content for screen readers.

Banner: 
   ``<div class="ARIARoleBanner"></div>`` will become ``<div class="ARIARoleBanner" role="banner"></div>``

Navigation: 
  ``<div class="ARIARoleNavigation"></div>`` will become ``<div class="ARIARoleNavigation" role="navigation"></div>``

Search function:
   ``<div class="ARIARoleSearch"></div>`` will become ``<div class="ARIARoleSearch" role="search"></div>``

Main application area:
   ``<div class="ARIARoleMain"></div>`` will become ``<div class="ARIARoleMain" role="main"></div>``

Footer:
   ``<div class="ARIARoleContentinfo"></div>`` will become ``<div class="ARIARoleContentinfo" role="contentinfo"></div>``

For navigation inside of ``<form<`` elements, it is necessary for the impaired user to know what each input elements purpose is. This can be achieved by using standard HTML ``<label>`` elements which create a link between the label and the form element.

When an input element gets focus, the screen reader will usually read the connected label, so that the user can hear its exact purpose. An additional benefit for seeing users is that they can click on the label, and the input element will get focus (especially helpful for checkboxes, for example).

* Provide ``<label>`` elements for *all* for element (``input``, ``select``, ``textarea``) fields.

.. note:: Example
   
   ``<label for="date">Date:</label><input type="text" name="date" id="date"/>``

Make Interaction Possible
=========================
:ref:`- jump top - <PageNavigation accessibility>` 

**Goal:**
   Allow the user to perform all interactions just by using the keyboard.

While it is technically possible to create interactions with JavaScript on arbitrary HTML elements, this must be limited to elements that a user can interact with by using the keyboard. Specifically, they need to be able to give focus to the element and to interact with it. For example, a push button to toggle a widget should not be realized by using a ``span`` element with an attached JavaScript ``onclick`` event listener, but it should be (or contain) an ``a`` tag to make it clear to the screen reader that this element can cause interaction.

Please follow these rules when working on the software:

* For interactions, always use elements that can receive focus, such as ``a``, ``input``, ``select`` and ``button``.
* Make sure that the user can always identify the nature of the interaction (see rules about non-textual content and labelling of form elements).

**Goal:**
   Make dynamic changes known to the user.

A special area of accessibility problems are dynamic changes in the user interface, either by JavaScript or also by AJAX calls. The screen reader will not tell the user about changes without special precautions. This is a difficult topic and cannot yet be completely explained here.

Please follow these rules when working on the software:

* Always use the validation framework ``OTRS.Validate`` for form validation.

This will make sure that the error tooltips are being read by the screen reader. That way the blind user a) knows the item which has an error and b) get a text describing the error.
* Use the function ``OTRS.UI.Accessibility.AudibleAlert()`` to notify the user about other important UI changes.

* Use the ``OTRS.UI.Dialog`` framework to create modal dialogs. These are already optimized for accessibility.


General Screen Reader Optimizations
====================================
:ref:`- jump top - <PageNavigation accessibility>` 

**Goal:**
   Help screen readers with their work.

Please follow these rules when working on the software:

* Each page must identify its own main language so that the screen reader can choose the right speech synthesis engine.

.. note:: Example
   
   ``<html lang="fr">...</html>``