2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# Linux File Permission Classes

Traditional Linux file permissions assign read, write, and execute bits to three classes: the owning user, the owning group, and everyone else. The kernel selects the applicable class from the process credentials and file ownership, then interprets the bits according to whether the object is a regular file or a directory.

Directory read permits listing names, write permits changing entries, and execute permits traversing and resolving names. A successful discretionary check does not guarantee access when [[SELinux Security Context]] policy also applies, and a failed check should be diagnosed before broadening permissions for all users.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
