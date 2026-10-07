2026-10-07 18:14

Status: #baby

Tags: [[SLES Administration Interfaces and Automation]]

# Cockpit Service and Account Management

Cockpit presents systemd unit state and local account information through web controls for tasks such as starting or enabling services and creating or modifying users. The actions still follow systemd and account rules: runtime service state differs from enablement, and an account change affects numeric identity, groups, login, and files.

Cockpit sessions can elevate privileges for authorized operations, so the logged-in identity and current administrative mode should be visible during review. A convenient control does not remove the need to inspect journal evidence or understand the downstream access granted by a group membership.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
