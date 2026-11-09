2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security One-Time Token Login

Spring Security one-time-token login issues a short-lived, single-use token after a user supplies an identity such as an email address. A success handler delivers a link containing the token through a separate channel, and presenting the link completes authentication without a reusable password.

The token service controls generation, storage, expiry, and consumption. A magic link is a bearer credential until used, so transport protection, a brief lifetime, and invalidation after success are essential. The delivery channel's security becomes part of the authentication boundary, and higher-risk actions can still require [[Spring Security TOTP Authentication]].

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
