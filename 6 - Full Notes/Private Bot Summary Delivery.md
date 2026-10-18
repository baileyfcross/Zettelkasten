2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# Private Bot Summary Delivery

Private bot summary delivery sends a requested channel summary directly to the requester instead of posting it back into the busy channel being summarized. The source proposes this as a refinement to its Slack example so an automation intended to reduce information overload does not create more public noise.

The delivery choice is part of the bot's interaction design. A private response protects channel focus and can limit disclosure to the person who requested the synthesis, while a public response may be appropriate when the group needs one shared record. The bot should make the destination explicit, preserve the source time window, and avoid implying that an automated summary replaces the underlying conversation.

# References

[[chatgptforjava.epub]]
