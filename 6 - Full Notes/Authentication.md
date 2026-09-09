2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]] [[.NET Cryptography and Access Control]] [[Cloud Security and Data Protection]]

# Authentication

Authentication is the process of verifying that a person or automated system is the identity it claims to be. A web application commonly collects credentials or completes a trusted-provider exchange before establishing an authenticated user.

Authentication answers who the client is; [[Authorization]] answers what that identity may view or change. Sessions, tokens, signatures, and second factors are different mechanisms for carrying or strengthening the result.

The stock-checker project separates authentication from permission: a user must first establish an accepted identity before the application considers which stock operations that identity may perform. IdentityServer issues the token used to carry that authenticated relationship to the API.

Within a cloud [[Security Container]], authentication follows identification and establishes whether a claimed person, application, system, or connected device is legitimate. Evidence may be something the claimant knows, something it possesses, or a biometric characteristic.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cloudcomputing_mit.epub]]
