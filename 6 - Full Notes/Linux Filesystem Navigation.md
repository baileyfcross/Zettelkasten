2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]]

# Linux Filesystem Navigation

Linux presents files, devices, configuration, and mounted storage through one directory tree rooted at `/`. Absolute paths begin from that root, while relative paths are resolved from the current working directory. Commands such as `pwd`, `cd`, and `ls` establish where an operation will occur before it reads or changes data.

Navigation is an administrative safety mechanism as well as a convenience. Confirming a resolved path, distinguishing a file from a symbolic link, and recognizing mount points reduces accidental work in the wrong tree. [[Persistent Filesystem Mounts with fstab]] explains how additional filesystems become part of this namespace.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
