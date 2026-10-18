2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Discord Gateway Intent Subscription

A Discord gateway intent subscription declares which categories of server events a bot wants to receive. The source enables message-content events for its Q&A bot and adds member-related events for its moderator rather than subscribing the Java process to every possible notification.

Intents control event delivery, while [[Discord Bot Permission Scoping|permissions]] control what the bot may do. A handler cannot process content it never receives, and receiving an event does not authorize a response. Selecting only necessary intents reduces irrelevant traffic and makes the bot's observation boundary explicit. Privileged intents require deliberate configuration because access to message or member data carries greater operational and privacy consequences.

# References

[[chatgptforjava.epub]]
