2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java First-Successful Structured Join

A first-successful structured join starts several competing subtasks and returns the first successful result. Once one subtask supplies that result, the task scope interrupts the remaining attempts because their answers are no longer required.

The policy suits redundant searches or connection attempts where the fastest acceptable provider wins. A failed attempt does not end the whole search while another attempt can still succeed; callers should inspect subtask state before retrieving a result from any nonwinning task.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
