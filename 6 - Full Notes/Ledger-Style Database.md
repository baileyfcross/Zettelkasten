2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# Ledger-Style Database

A ledger-style database records each transaction as a separate row and derives a current balance by aggregating those rows. Inventory additions, sales, and credits remain visible as a history instead of overwriting one quantity field. This gives an audit trail of what changed and can record who made the change, but a growing ledger may need a maintained summary for fast current-state queries.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

