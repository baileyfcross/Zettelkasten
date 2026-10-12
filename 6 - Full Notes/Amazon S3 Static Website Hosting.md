2026-09-27 18:58

Status: #baby

Tags: [[Amazon S3 and Hybrid Storage]]

# Amazon S3 Static Website Hosting

Amazon S3 static website hosting serves HTML, CSS, images, and other client-side files from a bucket website endpoint. It suits content that does not require server-side execution and can pair with CloudFront for HTTPS, caching, and a custom domain.

The bucket or distribution policy must allow the intended reads without exposing unrelated data. Dynamic form processing and database operations belong in separate services; S3 supplies the static presentation layer rather than an application server.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
