2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Data and Model Design]]

# Microsoft Foundry Data Connection Patterns

Microsoft Foundry supports distinct connection patterns for different kinds of enterprise data. Storage connections expose static files and tables, Azure AI Search indexes content for semantic retrieval, and MCP connections expose live tools or external systems that can retrieve current records or perform approved actions.

The patterns are complementary. A knowledge assistant may use indexed policy documents for stable reference material and an API or MCP tool for inventory that changes every minute. Choosing among them depends on freshness, search needs, side effects, authorization, deletion requirements, and maintenance cost rather than on a desire to route every source through one mechanism.

# References

[[microsoftfoundryinaction.pdf]]
