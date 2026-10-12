2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]], [[SLES Service Logging and Remote Operations]]

# Secure Shell Protocol

The Secure Shell protocol provides encrypted remote login, command execution, tunneling, and subsystem channels over a network connection. Its architecture separates secure transport, user authentication, and the multiplexed connection layer.

The transport tier authenticates the server and protects message integrity, the authentication tier validates the client, and the connection tier carries distinct interactive or forwarded channels within the secured session.

On SLES, OpenSSH supplies the server and client implementation used for administrative login, remote commands, file-transfer subsystems, and tunnels. Host-key verification protects the server identity, while account authentication and local authorization determine what the accepted session may do.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
