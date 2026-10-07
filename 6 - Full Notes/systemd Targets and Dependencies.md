2026-10-07 18:14

Status: #baby

Tags: [[SLES Service Logging and Remote Operations]]

# systemd Targets and Dependencies

A systemd target is a synchronization unit that groups other units into a meaningful system state, such as rescue or multi-user operation. Dependency directives express which units are wanted or required, while ordering directives state whether one unit must start before or after another.

Requirement and order solve different problems: depending on a service does not automatically specify every sequencing relationship, and ordering alone does not cause the other unit to be activated. Examining the dependency graph helps explain boot behavior more accurately than treating a target as a linear startup script.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
