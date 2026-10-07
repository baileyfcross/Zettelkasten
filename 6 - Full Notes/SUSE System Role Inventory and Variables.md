2026-10-07 18:14

Status: #baby

Tags: [[SLES Administration Interfaces and Automation]]

# SUSE System Role Inventory and Variables

An Ansible inventory identifies the hosts and groups targeted by a play, while role variables describe the configuration each [[SUSE Ansible System Roles]] invocation should enforce. Group and host variables can share defaults or express exceptions without copying the role implementation.

Reliable automation keeps targeting and desired state explicit. A correct role applied to the wrong inventory group is still a damaging change, and an unexamined variable default may be unsuitable for production. Dry runs and diffs can reveal planned changes, but modules that cannot model every side effect still require staged validation.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
