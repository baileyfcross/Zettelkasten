2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Web Access

Remote Desktop Web Access presents the desktops and RemoteApp programs assigned to a user through a browser-based portal or feed. It gives the RDS deployment a discoverable catalog so clients do not need a separately distributed connection file for every published resource.

Web Access does not run the application session; it publishes connection information that leads the client to the appropriate RDS components. The site should use a trusted certificate whose name matches the address users receive, and external publication is commonly paired with [[Remote Desktop Gateway]]. Collections and user-group assignments determine what appears after sign-in. A clean portal therefore depends on consistent naming, certificates, broker configuration, and authorization rather than on the web role alone.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
