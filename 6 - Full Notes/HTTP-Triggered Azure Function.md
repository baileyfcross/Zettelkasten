2026-09-08 22:09

Status: #baby

Tags: [[Azure Logic Apps and Functions]]

# HTTP-Triggered Azure Function

An HTTP-triggered Azure Function exposes a function through an HTTP request. Attributes identify the function name, accepted methods, route behavior, and authorization level, while the method receives the request and returns an HTTP action result.

The date-comparison function reads a JSON request body, performs its comparison, and returns a JSON-shaped flag. The HTTP boundary lets a Logic App call the function like another connected action without embedding the calculation in the workflow definition.

In the source, an HTTP trigger exposes focused C# computation through a managed endpoint, while other function triggers allow the same serverless model to react to queues, schedules, and service events without an always-running custom host.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[c8andnetcore30projectsusingazure.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
