2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# Linux Primary and Supplementary Groups

A Linux account has one primary group recorded with the account and may join additional supplementary groups. New files normally inherit the creator's primary group unless directory inheritance or another policy changes it, while all active group memberships can contribute permissions during access checks.

Group-based access scales better than granting equivalent permissions separately to every user. Membership changes should still be treated as privilege changes: an administrative group, shared-data group, or device-access group can expose powerful capabilities even when the account itself is not root. [[setgid Directory Inheritance]] helps preserve a shared group on collaborative files.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
