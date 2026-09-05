2026-09-05 16:28

Status: #baby

Tags: [[Conversational Assistant Design]]

# Asynchronous Assistant

An asynchronous assistant can continue a task after the immediate conversational turn and return when a result or event becomes available. The user does not have to hold an open synchronous exchange while external work completes.

The [[Dialog Manager]] must preserve task state, associate a late result with the correct request, and choose an appropriate time and channel for notification. This behavior often overlaps with [[Proactive Assistant|proactive interaction]].

# References

[[aiassistants.epub]]
