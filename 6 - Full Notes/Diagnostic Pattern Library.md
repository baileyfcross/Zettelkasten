2026-10-11 21:02

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Diagnostic Pattern Library

A diagnostic pattern library encodes recurring relationships between operational symptoms and the evidence needed to test them. Examples include out-of-memory termination, sustained CPU saturation, disk exhaustion, network reachability failure, and crash loops, each associated with relevant logs, metrics, commands, and disconfirming signals.

The library provides structure before model reasoning begins. It helps an incident assistant request the right evidence and explain which pattern matched, while keeping the result a hypothesis until current observations confirm it. Patterns should be versioned and revised from postmortems rather than treated as permanent rules.

The legacy-systems source organizes such knowledge as a failure-list data model. Failure records are classified by scope, system, type, and concrete condition across networks, kernels, JVMs, clusters, APIs, message systems, legacy middleware, pipelines, and microservices. Connecting that catalog to current telemetry lets retrieval supply a known diagnostic pattern while the live [[Root Cause Analysis Data Model]] determines whether its evidence is present in this incident.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
