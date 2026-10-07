2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# Symbolic and Octal File Modes

Symbolic file modes express a change in terms of user, group, other, and selected permission operations, while octal modes encode each permission class as the sum of read, write, and execute bit values. Both forms modify the same underlying mode bits; they differ in how the intended result is communicated.

Symbolic changes are useful for adding or removing one capability without restating every bit. Octal notation is concise when the complete final mode is known. Before applying either recursively, an administrator should distinguish files from directories because execute permission has different practical meaning on each.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
