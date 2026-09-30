2026-09-30 00:32

Status: #baby

Tags: [[Redux State Management]]

# Presentational Component

A presentational component renders interface elements from props and reports interaction through callback props without directly depending on a Redux store. Its concern is how data appears and how UI events are exposed, not where the data is stored.

A [[Connected Component|connected or container component]] can map shared state and dispatch operations into that ordinary prop contract. The separation makes the presentation reusable with another data source and lets its rendering and events be tested without assembling the entire state architecture.

# References

[[learningreact1.pdf]]
