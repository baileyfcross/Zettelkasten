2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]]

# Agent Task Contract

An agent task contract defines the task description, available inputs, permitted tools, expected output, completion criteria, and error behavior for an agent. It turns a vague delegation into an interface that another workflow component can inspect.

Typed or otherwise structured results improve handoffs between agents and make partial failure explicit. The contract should separate untrusted source data from instructions and avoid granting tools or context unrelated to the assigned task.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
