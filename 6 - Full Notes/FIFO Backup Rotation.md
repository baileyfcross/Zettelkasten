2026-09-09 00:00

Status: #baby

Tags: [[Backup and Recovery Strategies]]

# FIFO Backup Rotation

A first-in, first-out backup rotation reuses or expires the oldest backup slot when a new one is created. A seven-day full-backup cycle, for example, replaces the first day's set on the eighth day and continues in order.

The same idea can alternate cloud providers rather than physical tapes. Under a differential scheme, one provider can hold a week's full baseline and differentials before the next week's sequence begins with another provider.

# References

[[cloudcomputing_mit.epub]]
