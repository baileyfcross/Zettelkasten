2026-10-19 01:48

Status: #baby

Tags: [[Go Standard Library and Service Development]]

# Go SQL Row Scanning

Go SQL row scanning copies columns from a query result into caller-provided destinations. `Row` handles an expected single result, while `Rows` advances through multiple records with `Next` and scans each current record.

A multirow query should close its rows and inspect `Rows.Err` after iteration because some failures surface during traversal rather than at query creation. Destination order, type conversion, and null handling must match the selected columns.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
