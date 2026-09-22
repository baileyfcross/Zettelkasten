2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Chain of Responsibility Pattern

The chain of responsibility pattern sends a request through an ordered series of handlers. Each handler performs the part it can address and passes any remaining work to the next one, so the sender does not need to select a single concrete handler. In the book's car-service example, mechanics, wheel specialists, quality control, and detailers handle different service flags; changing their order changes the process without changing the request.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

