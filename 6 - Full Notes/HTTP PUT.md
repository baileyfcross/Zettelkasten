2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]]

# HTTP PUT

HTTP PUT sends a representation intended to replace or update the resource identified by the request URI. An API action combines the route identifier with a validated request model before invoking its repository operation.

The endpoint must define what happens when the resource does not exist and which fields participate in replacement. That contract keeps client expectations separate from incidental database behavior.

# References

[[aspnetcore3andreact.pdf]]
