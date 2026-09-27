2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Task Exception Aggregation

When several tasks fail, .NET can preserve their failures in an `AggregateException` rather than discarding every exception after the first. Observing the completed task is part of the contract because the error belongs to the asynchronous operation, not necessarily to the call that started it.

Handlers should distinguish expected cancellation from faults and inspect every relevant inner exception when multiple branches ran. Await-based code often presents one exception directly, but the underlying operation set may still contain several failures that require logging or policy decisions.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
