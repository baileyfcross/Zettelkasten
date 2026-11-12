2026-09-21 22:12

Status: #baby

Tags: [[Object-Oriented Design Patterns]]

# Observer Pattern

The observer pattern lets a subject notify registered observers when its state changes, without knowing the observers' concrete types. The book's C# subject raises an event after inventory quantity changes, and several observer objects subscribe through matching delegates. The subject remains loosely coupled to its consumers; subscription and unsubscription define who receives each update.

Observer reverses repeated polling by letting the subject retain a set of interested observers and notify them when relevant state changes. C# events and delegates provide language mechanisms for implementing this publisher-subscriber relationship.

The current source frames the dependency as one-to-many: observers register and unregister with a subject, and a state change causes the registered set to be notified and updated. The subject depends on the observer abstraction rather than the concrete purposes of its subscribers.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
