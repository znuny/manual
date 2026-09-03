.. meta::
   :description: Overview of Znuny's ITSM Configuration Management (CMDB) module — track configuration items, map dependencies, and link CIs to incidents, problems and changes.
   :keywords: znuny cmdb, configuration management database, configuration item, itsm asset management, ci relationships, znuny itsm

.. _PageNavigation itsmfeatures_configurationmanagement_index:

Configuration Management (CMDB)
###############################

In **Znuny**, **ITSM Configuration Management** is a module used to track and manage **Configuration Items (CIs)** within an organization's IT infrastructure. It provides a structured way to document, maintain, and control the relationships between different IT assets and services.

Key Functions of ITSM Configuration Management in Znuny
*******************************************************

1. **Configuration Item (CI) Management**

   - Create, modify, and track CIs (e.g., servers, applications, databases, networks, and workstations).
   - Supports custom attributes and classifications for different CI types.

2. **CI Relationships & Dependencies**

   - Link CIs to show dependencies (e.g., a database server linked to an application server).
   - Helps visualize how IT components interact and impact services.

3. **Change and Impact Analysis**

   - Supports change management processes by assessing the impact of modifications to IT infrastructure.
   - Helps with troubleshooting and root cause analysis by showing how failures in one component affect others.

4. **CMDB (Configuration Management Database)**

   - Acts as a central repository storing all CI details and relationships.
   - Ensures IT teams have accurate and up-to-date information on IT assets.

5. **Integration with Other ITSM Processes**

   - Links with Incident, Problem, and Change Management to provide relevant CI details when handling IT issues.
   - Allows service desk agents to quickly identify affected systems.

6. **Audit & Compliance**

   - Tracks historical changes and updates to CIs for compliance and reporting.
   - Supports access control so only authorized personnel can modify critical data.

7. **Automated CI Import & Discovery** (optional)

   - Can integrate with external tools or scripts to automate asset discovery and keep the CMDB updated.

How Znuny Uses ITSM Configuration Management
********************************************

- CIs are stored in CMDB objects and can be assigned owners, statuses, and attributes.
- You can customize CI classes based on your organization's needs.
- It supports workflow automation to streamline change tracking and approval processes.

Using Configuration Management
******************************

.. toctree::
   :maxdepth: 1

   overview
   add_ci
   viewing_ci
   update_ci
   add_class
