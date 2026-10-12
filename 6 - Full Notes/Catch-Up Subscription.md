2026-09-22 20:53

Status: #baby

Tags: [[Event Sourcing and Projections]]

# Catch-Up Subscription

A catch-up subscription reads an event stream from a stored [[Projection Checkpoint]], processes historical events until it reaches the stream's end, and then continues with new events in real time. Starting from the beginning allows a new [[Projection]] to build a read model for a system that already has a long history. Resetting the checkpoint and deleting the read model triggers a rebuild, so the event history remains the authoritative input.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
