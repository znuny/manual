.. meta::
   :description: YAML reference for defining Znuny ITSM Configuration Item classes — attribute options like Key, Name, Searchable and Input, plus every available input type with examples.
   :keywords: znuny ci class definition, configuration item yaml, itsm cmdb schema, ci attribute types, znuny configuration management reference

.. _PageNavigation annexes_itsm_configurationitemdefinition_index:

Configuration Item Definitions
##############################

In Znuny's ITSM Configuration Management, defining a **Configuration Item (CI) Class** involves specifying various elements that determine the structure and behavior of the CI. These elements are defined using a YAML-based configuration. Here's a breakdown of the possible definition elements:

Base Options
************

Key
===

- **Description**: A unique identifier for the attribute within the CI class.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Vendor

Name
====

- **Description**: The display name of the attribute, shown in the user interface.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Vendor
    Name: Vendor Name

Searchable
==========

- **Description**: Indicates whether the attribute is searchable.
- **Values**:
  - ``1``: Searchable
  - ``0``: Not searchable
- **Example**:

.. code-block:: yaml

  ---
  - Key: Vendor
    Name: Vendor Name
    Searchable: 1

Input
=====

- **Description**: Defines the input properties for the attribute.
- **Sub-elements**:
  - **Type**: Specifies the input type.
  - **Type Options**: Options specific to the chosen type.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Motivation
    Name: Purchase Motivation
    Searchable: 1
    Input:
      Type: Text
      Size: 50
      MaxLength: 100
      Required: 1

Count of Options
================

1. CountMin
2. CountMax
3. CountDefault

- **Description**: Defines the number of instances for an attribute. Useful for attributes that can have multiple entries like hard drives or CPUs.
- **Example**: Requires none, adds one by default, but allows up to 10.

.. code-block:: yaml

  ---
  - Key: Vendor
    Name: Vendor Name
    Searchable: 1
    Input:
      Type: Text
      Size: 50
      MaxLength: 100
      Required: 1
    CountMin: 0
    CountMax: 10
    CountDefault: 1

Sub
===

- **Description**: Allows nesting of sub-attributes under a main attribute.
- **Example**:

.. code-block:: yaml

  ---
  - Key: NIC
    Name: Network Adapter
    Input:
      Type: Text
      Size: 50
      MaxLength: 100
      Required: 1
    CountMin: 0
    CountMax: 10
    CountDefault: 1
    Sub:
    - Key: IPoverDHCP
      Name: IP over DHCP
      Input:
        Type: GeneralCatalog
        Class: ITSM::ConfigItem::YesNo
        Translation: 1
        Required: 1
    - Key: IPAddress
      Name: IP Address
      Searchable: 1
      Input:
        Type: Text
        Size: 40
        MaxLength: 40
        Required: 1
      CountMin: 0
      CountMax: 20
      CountDefault: 0

Available Input Types
*********************

CI
==

- **Description**: Search for and add a reference to other configuration items. Also creates a link of the defined type.
- **Example**:

.. code-block:: yaml

  ---
  - Key: CIParent
    Name: CI-Parent
    Searchable: 1
    Input:
      Type: CI
      CIClassName: Location
      CIClassLinkType: ParentChild
      Required: 0

CI Type Options
~~~~~~~~~~~~~~~

**CIClassName**
  Defines the referenced CI class using the name
**CIClassID**
  Defines the referenced CI class using the ID
**CIClassLinkType**
  Determines the link type with which the two CIs are to be linked if a link type exists. Expected values are like ``Normal``, ``ParentChild``, ``RelevantTo``, etc.

CI-Attachment
=============

- **Description**: Add one or more attachments to a configuration item.
- **Example**:

.. code-block:: yaml

  ---
  - Key: CIAttachment
    Name: Additional Attachment
    Searchable: 0
    Input:
      Type: CIAttachment
    CountMin: 0
    CountMax: 10

Customer
========

- **Description**: Add a customer user to the configuration item.
- **Example**:

.. code-block:: yaml

  ---
  - Key: CustomerUser
    Name: Billing Contact
    Searchable: 1
    Input:
      Type: Customer

CustomerCompany
===============

- **Description**: Add a customer company to the configuration item.
- **Example**:

.. code-block:: yaml

  ---
  - Key: ContractingCompany
    Name: Contractor
    Searchable: 1
    Input:
      Type: CustomerCompany

Date
====

- **Description**: Add a date that can be selected.
- **Example**:

.. code-block:: yaml

  ---
  - Key: DoB
    Name: Date of Birth
    Input:
      Type: Date

DateTime
========

- **Description**: Add a field to select a date and time.
- **Example**:

.. code-block:: yaml

  ---
  - Key: DowntimePlanned
    Name: Next planned downtime
    Input:
      Type: DateTime

GeneralCatalog
==============

- **Description**: A selection of a GeneralCatalog class. The options of the list are the GeneralCatalog class items, and the GeneralCatalog class must be defined first.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Roomtype
    Name: Roomtype
    Input:
      Type: GeneralCatalog
      Class: ITSM::ConfigItem::Roomtypes
      Required: 1

Integer
=======

- **Description**: A list of integer numbers to select from.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Beds
    Name: Beds
    Input:
      Type: Integer
      ValueMin: 1
      ValueMax: 6
      ValueDefault: 2
      Required: 1

Dummy
=====

- **Description**: Adds a structural element that does not hold any data.
- **Example**:

.. code-block:: yaml

  ---
  - Key: SectionOneLabel
    Name: Section One
    Input:
      Type: Dummy

Priority
========

- **Description**: Add a priority to the configuration item. Uses the configured ticket priorities.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Ticketpriority
    Name: Priority (optional)
    Searchable: 1
    Input:
      Type: Priority
      Required: 0

Queue
=====

- **Description**: Add a queue to the configuration item. Uses the configured ticket queues.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Queue
    Name: CI-Queue
    Searchable: 1
    Input:
      Type: Queue
      Required: 0

Service
=======

- **Description**: Add a service to the configuration item. Uses the configured services.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Service
    Name: Service (optional)
    Searchable: 1
    Input:
      Type: Service

SLA
===

- **Description**: Add an SLA to the configuration item. Uses the configured SLAs.
- **Example**:

.. code-block:: yaml

  ---
  - Key: SLA
    Name: Service Level Agreement
    Searchable: 1
    Input:
      Type: SLA
      Required: 0

State
=====

- **Description**: Add a state to the configuration item. Uses the configured ticket states.
- **Example**:

.. code-block:: yaml

  ---
  - Key: State
    Name: TicketState
    Searchable: 1
    Input:
      Type: State
      Required: 0

Text
====

- **Description**: A text field.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Firstname
    Name: Firstname
    Searchable: 1
    Input:
      Type: Text

TextArea
========

- **Description**: A textarea field.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Address
    Name: Delivery Address
    Searchable: 0
    Input:
      Type: TextArea

TextLink
========

- **Description**: A text field shown as a clickable link. The placeholder ``<VALUE>`` in the URL parameter will be replaced by the item's text.
- **Example**:

.. code-block:: yaml

  ---
  - Key: SearchTerm
    Name: Search term
    Input:
      Type: TextLink
      URL: https://example.com/?q=<VALUE>

Type
====

- **Description**: Add a type to the configuration item. Uses the existing, valid ticket types.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Type
    Name: Type
    Searchable: 1
    Input:
      Type: Type

User
====

- **Description**: Adds a list of the system's agents to the configuration item, to select from.
- **Example**:

.. code-block:: yaml

  ---
  - Key: Owner
    Name: Owner
    Searchable: 1
    Input:
      Type: User
      Required: 0
