2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Microsoft Entra Role

A Microsoft Entra role is a collection of directory permissions that can be assigned to a user, role-assignable group, or service principal. Built-in roles cover common administrative duties, while custom roles can collect a narrower set of supported permissions.

An assignment combines the role definition, the security principal receiving it, and a scope such as the tenant, an [[Microsoft Entra Administrative Unit|administrative unit]], or a particular app registration. This separation makes least privilege a design question: choose only the permissions needed, bind them at the smallest workable scope, and use [[Microsoft Entra Privileged Identity Management]] when powerful access should be eligible and time-bound rather than continuously active.

# References

[[masteringmicrosoftentraid.pdf]]
