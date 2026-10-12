2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# setgid Directory Inheritance

The setgid bit on a directory causes newly created entries to inherit the directory's group rather than relying only on each creator's primary group. This helps a shared project tree retain one group ownership model when collaborators have different primary groups.

Inheritance does not by itself grant group write permission or override the creator's umask. A collaborative directory therefore combines suitable ownership, the setgid bit, and modes or access controls that let the intended group work. [[Sticky Bit Directory Protection]] solves a different problem: limiting deletion in a broadly writable directory.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
