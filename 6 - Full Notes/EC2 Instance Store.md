2026-09-27 18:58

Status: #baby

Tags: [[AWS Compute and Serverless Services]]

# EC2 Instance Store

EC2 instance store is temporary block storage physically attached to the host running an eligible instance. It offers low-latency access but its data is lost when the instance is stopped, terminated, or moved from that host.

It is appropriate for caches, buffers, scratch data, and replicated information that can be recreated. Durable application state needs EBS, file, object, or database storage. Performance does not make ephemeral media a backup destination.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
