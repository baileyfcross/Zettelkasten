2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# Session Authentication

Session authentication keeps an authenticated user's state associated with a server-managed session and sends a session identifier with later requests. The server uses that identifier to recover the corresponding login state.

This is stateful because the server must retain session information. [[Token-Based Authentication]] instead gives the client a signed token that carries information used to validate subsequent requests.

# References

[[aspnetcore3andangular9_3ed.pdf]]
