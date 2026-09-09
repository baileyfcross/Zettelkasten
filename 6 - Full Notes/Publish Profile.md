2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]] [[Cloud Application Deployment]]

# Publish Profile

A publish profile stores a repeatable set of application publication settings for a destination. Profiles can target a folder, FTP location, or configured virtual machine and select build and deployment options.

Publishing produces the server application and compiled Angular files that the target host will serve. A profile automates the packaging step but does not replace target configuration such as IIS bindings, Nginx rules, or environment values.

Visual Studio's publishing workflow can create or import a profile for Azure App Service, IIS, FTP, Web Deploy, a package, or a folder target. The saved profile makes the selected build and destination settings repeatable while leaving credentials and production configuration as separate concerns.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
