2026-09-27 18:30

Status: #baby

Tags: [[Network AI Model and Prompt Engineering]]

# Task-Specific Network Prompt

A task-specific network prompt replaces a vague request such as “help with BGP” with the target platform, software family, current topology, desired state, constraints, and required deliverable. These details reduce the number of unstated choices the model must invent.

Good direction also marks unknown facts instead of encouraging the model to fill them in. A request for IOS-XR syntax should not silently become IOS syntax, and a change plan should identify missing addresses or maintenance requirements. [[Network Engineering System Message]] supplies stable behavior; the task prompt supplies the immediate engineering context.

# References

[[ainetworkingcookbook.pdf]]
