2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# Isomorphic Fetch

Isomorphic fetch is a fetch-compatible request implementation that can be used from both browser and Node.js environments. It replaces a browser-only request object or a Node-only HTTP call with one request interface available to shared application code.

The source combines it with [[Redux Thunk]]: a thunk sends a request, parses the JSON response, and dispatches the returned action. The universal request adapter reduces platform branching, while the thunk still owns latency, failure handling, and the timing of local dispatch.

# References

[[learningreact1.pdf]]
