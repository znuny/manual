.. meta::
   :description: Understand how Znuny groups and roles work together to control who can see tickets, take actions, and access modules — and when to use roles instead of direct assignment.
   :keywords: znuny groups, znuny roles, permission model, group permissions, role assignment, queue access, access control

.. _PageNavigation concepts_groups_index:

Groups and Roles in Znuny
##########################

The Znuny authorization system is built on two complementary concepts: **groups** and **roles**. Together they answer the question: *who is allowed to do what, and where*.

- **Groups** define the scope of permission — which queues, modules, or system objects an agent can access, and with what level of access.
- **Roles** are named bundles of group permissions — a convenient shorthand that lets you assign a standard permission profile to many agents at once.

Think of groups as resources and roles as the permissions you build from them.

---

Groups
******

What a Group Is
===============

A group in Znuny is an entity defining a set of permissions.
Agents — directly or via roles — are assigned to these groups with specific permission levels.

Groups do not define organizational structure.
They define **what actions someone is allowed to take on system objects**.

Groups apply to:

- Tickets (via queue-to-group mapping)
- Packages and system modules
- Navigation entries
- Statistics
- Calendars
- Configuration item classes
- and more...

Group Permissions
=================

Each group grants permissions using the flags found in :ref:`pagenavigation annexes_permissions`.

How Groups Connect to Other Znuny Concepts
==========================================

Groups and Queues
-----------------

Every queue belongs to exactly one group.

This means:

- **rw** → full work access to this queue's tickets or module functionality.
- **ro** → search for and view a protected resource.

Groups and Agents
-----------------

Agents receive their group permissions through:

- Direct assignment (small installations or temporary exceptions)
- Roles (recommended)

.. important::

    Groups can be synchronized from an identity provider (e.g., LDAP, Active Directory, or SAML).

Groups and Modules
------------------

Screens (frontend) and system (backend) modules are group-protected.

Examples:

- **rw** on group ``admin`` → full access to admin screens.
- **ro** on group ``admin`` → read-only access to some configuration areas.

This enables delegated administration without granting unrestricted system access.

Why Groups Matter in Daily Operations
======================================

Queue Accessibility
-------------------

Groups determine **which agents see which tickets**.
This is critical when:

- Multiple departments share a single Znuny instance.
- Sensitive data must be isolated.
- Compliance (e.g., privacy, HR data) requires strict segmentation.

Workflow Governance
-------------------

Group-based permissions determine:

- Who can take ownership of a ticket
- Who may raise priority
- Who may add notes or update ticket content
- Who can move or create tickets in another team's queue
- Who can close or reopen tickets

Multi-Department Isolation
--------------------------

One Znuny instance can support completely separate organizational units:

- IT
- HR
- Finance
- Legal
- Facility Management
- Customer Service

Each department sees only its own queues, enforced by group permissions.

---

Roles
*****

What a Role Is
==============

A **role** in Znuny is a named bundle of group permissions.

Instead of assigning each agent to each group individually, you define a role once — "Service Desk Analyst", "Team Lead", "Billing Specialist" — and assign that role to many agents. The role carries the group memberships; agents inherit them automatically.

Roles do not grant permissions directly. They are a grouping mechanism that maps to groups, which in turn map to queues and modules.

The Permission Chain
====================

The full authorization path in Znuny is:

.. code-block:: text

    Agent → Role → Group → Queue / Module

.. mermaid::

   graph LR
       A[Agent] -->|assigned to| R[Role]
       R -->|grants permissions in| G[Group]
       G -->|controls access to| Q[Queue / Module]
       A -.->|or directly assigned to| G

An agent can receive group permissions either through a role or through direct assignment. Both paths are equally valid; roles are the recommended approach for anything beyond a handful of agents.

Roles vs. Direct Assignment
============================

+----------------------------+------------------------------+----------------------------------+
| Aspect                     | Direct Assignment            | Via Role                         |
+============================+==============================+==================================+
| Setup speed                | Fast for one agent           | Slightly more setup up-front     |
+----------------------------+------------------------------+----------------------------------+
| Consistency                | Each agent configured        | Single definition shared         |
|                            | individually                 | by all role members              |
+----------------------------+------------------------------+----------------------------------+
| Change propagation         | Must update every agent      | Update the role once             |
+----------------------------+------------------------------+----------------------------------+
| Audit clarity              | Hard to see who has what     | Role name conveys intent         |
+----------------------------+------------------------------+----------------------------------+
| Scale                      | Does not scale               | Scales to any team size          |
+----------------------------+------------------------------+----------------------------------+
| Recommended for            | Single-agent installations   | All other cases                  |
|                            | or temporary exceptions      |                                  |
+----------------------------+------------------------------+----------------------------------+

