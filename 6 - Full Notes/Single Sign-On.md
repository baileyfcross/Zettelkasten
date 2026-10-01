2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Identity and Authentication]]

# Single Sign-On

Single sign-on lets a user establish a session with an identity provider and then reach several trusted applications without presenting a separate application password each time. The applications delegate [[Authentication]] to the provider and accept a validated assertion or token under a configured trust relationship.

Microsoft Entra can provide SSO to cloud applications through SAML or OpenID Connect and to suitable on-premises applications through identity-aware access services. SSO reduces duplicated credentials and centralizes policy, but it also makes the identity-provider session important: applications must still validate the token and enforce their own [[Authorization]], while Conditional Access and session controls determine whether the shared sign-in remains acceptable.

# References

[[masteringmicrosoftentraid.pdf]]
