2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Output Token Budget

An output token budget limits how many tokens a model may generate for one response. The source uses this control to request short summaries and demonstrates that a budget can terminate a response in the middle of a sentence when it is too small.

The budget is distinct from the total [[Model Context Window Governance|context window]], which must accommodate both input and output. A concise instruction does not guarantee concise generation, so an explicit limit provides a predictable ceiling for latency and usage. The client should inspect the [[Chat Completion Finish Reason]] to distinguish a completed answer from one cut off by the limit and should not display truncated text as though it were complete.

# References

[[chatgptforjava.epub]]
