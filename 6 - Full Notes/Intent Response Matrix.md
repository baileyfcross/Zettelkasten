2026-09-08 22:09

Status: #baby

Tags: [[Microsoft Bot Framework Applications]]

# Intent Response Matrix

An intent-response matrix maps each recognized conversational intent to one or more possible replies. It separates the language model's classification from the text the bot returns, so response content can change without retraining the recognizer.

The project stores arrays of replies in an embedded JSON resource, retrieves the array for the winning intent, and selects one entry at random. A fallback intent supplies responses when no more specific class is recognized.

# References

[[c8andnetcore30projectsusingazure.pdf]]
