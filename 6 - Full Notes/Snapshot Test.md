2026-09-30 00:32

Status: #baby

Tags: [[React Testing Practice]]

# Snapshot Test

A snapshot test stores one reviewed representation of rendered output and compares later output with it. Any structural change fails the comparison, making unexpected interface changes visible without asserting every element separately.

The first saved snapshot must be inspected for correctness, and a failed snapshot should be updated only when the change is intentional. A readable JSX-like representation is easier to review than one long HTML string; blindly accepting snapshots can turn the test into an approval mechanism for defects.

# References

[[learningreact1.pdf]]
