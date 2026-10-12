2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux Action

A Redux action is an object that describes an event that may change application state. Its type identifies what happened, and additional fields carry the data the reducer needs to interpret that event.

Actions describe requested transitions without performing them. Dispatching the action sends it through the store to the reducer, which decides the resulting state.

The source treats actions as both instructions and receipts: their type names the event and their [[Redux Action Payload|payload]] records the data used for it. Logging the ordered actions therefore provides a history of how the current state was reached.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
