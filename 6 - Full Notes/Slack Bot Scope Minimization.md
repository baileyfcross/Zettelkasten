2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Slack Bot Scope Minimization

Slack bot scope minimization grants a bot only the platform capabilities required for its job. The book's channel summarizer needs to discover channels, read channel history, and resolve user identities, so its bot token scopes are limited to those operations rather than broad workspace administration.

The scopes define what Slack will authorize; inviting the app to a channel defines where it can participate. The Java process still runs outside Slack and presents its OAuth bearer token when calling the platform. Narrow scopes reduce the damage of a leaked token or faulty implementation, but the credential must still be protected and rotated. A new feature should trigger an explicit permission review instead of accumulating unrelated privileges by default.

# References

[[chatgptforjava.epub]]
