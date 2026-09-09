2026-09-08 22:09

Status: #baby

Tags: [[Azure Logic Apps and Functions]]

# Logic App For Each Loop

A Logic App for-each loop applies its contained steps to every item in a collection returned by an earlier action. The campaign uses iteration to examine each row read from its Excel table.

The loop gives each iteration access to the current row's dynamic values, which can be supplied to conditions and connected services. Its downstream effects must be safe for repeated execution because a workflow may encounter several eligible items in one run.

# References

[[c8andnetcore30projectsusingazure.pdf]]
