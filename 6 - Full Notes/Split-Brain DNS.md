2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# Split-Brain DNS

Split-brain DNS returns different answers for the same namespace according to where the query originates. An internal client may receive a private address for a service, while an external client receives the public endpoint. Windows DNS policies and zone scopes can implement this behavior without maintaining completely unrelated naming conventions.

The design lets users keep one service name across locations and prevents internal traffic from taking an unnecessary public path. It also creates two views whose records must remain intentionally aligned. Administrators should document which names differ, ensure internal clients use the internal resolver, and test both perspectives. An accidental mismatch can make a service appear healthy from one network and broken from another even though both are querying the same name.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
