Groups in Znuny
###############

A foundational element of access control, workflow governance, and ticket visibility.

In Znuny, *groups* are one of the core building blocks of the authorization system. They determine what an agent can see, what they can do, and how ticket workflows are segmented across departments.

Consider groups as the permission layer, whereas roles and queues represent functional or organizational layers.


What a Group Is
=================

A group in Znuny is a container defining a set of permissions.
Agents (directly or via roles) are assigned to these groups with specific permission levels.

Groups do not define organizational structure.  
They define **what actions someone is allowed to take on system objects**.

Groups apply to:

- Tickets (via queue-to-group mapping)
- Packages and system modules
- Navigation entries
- Statistics
- Calendars
- Configuration Item Classes
- and more...

Group Permissions (The Backbone)
================================

Each group grants permissions using the flags found in :ref:`pagenavigation annexes_permissions` .

Important: **rw does not equal admin**.  
It applies only to the specific object (queue, module, field, etc.) owned by the group.


How Groups Connect to Other Znuny Concepts
==========================================

Groups and Queues
-----------------

Every queue belongs to exactly one group.

This means:

- **rw** → full work access to this queue’s tickets or modules functionality.
- **ro** → search for and view protected resource.

Groups and Agents
------------------

Agents receive their group permissions through:

- Direct assignment (small installations)
- Roles (recommended)

.. important::
    
    Groups can be synchronized from the identity provider (e.g., LDAP, AD, or SAML).

Groups Modules
--------------

Screens (Frontend) and System (Backend) Modules are group-protected.

Examples:

- **rw** on group "admin" → full access to admin screens.
- **ro** on group "admin" → read-only access to some configuration areas.

This enables delegated administration.


Why Groups Matter in Daily Operations
=====================================


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

- Who can take ownership
- Who may raise priority
- Who may add notes or update tickets
- Who can move or create tickets to another team
- Who can close or reopen tickets


Multi-Department Isolation
--------------------------

One Znuny instance can support completely separate units:

- IT
- HR
- Finance
- Legal
- Facility Management
- Customer Service

Each sees only their own queues, enforced by group permissions.
