2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Network Copilot Knowledge Files

Network copilot knowledge files provide bounded local facts that a general model does not possess. Separate JSON files can describe device inventories, network context, known response examples, and topology relationships in forms that ordinary code can inspect before building a prompt.

Separation makes each source replaceable and reviewable, but filenames do not establish truth. Every file needs a defined owner, schema, update time, and validation path. The copilot should load only the subset relevant to the active device and intent so context remains focused.

# References

[[ainetworkingcookbook.pdf]]
