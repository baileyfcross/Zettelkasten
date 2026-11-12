2026-11-11 19:33

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Overlay Network

A Docker overlay network creates a virtual network that can connect containers running on multiple Docker hosts. It extends container communication beyond the single-host boundary of a [[Docker Bridge Network]] and is used with multi-host orchestration such as Docker Swarm.

The overlay sits above the hosts' existing networks so participating containers can communicate through one logical network without being configured as direct peers on the physical network.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
