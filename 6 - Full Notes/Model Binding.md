2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]]

# Model Binding

Model binding constructs action parameters from HTTP request data. ASP.NET Core reads values from sources such as route segments, query strings, and request bodies and converts them into the declared .NET types.

Using the framework's binding pipeline keeps parsing and allocation behavior centralized. Explicit binding sources can make an endpoint contract clearer when the same value could plausibly come from more than one place.

# References

[[aspnetcore3andreact.pdf]]
