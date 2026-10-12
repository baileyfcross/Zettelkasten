2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# Materialized View

A materialized view stores the result of a query so readers need not recompute it from all source rows on every request. The ledger example can keep a purchaser's current amount as an aggregate of many transaction entries. The view must be refreshed when source data changes or on a defined schedule; faster reads therefore introduce a maintenance and potential-staleness obligation.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
