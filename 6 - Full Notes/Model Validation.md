2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]]

# Model Validation

Model validation checks a bound request model against its declared constraints before the application treats it as valid input. An API action can reject invalid state with a client-error response instead of passing malformed values into persistence behavior.

Client validation improves feedback but cannot replace this server boundary. A caller can bypass the React interface and send any request allowed by the network.

# References

[[aspnetcore3andreact.pdf]]
