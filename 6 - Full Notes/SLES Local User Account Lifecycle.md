2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# SLES Local User Account Lifecycle

A local SLES user account binds a login name to a numeric user ID, primary group, home directory, shell, and password-related state. Creation establishes those attributes, modification changes them deliberately, locking prevents password login without erasing the identity, and deletion requires a separate decision about the account's files.

The numeric identity matters more to filesystem ownership than the display name. Reusing an old UID can therefore give a new account unintended access to abandoned files. Account retirement should locate owned data, scheduled work, keys, and delegated privileges before removing the record.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
