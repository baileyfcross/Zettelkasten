2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Factory Method Pattern

A factory method centralizes the decision about which concrete implementation to create and returns it through a shared type. The inventory application's command factory maps textual input such as add, get, update, or quit to a corresponding command object, so the command loop need not contain each constructor and its dependencies. A new command changes the creation boundary rather than every caller that executes commands.

A factory method selects and constructs one implementation of a shared product abstraction according to creation logic hidden from the client. The client receives the common product type rather than hard-coding a particular concrete class.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]
