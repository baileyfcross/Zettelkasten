2026-09-22 23:34

Status: #baby

Tags: [[HTTP FTP SMTP and Custom Protocols]]

# Secure File Transfer Protocol

Secure File Transfer Protocol provides file-transfer operations through an SSH connection. Its authentication, encryption, and message integrity come from the SSH transport rather than from wrapping the ordinary FTP command and data connections.

SFTP is therefore a distinct protocol, not simply FTP with a secure flag. An implementation must use an SSH-capable client and server that agree on the SFTP subsystem.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
