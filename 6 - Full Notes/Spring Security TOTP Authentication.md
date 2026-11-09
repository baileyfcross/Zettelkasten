2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security TOTP Authentication

Spring Security TOTP authentication adds a time-based one-time code as a second factor after the primary identity is accepted. Enrollment establishes a shared secret with the user's authenticator, and later logins validate a code derived from that secret and the current time window.

The factor reduces the value of a stolen password or magic link but creates secret storage, recovery, clock-skew, and replay concerns. The application should make the second factor a distinct authentication step rather than treating the code as another long-lived password, and recovery paths need protection comparable to enrollment.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
