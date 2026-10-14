2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Hybrid Identity

Hybrid identity represents the same workforce identity across an on-premises Active Directory and Microsoft Entra ID. A synchronization service copies selected users, groups, and attributes to the cloud so applications can use modern tokens while existing systems continue to rely on the on-premises directory.

Synchronization and authentication are separate choices. Password hash synchronization validates a derived password hash in the cloud, pass-through authentication sends validation to an on-premises agent, and federation redirects sign-in to another identity provider. Each choice changes availability and operational dependencies. [[Microsoft Entra Cloud Sync]] or Entra Connect can bridge the directories, but the authoritative source, attribute flow, deletion behavior, and eventual plan for reducing legacy dependencies must remain explicit.

# References

[[masteringmicrosoftentraid.pdf]]
