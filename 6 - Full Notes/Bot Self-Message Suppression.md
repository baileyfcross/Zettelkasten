2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Bot Self-Message Suppression

Bot self-message suppression prevents a message-handling bot from reacting to the message it just sent. The source observes that Discord delivers a bot's own reply back through the same message callback, so an unfiltered listener can produce a feedback loop of responses to responses.

Checking only the current bot's identity is the minimum safeguard. When several bots share a server, a Q&A bot may still react to a moderator's notice unless the handler excludes other bot authors or defines an explicit inter-bot protocol. Suppression should happen before expensive model calls or public replies. The rule turns author identity into an input filter for the [[Event-Driven Discord Message Listener]].

# References

[[chatgptforjava.epub]]
