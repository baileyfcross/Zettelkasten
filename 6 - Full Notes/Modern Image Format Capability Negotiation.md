2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# Modern Image Format Capability Negotiation

A server must not send a specialized image representation merely because it is smaller. It first needs evidence that the client can decode the required format variant, then must provide a broadly supported fallback.

HTTP Accept information, responsive `picture` sources, client hints, and sometimes client identification can participate in selection. The resulting response must also be cached under the correct variation dimensions; otherwise one client’s representation may be served to an incompatible client. See [[Vary Header for Image Variants]] and [[Responsive Image Format Fallback]].

# References

[[highperformanceimages.pdf]]
