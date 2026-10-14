2026-10-14 00:45

Status: #baby

Tags: [[Active Directory and Group Policy Administration]]

# Active Directory Schema Change Management

The Active Directory schema defines the object classes and attributes that the directory can store. Extending it can support a new application or relationship, but a schema modification affects the forest-wide data model and is not an ordinary reversible configuration change. Competing definitions, incompatible dependencies, or unnecessary attributes can therefore disrupt every service that depends on the directory.

Disciplined schema change management starts by documenting the business requirement, dependencies, and compatibility impact. A proposed extension should be compared with the current schema, tested in an isolated environment, backed by a complete recovery plan, and applied through the [[Flexible Single Master Operation Roles|schema master]] under restricted authorization. Version history, approvals, and auditing make the change traceable; continued review keeps obsolete or conflicting definitions from accumulating.

# References

[[windowsserver2025administrationfundamentals_fourthedition.pdf]]
