2026-09-06 20:41

Status: #baby

Tags: [[Progressive Web Application Capabilities]]

# Network Connectivity Detection

Network connectivity detection estimates whether a browser currently has access to a network. Browser online and offline events, the navigator state, or a dedicated Angular service can notify the application when that estimate changes.

An online flag does not prove that a particular API is reachable, and cached responses can make a request appear successful without contacting the network. Applications should combine connectivity signals with real request outcomes.

# References

[[aspnetcore3andangular9_3ed.pdf]]
