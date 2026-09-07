2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# Web Host

A web host is the execution context of an ASP.NET Core web application. It coordinates application startup and supplies web-related hosting services rather than directly representing the network listener.

Host construction can select the [[Kestrel]] [[Web Server]], set the content root used to find configuration, enable IIS integration, identify the startup class, and then build and run the configured application.

# References

[[aspnetcore3andangular9_3ed.pdf]]
