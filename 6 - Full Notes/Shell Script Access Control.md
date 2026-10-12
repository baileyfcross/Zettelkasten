2026-10-12 00:45

Status: #baby

Tags: [[Shell Script Security and Reliability]]

# Shell Script Access Control

Shell script access control uses file ownership, mode bits, access-control lists, and privilege policy to determine who may read, modify, or execute a script. A privileged script must not be writable by an identity less trusted than the one under which it runs.

Read and execute authority solve different problems: hiding source does not make unsafe behavior secure, while execute-only arrangements may be ineffective for interpreted files. SUID and SGID bits on scripts are unreliable security mechanisms and should not substitute for narrow [[sudo Policy Delegation]].

# References

[[ultimatelinuxshellscriptingguide.pdf]]
