2026-10-07 18:14

Status: #baby

Tags: [[SLES Networking Firewall and SELinux]]

# SLES Hostname and DNS Resolution

A SLES hostname identifies the local system, while DNS resolution maps names to addresses and addresses back to names according to configured resolvers and search domains. Local host mappings and resolver configuration can also influence the answer, so a displayed hostname and a successful DNS lookup are related but separate facts.

Diagnosis should test the exact name used by an application and inspect which configuration source supplied the result. A working IP route does not prove DNS works, and a correct DNS answer does not prove that the destination service or firewall permits the connection.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
