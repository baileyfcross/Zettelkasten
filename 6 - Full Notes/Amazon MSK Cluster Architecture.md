2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Engineering and Analytics Optimization]]

# Amazon MSK Cluster Architecture

An Amazon MSK provisioned cluster places Kafka broker nodes across multiple availability zones and stores topic partitions on those brokers. Replicas distribute a partition’s data so a broker or zone failure does not remove every copy. Client applications connect as producers or consumers through the cluster endpoints. Broker count, instance capacity, storage, partition count, replication factor, and traffic distribution must be sized together because Kafka scale is partition-driven.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

