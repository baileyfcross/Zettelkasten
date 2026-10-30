2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Internet Address Resolver SPI

The Java Internet-address resolver SPI lets a service provider supply host-to-address and address-to-host resolution for `InetAddress`. A provider can implement a custom DNS source, test mapping, or naming system while the platform resolver remains the fallback when no provider is available.

Java locates providers through the service-loading mechanism on the class path or module path. The separation places resolution policy behind a standard interface instead of requiring an application to replace or intercept the native operating-system resolver internally.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
