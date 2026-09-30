2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Makefile

An out-of-tree kernel module Makefile delegates compilation to the [[Kbuild]] system of the target kernel. The module declares its object or composite objects, and the external invocation supplies the module directory while using the kernel tree's compiler flags, generated headers, and symbol information.

A stronger template can add install, clean, packaging, style checking, and static-analysis targets. Building against the exact intended kernel tree matters because a superficially successful native compile does not establish module ABI compatibility.

# References

[[linuxkernelprogramming_secondedition.pdf]]
