2026-09-30 23:37

Status: #baby

Tags: [[Windows Server Security and PKI]]

# Certificate Template and Auto-Enrollment

An Active Directory certificate template is a reusable recipe for certificates issued by an enterprise CA. It defines purpose, key and cryptographic settings, validity, subject naming, and which users or computers may read and enroll. A new template is commonly created by duplicating a compatible built-in version, modifying it, and publishing it on the issuing CA.

Publishing makes the template available, but security permissions still determine who can request it. Auto-enrollment adds Group Policy so eligible domain members request and renew appropriate certificates without a manual MMC workflow. Broad Enroll or Autoenroll rights can distribute a powerful credential farther than intended, so template permissions and intended purpose must agree. Changes also depend on directory and CA replication; troubleshooting should distinguish an unpublished template from one hidden by permissions or stale replication.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
