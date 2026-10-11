2026-10-11 12:45

Status: #baby

Tags: [[Search Log and Web Text Mining]]

# Search Log Sessionization

Search log sessionization groups consecutive queries into an estimated episode of activity, commonly by starting a new session after a chosen inactivity gap. It converts isolated log rows into units from which behavior-level features can be calculated.

The boundary is heuristic rather than observed ground truth. Shared addresses, changing devices, unattended tabs, and long pauses can merge different people or split one task, so conclusions should be tested against alternative thresholds when possible.

# References

[[textminingandvisualization.pdf]]
