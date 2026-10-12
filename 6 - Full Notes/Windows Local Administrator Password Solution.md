2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Windows Local Administrator Password Solution

Windows Local Administrator Password Solution manages a unique, regularly rotated local administrator password for each domain-joined computer. The current value and its expiration metadata are stored under controlled permissions in Active Directory, preventing one shared local password from becoming a reusable credential across the server fleet.

Group Policy defines the managed account, complexity, length, rotation, and backup directory. Directory permissions must restrict who can retrieve or reset the password, and access should be auditable because the stored secret grants powerful local control. LAPS limits lateral movement from a captured local credential but does not protect domain accounts or replace privileged-access discipline. Recovery procedures should let authorized operators obtain a machine's password without normalizing broad read access to every managed credential.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
