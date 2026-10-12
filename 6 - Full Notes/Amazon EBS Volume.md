2026-09-27 18:58

Status: #baby

Tags: [[AWS Compute and Serverless Services]]

# Amazon EBS Volume

An Amazon Elastic Block Store volume provides persistent block storage for EC2 within one availability zone. It can hold an instance boot filesystem or application data and normally survives instance stop or replacement according to its deletion settings.

Volume types trade price, IOPS, throughput, and capacity. Snapshots copy block changes to durable AWS storage for recovery and creation of new volumes. A volume's zonal scope must align with the instance that attaches to it.

The book distinguishes general-purpose SSD volumes from provisioned-IOPS SSD volumes and throughput-oriented HDD volumes. Selection should follow the workload’s IOPS, throughput, latency, size, and boot requirements rather than treating all block storage as interchangeable; [[AWS Compute Optimizer]] can add utilization evidence to a resizing decision.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
