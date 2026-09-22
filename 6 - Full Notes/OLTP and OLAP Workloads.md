2026-09-15 09:10

Status: #baby

Tags: [[Data Science Infrastructure and Integration]] [[CQRS and Ledger Data Architecture]]

# OLTP and OLAP Workloads

Online transaction processing records operational events such as orders, payments, and customer contacts. Online analytical processing asks historical, aggregated questions across those events, often by region, product, or time period. The two workloads therefore organize data for different purposes.

A warehouse and data cube can make predefined summaries quick to slice, pivot, and report. Those fixed dimensions also limit the questions the cube can express. OLAP supports exploration and reporting, but it does not itself learn a predictive model or discover every pattern the organization may need.

The design-patterns source contrasts an operational database optimized for frequent insert, update, and delete statements with an analytical store optimized for selections and aggregation. Indexes and other table structures accelerate reads but add maintenance cost to each write. A separate read store can protect transactional throughput while serving reporting needs, though it must be kept in sync with its source.

# References

[[datascience_mit.epub]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
