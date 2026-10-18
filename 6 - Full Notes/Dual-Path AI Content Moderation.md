2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Dual-Path AI Content Moderation

Dual-path AI content moderation evaluates one community message with two classifiers aimed at different policy domains. In the source's Discord example, a moderation endpoint checks its defined unsafe-content categories, while a chat prompt checks a community-specific rule about solicitation and scams. A flag from either path causes the bot to remove the message and notify the author.

The arrangement distinguishes provider-defined safety categories from local community policy instead of expecting one classifier to cover both. It also creates two possible error sources, so the application should retain which path and category triggered an action. Automated deletion is consequential; the book demonstrates the mechanism but the broader design still needs review, appeal, and handling for uncertain or conflicting classifications.

# References

[[chatgptforjava.epub]]
