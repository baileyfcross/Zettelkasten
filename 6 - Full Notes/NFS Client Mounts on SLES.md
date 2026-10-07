2026-10-07 18:14

Status: #baby

Tags: [[SLES Storage and Snapshot Administration]]

# NFS Client Mounts on SLES

An NFS client mount attaches a directory exported by a remote server to the local filesystem namespace. The client specifies the server, exported path, local mount point, protocol behavior, and options, while the server's export policy and underlying permissions still govern the accessible data.

Successful name resolution or network reachability does not prove an export is authorized or responsive. Persistent NFS mounts should account for network availability during boot and for the effect of a stalled server. Local ownership displays also depend on identity mapping between client and server.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
