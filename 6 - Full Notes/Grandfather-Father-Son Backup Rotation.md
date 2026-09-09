2026-09-09 00:00

Status: #baby

Tags: [[Backup and Recovery Strategies]]

# Grandfather-Father-Son Backup Rotation

Grandfather-father-son backup rotation keeps backup sets at three time scales: monthly, weekly, and daily. The tiers provide recent recovery points while retaining less frequent snapshots over longer periods.

In a cloud version, different providers can hold the monthly, weekly, and daily sets. This separates schedules and locations so a problem at one provider does not necessarily remove every tier of recovery history.

# References

[[cloudcomputing_mit.epub]]
