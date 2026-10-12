2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Network Knowledge Refresh

Network knowledge refresh replaces or reconciles copilot context when inventory, topology, configurations, or standards change. A static mock file is useful for a demonstration, but operational guidance must declare when its facts were captured and how they are updated.

Refresh can pull from approved systems of record, validate the schema, and publish a new version atomically. Failed or partial refreshes should leave the last known-good dataset identifiable rather than mixing versions. Responses can then cite the knowledge version used and warn when its freshness is insufficient for the requested action.

# References

[[ainetworkingcookbook.pdf]]
