2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# Append-Only Transaction Ledger

An append-only transaction ledger expresses corrections as new entries rather than editing or deleting old ones. If an order or amount was recorded incorrectly, a compensating credit or reversal preserves the original entry and explains the adjustment. This protects historical traceability, but consumers must interpret the complete sequence or an up-to-date projection to obtain the effective current value.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

