2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]]

# Agama Installer Workflow

Agama is the SLES 16 installer that organizes deployment into reviewable choices for hostname, registration, localization, networking, storage, software, and authentication. Rather than treating installation as one opaque action, it exposes the current proposal so an administrator can resolve incomplete or unsuitable settings before writing the system.

The workflow applies to physical and virtual installations, while cloud images normally arrive preinstalled and receive instance-specific configuration later. Choices such as [[SLES Installation Storage and Software Selection]] establish assumptions that continue into package management, boot recovery, and ongoing administration.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
