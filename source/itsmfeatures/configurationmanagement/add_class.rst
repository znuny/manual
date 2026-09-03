.. meta::
   :description: Create a new Configuration Item class in Znuny via General Catalog, then define its attribute structure as YAML under Admin → Config Items.
   :keywords: znuny ci class, add configuration item class, general catalog, itsm::configitem::class, ci definition yaml

.. _PageNavigation itsmfeatures_configurationmanagement_add_class:

Add New Configuration Item Classes
##################################

In **Znuny ITSM**, **Configuration Item (CI) Classes** are managed through the **General Catalog**. This approach allows for centralized management of various categorizations used across the system. Here's how you can add a new CI Class:

1. Access the General Catalog

  - **Log in** to Znuny as an **Administrator**.
  - Navigate to **Admin**.
  - Select **General Catalog**.

2. Add a New CI Class

  - In the General Catalog, locate the **'Class'** entry for Configuration Items:
    - This is typically found under **'ITSM::ConfigItem::Class'**.
  - Click on **'Add Catalog Item'**.
  - Fill in the details:
      **Name**
          Enter the name of your new CI Class (e.g., "Cloud Service").
      **Permission Group**
          Select the group that controls access to the class. Members of that group need at least ``ro`` permission to view CIs of this class, or ``rw`` to create and edit them.
      **Comment**
          Optionally, add a description or notes about this class.
      **Validity**
          Mark the validity of the class.
  - Click **'Save'** to add the new class.

3. Define the CI Class Structure

  - After adding the new class, navigate to **Admin → Config Items**.
  - Select your newly created CI Class from the list.
  - Click on **'Change class definition'**.
  - Define the structure of your CI Class using **YAML** format. This includes specifying attributes and their data types. For example:

  .. code-block:: yaml

      ---
      - Key: Vendor
        Name: Vendor
        Searchable: 1
        Input:
          Type: Text
          Size: 50
          MaxLength: 50
      - Key: Model
        Name: Model
        Searchable: 1
        Input:
          Type: Text
          Size: 50
          MaxLength: 50
      - Key: Description
        Name: Description
        Searchable: 1
        Input:
          Type: TextArea

.. note::

    This structure defines attributes like Vendor, Model, and Description for the CI Class. See :ref:`PageNavigation annexes_itsm_configurationitemdefinition_index` for the full reference of available attribute options and input types.

4. After defining the structure, click **'Save'** to apply the changes.
