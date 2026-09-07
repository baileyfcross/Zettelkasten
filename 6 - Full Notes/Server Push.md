2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# Server Push

Server push is the delivery of a message from the server to a client without a new client-initiated request for that message. SignalR uses this pattern to notify connected React applications after relevant server events.

Push reduces the delay and repeated traffic of polling, but the message is still a notification within a fallible connection. The client must update state deliberately and recover its authoritative view when necessary.

# References

[[aspnetcore3andreact.pdf]]
