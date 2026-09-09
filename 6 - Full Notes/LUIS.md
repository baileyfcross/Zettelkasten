2026-09-08 22:09

Status: #baby

Tags: [[Natural Language Understanding Systems]]

# LUIS

LUIS, the Language Understanding Intelligent Service, is the 2019 Azure service used by the book to train a small language model for intent recognition. Developers define intents, supply example phrases, train the model, test classifications, and correct mistakes.

The Bot Framework client sends an incoming activity to a LUIS recognizer and receives the top-scoring intent. Application code then maps that symbolic result to a response, keeping language classification separate from reply selection.

# References

[[c8andnetcore30projectsusingazure.pdf]]
