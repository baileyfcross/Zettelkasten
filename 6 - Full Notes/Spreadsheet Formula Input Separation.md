2026-09-28 23:03

Status: #baby

Tags: [[Game Design Spreadsheets]]

# Spreadsheet Formula Input Separation

Spreadsheet formula input separation stores each tunable value in a labeled input cell and makes calculations refer to that cell instead of repeating a literal number. Even a simple constant such as gravity or a strength multiplier should have one authoritative location when it affects many formulas.

This turns a balance change into one controlled edit whose effects propagate automatically. Intermediate calculations should likewise be broken into labeled cells rather than compressed into a single opaque formula. The extra setup makes repeated iteration faster, reveals which step failed, and prevents copies of the same value from drifting apart.

# References

[[introductiontogamesystemdesign.pdf]]
