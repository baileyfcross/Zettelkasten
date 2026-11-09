2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security Delegating Password Encoder

Spring Security's delegating password encoder records which hashing scheme produced a stored credential and dispatches verification to the matching encoder. New credentials can use BCrypt or another current adaptive scheme while older supported hashes remain verifiable during a migration.

The arrangement prevents a forced all-at-once password reset and allows a successful login to become an opportunity to upgrade the stored hash. It does not make weak legacy hashes safe indefinitely, and plaintext passwords must never be stored. Encoding policy, work factor, and retirement of old formats remain explicit security decisions.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
