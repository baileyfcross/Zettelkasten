2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Deployment and Administration]]

# Windows Server In-Place Upgrade

A Windows Server in-place upgrade replaces the operating-system version while attempting to preserve installed roles, applications, data, and configuration. Windows Server 2025 supports a wider upgrade span than earlier releases, including supported multi-version paths, but compatibility still depends on hardware, installation option, applications, and role-specific requirements.

An upgrade is a change to an operating system that may host irreplaceable state, so a successful setup wizard is not the only acceptance criterion. Administrators should verify support, patch the source system, capture tested backups, check free space and drivers, document rollback, and validate every hosted service afterward. Rebuilding from a standardized image remains preferable when it offers a cleaner and safer migration path; in-place upgrade is useful when preserving the existing system is the deliberate constraint.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
