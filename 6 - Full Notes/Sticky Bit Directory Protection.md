2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# Sticky Bit Directory Protection

The sticky bit on a directory restricts deletion and renaming so a writable shared directory does not let every participant remove every other participant's entries. The file owner, directory owner, and privileged users retain the permitted control.

This is why a temporary directory can be writable by many users without becoming an unrestricted deletion zone. The sticky bit does not make file contents private and does not replace appropriate read and write modes; it narrows directory-entry operations within an otherwise shared namespace.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
