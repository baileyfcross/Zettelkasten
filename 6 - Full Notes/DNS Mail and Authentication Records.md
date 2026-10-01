2026-09-30 23:37

Status: #baby

Tags: [[Windows DNS and DHCP Services]]

# DNS Mail and Authentication Records

DNS publishes more than host addresses. MX records identify the mail exchangers responsible for receiving a domain's messages and use preference values to order alternatives. TXT records carry arbitrary verification data and commonly publish mail-sender policy. SPF information identifies expected sending systems, while DKIM publishes the public material used to validate a signature added by the sending mail system.

These records form part of a mail trust and routing design, but no single record proves a message is safe. Names, priorities, quoting, and provider-supplied values must be copied accurately, and old entries should be removed when services change. Because public resolvers cache answers, administrators should plan DNS propagation alongside the mail-system change rather than expecting an edit to become universal immediately.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
