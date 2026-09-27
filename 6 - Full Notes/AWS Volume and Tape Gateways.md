2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# AWS Volume and Tape Gateways

AWS Volume Gateway presents iSCSI block volumes backed by cloud storage, while Tape Gateway presents virtual tapes to existing backup software and stores them through AWS archival services. Both preserve interfaces expected by established on-premises tools.

The modes serve different recovery workflows: volumes support block-oriented application data and snapshots, whereas virtual tapes support backup catalogs and long retention. Restore time and local cache behavior should be tested before relying on either for continuity.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