Enforcing Roles-Only Assignment
================================

To prevent direct agent-to-group assignment entirely, disable the
``Kernel/Modules/AdminUserGroup.pm`` module via SysConfig. This removes the
**Agents ↔ Groups** admin screen.

Navigate to **Admin → System Configuration**, search for
``Frontend::Module###AdminUserGroup``, and set the module to inactive.

With the module disabled:

- The **Agents ↔ Groups** screen is no longer available.
- The group assignment step is absent from the agent create and edit forms — new
  agents can only be assigned to roles, not to groups directly.
- All group permissions flow exclusively through roles, making the role the
  single point of control for every agent's access.

This is the recommended configuration for installations where consistent,
auditable, role-based access control is required.

When to Use Roles
=================

Use roles whenever:

- More than two or three agents share the same permission profile.
- Your team structure maps to recognizable job functions (e.g., first-line support, team lead, billing).
- You want to onboard new agents quickly by assigning a role rather than replicating permissions.
- You use LDAP or Active Directory and want to synchronize group memberships via role.

Use direct assignment only for:

- One-off exceptions or temporary elevated access.
- Very small installations where one or two agents need unique permissions.

Practical Example
=================

Consider a service desk with three tiers of agents.

**Role: Service Desk Analyst**

+------------------+------------+
| Group            | Permission |
+==================+============+
| support-queue    | rw         |
+------------------+------------+
| service-desk     | rw         |
+------------------+------------+
| stats            | ro         |
+------------------+------------+

**Role: Team Lead**

+------------------+------------+
| Group            | Permission |
+==================+============+
| support-queue    | rw         |
+------------------+------------+
| service-desk     | rw         |
+------------------+------------+
| escalation-queue | rw         |
+------------------+------------+
| stats            | rw         |
+------------------+------------+
| admin            | ro         |
+------------------+------------+

**Role: Billing Specialist**

+------------------+------------+
| Group            | Permission |
+==================+============+
| billing-queue    | rw         |
+------------------+------------+
| stats            | ro         |
+------------------+------------+

Any agent assigned to "Team Lead" automatically has access to escalation tickets and read-only admin visibility. Adding a new team lead requires one role assignment — no per-agent group configuration needed.

Stacking Roles and Direct Permissions
======================================

An agent can hold multiple roles simultaneously. Znuny merges the permissions from all roles and any direct group assignments using a **most-permissive wins** rule: if one path grants ``rw`` and another grants ``ro`` on the same group, the agent receives ``rw``.

This makes roles additive — you can grant a temporary exception via direct assignment without creating a dedicated role for a one-off case.

Identity Provider Synchronization
===================================

When using LDAP, Active Directory, or SAML, Znuny can synchronize group membership automatically. The typical mapping is:

- Identity provider groups → Znuny groups (direct)
- Identity provider groups → Znuny roles (which then confer group permissions)

This allows onboarding and offboarding to flow from your directory service without manual permission changes in Znuny.

.. important::

    When group membership is synchronized from an identity provider, manual changes made in Znuny will be overwritten on the next sync. Treat the identity provider as the authoritative source.

---

How Groups and Roles Work Together
************************************

The permission system is designed to be composed in layers:

1. **Groups** define permission scope — the objects and the access level.
2. **Queues** each belong to exactly one group — so group permissions translate directly to queue visibility and ticket actions.
3. **Roles** aggregate group permissions under a meaningful job-function label.
4. **Agents** are assigned roles and optionally receive direct group overrides.

.. mermaid::

   graph TD
       subgraph "Permission Scope"
           G1[Group: support-queue]
           G2[Group: billing-queue]
           G3[Group: admin]
           G4[Group: stats]
       end

       subgraph "Roles"
           R1[Role: Service Desk Analyst]
           R2[Role: Team Lead]
           R3[Role: Billing Specialist]
       end

       subgraph "Agents"
           A1[Alice]
           A2[Bob]
           A3[Carol]
       end

       R1 --> G1
       R1 --> G4
       R2 --> G1
       R2 --> G3
       R2 --> G4
       R3 --> G2
       R3 --> G4

       A1 -->|assigned| R1
       A2 -->|assigned| R2
       A3 -->|assigned| R3

A change to the "Service Desk Analyst" role — adding a new queue group or adjusting a permission level — propagates instantly to every agent who holds that role.
No per-agent configuration is needed.

.. seealso::

    - :ref:`pagenavigation annexes_permissions` — full list of permission flags and their meaning.
    - Administrator Interface → Groups — configure groups in the admin panel.
    - Administrator Interface → Roles — create and assign roles.
    - Administrator Interface → Roles ↔ Groups — map group permissions onto roles.
