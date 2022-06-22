# Znuny Documentation README

The branches `production` and `staging` are deployed on with every push.

- Branch `production` is available at https://doc.znuny.org/manual/ after the deployment
- Branch `staging` is available at https://doc.internal.znuny.org/ after the deployment

## Requirements

- sphinx-book-theme
- [sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/)
- [sphinxcontrib.mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid)
- [sphinx_code_tabs](https://github.com/coldfix/sphinx-code-tabs)
- [sphinx_fontawesome](https://github.com/fraoustin/sphinx_fontawesome)

## Style Guide

Here are some notes to the styling used in our documentation.

### Headings

For H1..H6, we have the following conventions.

'#' for Parts

'*' for Chapters

'=' for Sections

'~' for Subsections

'^' for Sub-subsections

'.' for sub-sub-subsections.

### Specials

Use [Mermaid](https://mermaid-js.github.io/mermaid) to create graphs whenever needed. Check the documentaion of [sphinxcontrib.mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) for details.

### ALT Tags

When using images, each image must contain an 'alt' tag.

Use the tag 'Image *filename*' without extension.

```rst

.. image:: images/some_image.png
    :alt: Image Some Image

```

### Page Navigation Links

Insert page navigation where needed. If you need to navigate between manual sections or pages, include a page navigation link at the top of the page.

The link is constructed from the chapter and filename and prefixed with ``.. _PageNavigation``.

Here is an example:

You want to link to this page.

```screen

source\
  admin\
    email\
      postmaster_mail_account.rst
```

1. Insert a reference link under the first heading in the page.

```rst

Configure Mailbox Collection
############################
.. _PageNavigation email_postmaster_mail_account:

```


Linking to this from any file can be done with.

```rst
:ref:`Link text <PageNavigation email_postmaster_mail_account>`
```

Add H2 - H6 reference links to the top of the heading

```rst
.. _ProcessManagement ProcessScope:

Process Element Scope
=====================
```
=======
'.' for Sub-sub-subsections

### Lists

Use of lists is broken down into the following two types and their uses.

#### Unordered

```rst

* Item 1
* Item 2

```

#### Enumeration

Enumeration is implicit when using just the #, so each list should start with the enumeration type 'A' or '1' for lettered or numbers lists. This way we explicitly set enumeration to alphabetic or numeric. All other signs follow suit.

```rst
A. Item A
#. Item B
```

```rst
1. Item 1
#. Item 2
```

### Navigation

Add a ``- jump top -`` element to all parts, chapters, and sections which nagvigates to the page top.

```rst
    :ref:`- jump top - <PageNavigation <pagename>` #see belew
```

#### Jump Top Anchor
At the top of each page, add a reference tag. This will be the tag you jump to (see above).

```rst

    .. _PageNavigation <pagename>:

```

### Structure

Each section of the manual has its purpose. Please adhere to the structure and only create a new structure when advised. Find a structure fitting for your topic and create a section for the topic, if not available. Make sure that your subject doesn't already appear in the documentation somewhere else.

### Specials

#### Mermaid Graph

Use [Mermaid](https://mermaid-js.github.io/mermaid) to create graphs whenever needed. 

Here a simple top down example.

```md
graph TD
    style End stroke-width:6px, width: 10px
    Start((Start))
    A[Request Pay Raise]
    B[Conduct Employee Review]
    C[Report New Salary]
    D[Notify Employee]
    End((End))
   Start --> A
   A --> B
   B --> C
   C --> D
   D --> End

```

Check the documentaion of [sphinxcontrib.mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) for details.


#### Font Awesome

To use icons in the documentation, just add a role

```md
:fa:`icon`
```
Read more at [sphinx_fontawesome](https://github.com/fraoustin/sphinx_fontawesome)

### DRY

Use references where ever possible to link to appropriate information like

Ticket and Article Menus. Use

```rst

:ref:`ticket menu <PageNavigation ticketviews_agentticketzoom_ticketmenu>`.
:ref:`article menu <PageNavigation ticketviews_agentticketzoom_articlemenu>`

```

