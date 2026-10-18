2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Discord Bot Permission Scoping

Discord bot permission scoping selects the server operations an installed bot is allowed to perform. The source gives a Q&A bot only message-reading and message-sending permissions, while a separate moderation bot also receives powers needed to manage messages and members.

Registration, invitation, and the bot token establish the application identity, but the chosen permissions determine its authority inside the server. Different responsibilities should receive different permission sets rather than sharing one overpowered bot credential. Platform permissions also do not replace application checks: the Java handler must still restrict itself to the intended channels and operations. [[Single-Responsibility Community Bots]] makes that least-privilege boundary easier to understand and review.

# References

[[chatgptforjava.epub]]
