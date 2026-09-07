2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]]

# Controller Action Method

A controller action method handles a routed HTTP operation. Its parameters receive bound request data, its body coordinates application work, and its return value communicates a response body and status to the client.

Action methods can be asynchronous when repository operations wait on external resources. Their signatures also document which request values are required and which response shapes callers can expect.

# References

[[aspnetcore3andreact.pdf]]
