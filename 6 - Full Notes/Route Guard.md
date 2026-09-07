2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# Route Guard

An Angular route guard decides whether a client-side route may be activated, loaded, or left under the current application state. An authentication guard can redirect an unauthenticated user to a login flow before showing a protected component.

Route guards improve navigation behavior but run in the client and can be bypassed. The server endpoint reached by the guarded component must enforce its own [[Authorization]].

# References

[[aspnetcore3andangular9_3ed.pdf]]
