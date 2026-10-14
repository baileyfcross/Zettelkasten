2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Application Install Mode

Remote Desktop application install mode prepares a Session Host to install software for many users rather than only for the administrator performing setup. It records installation-time changes so user-specific registry and configuration behavior can be supplied appropriately when different users later launch the application. Server Manager or `change user /install` can place the server into this mode, followed by `change user /execute` for normal use.

The procedure matters most for traditional installers that assume one interactive profile. Modern packages may handle multi-user installation correctly, but testing remains necessary. Administrators should drain sessions, install consistently on every host in the collection, return to execute mode, and validate with a non-administrative user. An application that runs once for the installer is not yet proven safe for concurrent sessions or roaming profiles.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
