2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# In-Process Hosting

In-process hosting runs an ASP.NET Core application inside the IIS worker process. IIS handles the public server role while the application executes within the same process instead of forwarding requests to a separate Kestrel process.

The arrangement is the default Windows hosting model described for current ASP.NET Core versions in the source. It contrasts with [[Out-of-Process Hosting]], which separates the reverse proxy and application server processes.

# References

[[aspnetcore3andangular9_3ed.pdf]]
