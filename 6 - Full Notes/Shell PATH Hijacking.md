2026-10-12 00:45

Status: #baby

Tags: [[Shell Script Security and Reliability]]

# Shell PATH Hijacking

Shell PATH hijacking occurs when command lookup finds an attacker's executable before the intended system utility. A writable directory placed early in `PATH` can turn an ordinary command name into code execution under the script's identity or privilege.

Privileged scripts should use a controlled path, absolute command locations where appropriate, and trusted ownership for every searched directory. Changing directories or accepting environment values must not silently introduce a user-writable lookup location.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
