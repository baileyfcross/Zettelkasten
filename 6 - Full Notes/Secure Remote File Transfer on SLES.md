2026-10-07 18:14

Status: #baby

Tags: [[SLES Service Logging and Remote Operations]]

# Secure Remote File Transfer on SLES

SLES can transfer files over the SSH trust and encryption boundary through tools such as `scp` and `sftp`, while `rsync` can use an SSH transport to synchronize changed data efficiently. Authentication, host verification, account permissions, and destination paths remain part of the transfer even when the command syntax is brief.

The tools express different workflows: SFTP provides an interactive file-transfer subsystem, SCP copies named paths, and rsync compares trees and preserves selected metadata. A transfer plan should state whether deletion, recursion, ownership, links, and partial files are intended rather than assuming every tool produces the same result.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
