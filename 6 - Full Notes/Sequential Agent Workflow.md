2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]]

# Sequential Agent Workflow

A sequential agent workflow passes the output of one role to the next in a defined order. It is appropriate when later work depends on an earlier artifact, such as a researcher producing evidence before a writer drafts and an editor reviews.

The handoff should preserve provenance and conform to an [[Agent Task Contract]] rather than relying on conversational implication. Sequential execution is easier to reason about than parallel work but accumulates latency and can propagate an early mistake downstream.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
