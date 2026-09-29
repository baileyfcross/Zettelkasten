2026-09-28 21:33

Status: #baby

Tags: [[Scientific Workflow Provenance]]

# Workflow Upgrade Path

A workflow upgrade path maps a workflow written for an older module or package version onto a newer interface. The mapping may be automatic when the change is simple or explicitly supplied by a developer when parameters and behavior have changed.

Preserving the original workflow and recording the upgrade is safer than silently replacing it. The old specification remains part of [[Workflow Evolution Provenance]], while the transformation documents how execution became possible in the new environment. This makes compatibility work inspectable and prevents a modernized run from being mistaken for an unchanged reproduction.

# References

[[implementingreproducableresearch.pdf]]
