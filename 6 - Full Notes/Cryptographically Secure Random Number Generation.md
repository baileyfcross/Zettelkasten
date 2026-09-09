2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# Cryptographically Secure Random Number Generation

Security-sensitive values require randomness that an attacker cannot feasibly predict. .NET cryptographic random-number generators draw from operating-system facilities intended for keys, salts, nonces, and other secrets.

The ordinary `Random` class is useful for simulation and general variation but is not designed to resist prediction. Choosing the cryptographic generator is therefore a security boundary, not merely a matter of producing a wider range of numbers.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
