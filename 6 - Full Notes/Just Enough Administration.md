2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Just Enough Administration

Just Enough Administration constrains PowerShell remoting so an operator receives only the commands, parameters, providers, and functions required for a defined task. A JEA endpoint maps connecting users or groups to a role capability and can run the permitted action through a temporary privileged identity rather than granting the human a standing administrator account.

This applies least privilege at the command surface. A help-desk role might restart a service or inspect a process without receiving arbitrary code execution on the server. Endpoint configuration, role files, transcript logging, and testing are security-sensitive because an apparently harmless command can expose an escape path through unrestricted parameters or scripts. JEA reduces privilege only when the allowed operations and the files that define them are themselves tightly controlled.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
