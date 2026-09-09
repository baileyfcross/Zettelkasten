2026-09-08 22:09

Status: #baby

Tags: [[Microsoft Bot Framework Applications]]

# Bot Conversation Turn

A bot conversation turn is one cycle in which an incoming activity is processed and zero or more outgoing activities are produced. The turn context provides the current message and the operation used to send the bot's response.

Conversation quality depends on more than one isolated turn because earlier answers can determine which information is missing next. The book's simplified bot chooses a response from the recognized current intent rather than implementing a deeper dialog state model.

# References

[[c8andnetcore30projectsusingazure.pdf]]
