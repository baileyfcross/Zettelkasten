2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Exception Handling]]

# C# Try-Catch Statement

A C# `try` block surrounds operations that may throw, and an associated `catch` block handles a compatible exception. When no exception occurs, execution leaves the `try` normally; when one occurs, control searches the available handlers rather than continuing through the remaining statements in the block.

The handler can inspect the exception, report useful context, choose a safe recovery, or rethrow it. A catch should represent a deliberate policy rather than a blanket promise that every failure is recoverable.

When several handlers are present, they must proceed from more specific exception types toward more general ones. Placing a broad handler first would make a later specialized recovery unreachable and erase information the caller could have used.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
