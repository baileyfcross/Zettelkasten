2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Thread Group ID

Linux assigns every schedulable thread its own task identifier, while threads belonging to one user-visible process share a thread group ID. The group ID is the task ID of the thread-group leader and is what many user-space tools present as the process ID.

This distinction explains how Linux can schedule threads independently while preserving process-level operations such as group-directed signals. It also clarifies why a [[Linux Task Structure]] describes a task rather than mapping one-to-one with the everyday notion of a process.

# References

[[linuxkernelprogramming_secondedition.pdf]]
