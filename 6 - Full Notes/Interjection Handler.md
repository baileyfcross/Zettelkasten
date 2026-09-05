2026-09-05 16:28

Status: #baby

Tags: [[Dialog Management Systems]]

# Interjection Handler

An interjection handler is reusable dialog logic that detects and responds to interruptions such as help, repeat, correction, or cancellation. It can be available from many states without duplicating the same transitions everywhere.

The handler must preserve enough [[Conversation Context]] to resume safely when appropriate. Some interjections instead require clearing state or transferring control to a different [[Assistant Skill]].

# References

[[aiassistants.epub]]
