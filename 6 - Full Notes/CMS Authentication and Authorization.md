2026-09-08 21:16

Status: #baby

Tags: [[ASP.NET Core Content Management Systems]]

# CMS Authentication and Authorization

A CMS authenticates editors before granting access to management functions and authorizes what each identity may view or change. Publishing, administration, media management, and ordinary editing can require different permissions.

Editorial access should be separated from public content delivery and follow least privilege. The surrounding application's identity and authorization mechanisms remain responsible for enforcing these boundaries consistently across pages and APIs.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
