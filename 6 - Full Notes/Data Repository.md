2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Data Repository

A data repository is a concrete service that implements a set of persistence operations for an application. Its methods translate meaningful requests, such as retrieving a question or saving an answer, into database commands.

The repository keeps data-access details out of controllers and can be registered through dependency injection. Its method boundaries also expose where asynchronous execution and transaction decisions belong.

# References

[[aspnetcore3andreact.pdf]]
