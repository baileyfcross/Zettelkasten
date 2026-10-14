2026-09-08 22:39

Status: #baby

Tags: [[Cloud Computing Foundations]], [[Computational Environment Portability]]

# Virtual Machine

A virtual machine is a software-defined computer instance that runs on shared physical hardware. It presents processors, memory, storage, and networking to its own operating system while remaining logically separate from other virtual machines on the host.

Cloud resource pools can create or remove virtual machines to alter capacity quickly. This makes the virtual machine an important unit for [[Server Virtualization]], [[Horizontal Scalability]], and infrastructure delivery.

In an AWS infrastructure service such as [[Amazon EC2 Instance|Amazon EC2]], the provider operates the physical host and virtualization layer while the customer still manages the guest operating system, installed software, and many host-level security decisions.

For reproducible research, a virtual machine can preserve a complete working environment as an image: operating system, libraries, configuration, code, and selected data. This reduces installation and portability burdens, though an undocumented image remains difficult to understand or extend and does not by itself capture workflow provenance.

# References

[[cloudcomputing_mit.epub]]

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]

[[implementingreproducableresearch.pdf]]
