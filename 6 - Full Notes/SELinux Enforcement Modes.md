2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# SELinux Enforcement Modes

SELinux enforcing mode applies policy decisions and denies disallowed operations, while permissive mode records policy violations without blocking them. Disabled mode removes SELinux from normal policy enforcement and also prevents the system from maintaining the same active labeling behavior.

SLES 16 uses SELinux as its default mandatory access-control framework. Temporarily observing a denial in permissive mode can aid diagnosis, but leaving the system permissive is not a repair. The correct response is to identify the expected access, inspect [[SELinux Security Context]], and make the narrowest persistent policy or labeling correction.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
