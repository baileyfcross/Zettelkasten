2026-10-18 23:53

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# Chat Memory Sliding Window

A chat memory sliding window retains only a bounded set of recent messages for use in later model calls. It prevents an indefinitely growing conversation from consuming the entire context window and gives the application a predictable upper bound on stored turns.

Simple recency can discard an early fact that remains important. The window size should therefore be evaluated against the task, and durable facts may need separate state or a controlled summary rather than being assumed to survive message eviction.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
