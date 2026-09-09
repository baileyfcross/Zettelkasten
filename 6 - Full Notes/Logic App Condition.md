2026-09-08 22:09

Status: #baby

Tags: [[Azure Logic Apps and Functions]]

# Logic App Condition

A Logic App condition evaluates a Boolean test and separates the workflow into yes and no branches. Each branch can contain its own actions, allowing later work to depend on data produced earlier in the run.

The campaign compares the current time with a spreadsheet value by calling an Azure Function, then uses the returned flag to decide whether a tweet should be sent and the source row removed. The condition turns an external calculation into visible workflow control.

# References

[[c8andnetcore30projectsusingazure.pdf]]
