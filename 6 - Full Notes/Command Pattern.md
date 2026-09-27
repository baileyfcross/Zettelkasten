2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Command Pattern

The command pattern represents a request as an object with an operation to execute. The inventory console models help, add, get, update, and quit as command objects sharing an execution contract; a factory chooses one from user input. This separates the parsing and dispatch of a request from the behavior that carries it out and makes individual commands easier to test.

A command object packages the receiver, requested operation, and required parameters so an invoker does not call the receiver directly. Treating the request as an object creates room for queuing, logging, composition, or delayed execution.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
