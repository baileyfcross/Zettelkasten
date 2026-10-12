2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Command Pattern

The command pattern represents a request as an object with an operation to execute. The inventory console models help, add, get, update, and quit as command objects sharing an execution contract; a factory chooses one from user input. This separates the parsing and dispatch of a request from the behavior that carries it out and makes individual commands easier to test.

A command object packages the receiver, requested operation, and required parameters so an invoker does not call the receiver directly. Treating the request as an object creates room for queuing, logging, composition, or delayed execution.

The design-pattern and DDD chapters both represent an operation as a command object and route it to a handler. This decouples the requester from execution logic and gives validation, logging, or dispatch a named message boundary.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
