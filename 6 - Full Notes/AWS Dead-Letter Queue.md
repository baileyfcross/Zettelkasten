2026-09-27 20:01

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# AWS Dead-Letter Queue

An AWS dead-letter queue receives messages or events that a consumer could not process successfully after the configured number of attempts. Separating repeated failures prevents one poison message from blocking normal work and preserves evidence for diagnosis or replay. A DLQ is useful only with alarms, ownership, retention, and a redrive procedure; otherwise it silently converts visible processing failures into an accumulating backlog.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

