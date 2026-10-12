2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]]

# SLES Cloud Image Deployment

A SLES cloud image is a prebuilt operating-system disk designed to be instantiated by a cloud platform rather than installed interactively from media. Instance creation supplies machine size, storage, networking, access credentials, and image selection, while initialization data adapts the generic image to its assigned role.

This changes the provisioning boundary, not the need for administration. Image provenance, subscription handling, persistent data placement, network reachability, and post-boot configuration still require verification. Cloud-init can automate first-boot settings, but its result should be inspected like any other configuration source.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
