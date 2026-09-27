2026-09-27 18:30

Status: #baby

Tags: [[AI-Assisted Network Automation]]

# Environment-Based AI API Credentials

An AI API credential should be loaded from an environment variable or a managed secret rather than embedded in a network script. This keeps the key out of source files, examples, and ordinary version-control history while allowing the same program to run with different credentials in different environments.

Environment storage is only one layer of protection. The variable still inherits the exposure and lifetime of its process and shell session, so it should be narrowly scoped, rotated, and excluded from logs. A missing key must cause a clear failure before a [[Network AI API Request Anatomy]] call is attempted.

# References

[[ainetworkingcookbook.pdf]]
