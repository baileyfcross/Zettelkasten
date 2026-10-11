2026-10-11 12:45

Status: #baby

Tags: [[Sentiment Analysis Methods]]

# Emoticon Sentiment Feature

An emoticon sentiment feature summarizes the polarity carried by emoticons before punctuation removal erases them. One practical representation subtracts the count of negative emoticons from the count of positive emoticons and appends the score to the text feature matrix.

The feature captures a platform-specific signal that ordinary word counts omit. It depends on an explicit emoticon inventory and cannot resolve irony or cases where an emoticon refers to only one part of a message.

# References

[[textminingandvisualization.pdf]]
