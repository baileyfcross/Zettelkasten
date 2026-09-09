2026-09-08 22:09

Status: #baby

Tags: [[WebAssembly and Blazor Applications]]

# WebAssembly Security Sandbox

WebAssembly runs under the browser's security context rather than as an unrestricted executable installed directly on the user's computer. The source describes its security boundary as comparable to JavaScript because both rely on the browser sandbox.

The sandbox reduces direct machine access but does not make application logic or data automatically safe. Network requests, exposed secrets, untrusted inputs, and browser vulnerabilities still belong to the web application's security model.

# References

[[c8andnetcore30projectsusingazure.pdf]]
