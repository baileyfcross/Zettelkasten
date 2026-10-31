2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Framework-Independent Application Core

A framework-independent application core contains the entities and business services whose meaning should survive changes in delivery or infrastructure. It accepts and produces application concepts through ports rather than importing the details of a web framework, database driver, or broker into its rules.

The book demonstrates the boundary by reusing the same product entity and service while REST, GraphQL, PostgreSQL, MongoDB, and messaging adapters change around them. Reuse is evidence that external context has not leaked into the core.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

