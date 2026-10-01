2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DNS CNAME Record

A DNS CNAME record makes one DNS name an alias of another canonical name. Users can connect to a role-oriented name such as `files.example` while the alias points to the current server hostname. Moving the service then requires changing the alias target rather than retraining users or reconfiguring every client.

The alias resolves through the canonical name, so that target must itself resolve correctly. CNAMEs are most useful when they express a stable service identity and avoid exposing a replaceable machine name. They should not be confused with multiple A records or load balancing: an alias redirects the lookup to another name but does not by itself test health, distribute sessions, or preserve a service when the target is unavailable.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
