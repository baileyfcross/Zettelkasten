2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]]

# Tool-Augmented Generation

Tool-augmented generation allows a model to request structured functions that retrieve live information or perform bounded actions. The application, not the model, owns tool execution: it validates arguments, authorizes the caller, invokes the target, records the result, and decides what may return to the model. This boundary turns function calling into an integration and security design problem, especially when a tool can modify data or trigger external effects.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
