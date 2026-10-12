2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]]

# SLES Virtual Machine Installation

A SLES virtual-machine installation presents an ISO image to virtual firmware and supplies virtual CPU, memory, storage, and network devices before the guest installer starts. The guest experiences these as machine resources, so an undersized disk, disconnected virtual adapter, or unsuitable firmware selection becomes an operating-system installation constraint.

Virtualization makes reconfiguration easier but does not remove deployment decisions. [[Agama Installer Workflow]] still establishes identity, registration, storage, software, and authentication, and the administrator must distinguish a guest configuration problem from a hypervisor-side device or network problem.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
