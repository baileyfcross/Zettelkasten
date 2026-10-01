2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Temporary Access Pass

A Temporary Access Pass is a time-limited passcode issued by Microsoft Entra so a user can bootstrap or recover a strong authentication method. It is useful when a new user has no registered factor or when an existing user has lost the device that held a passwordless credential.

An administrator defines whether the pass is single-use or reusable within its validity window. The user signs in with it and registers a durable method such as a passkey or certificate. Because the pass temporarily bridges an unproven user to a new credential, its issuance, delivery, lifetime, and use must be tightly controlled and audited; it is an onboarding mechanism for [[Passwordless Authentication]], not a standing credential.

# References

[[masteringmicrosoftentraid.pdf]]
