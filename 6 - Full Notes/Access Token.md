2026-09-06 20:52

Status: #baby

Tags: [[Web Identity and Access Control]]

# Access Token

An access token is a credential a client presents to an API when requesting a protected operation. The React client obtains a token for the configured API and sends it in the authorization header of its fetch request.

The API validates the token's issuer, audience, signature, and applicable claims before accepting the identity it represents. A token should be requested and used for its intended resource rather than treated as a general user profile.

# References

[[aspnetcore3andreact.pdf]]
