2026-10-18 16:30

Status: #baby

Tags: [[Java Platform Cryptography and Security]]

# Jakarta Security

Jakarta Security is the enterprise Java API for portable authentication and authorization mechanisms. The source describes basic, form-based, and JSF-oriented form authentication and presents client-certificate, digest, OpenID, OAuth, and JSON Web Token support as part of the Jakarta EE 11 security direction.

Authorization annotations such as `@RolesAllowed` and `@RunAs` express access constraints near application components, while Contexts and Dependency Injection makes security mechanisms easier to integrate. The broader design also includes secure session defaults, TLS configuration, service-to-service identity propagation, and ongoing patching and testing for cloud-native applications.

Its portable model separates an HTTP authentication mechanism from an identity store. The mechanism obtains evidence from a request and coordinates authentication; the store validates credentials and supplies groups. The resulting caller principal and group information can then be mapped to application roles. This allows local basic or form login and an external social identity flow to share the container's authorization model without embedding the credential database in the web protocol handler.

# References

[[cryptographyandcryptanalysisinjava.epub]]

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
