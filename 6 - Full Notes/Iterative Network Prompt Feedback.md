2026-09-27 18:30

Status: #baby

Tags: [[Network AI Model and Prompt Engineering]]

# Iterative Network Prompt Feedback

Iterative prompt feedback treats the first model response as a draft. An engineer reviews it, identifies concrete defects or missing requirements, and supplies those observations in a subsequent turn. The retained conversation lets the model revise the same artifact rather than beginning from an unrelated prompt.

Feedback is most useful when it names evidence: an ACL omitted return traffic, a command targets the wrong operating system, or a required validation step is absent. The final artifact still needs independent review because repeated agreement inside one conversation can reinforce an earlier mistake. For complex work, feedback pairs well with [[Layered Network Prompt Construction]].

# References

[[ainetworkingcookbook.pdf]]
