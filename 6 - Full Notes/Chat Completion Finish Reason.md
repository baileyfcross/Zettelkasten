2026-10-18 16:07

Status: #baby

Tags: [[Java OpenAI API Integration]]

# Chat Completion Finish Reason

A chat completion finish reason states why a generated choice ended. In the source's 2024 response schema, normal completion or a configured stop sequence is distinct from reaching an output or model limit, requesting a tool call, being terminated by a content filter, or still being incomplete.

The application should inspect this field before treating the generated content as a finished answer. A length-limited response may end mid-sentence and require a different user experience from a normal stop, while a tool call needs structured handling rather than display as prose. The finish reason therefore turns termination into explicit control flow and helps [[Output Token Budget|an output budget]] remain observable.

# References

[[chatgptforjava.epub]]
