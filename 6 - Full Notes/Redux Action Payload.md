2026-09-30 00:32

Status: #baby

Tags: [[Redux State Management]]

# Redux Action Payload

A Redux action payload is the data an action carries in addition to its type so a reducer can calculate the requested transition. A rate action needs both the record identifier and new rating; an add action can carry every field needed to construct the new record.

The payload records the facts of the event rather than performing the change itself. Keeping those facts in the [[Redux Action|action]] makes the transition inspectable and allows several reducers to interpret the same event for different branches of the state tree.

# References

[[learningreact1.pdf]]
