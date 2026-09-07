2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# Real-Time API

A real-time API allows the server to deliver an event to a client without waiting for that client to poll another request. It is useful when the value of a screen changes because of activity elsewhere in the system.

The contract defines connection setup as well as message names and payloads. Clients must map each message into their own state and remain prepared for connection failure or interruption.

# References

[[aspnetcore3andreact.pdf]]
