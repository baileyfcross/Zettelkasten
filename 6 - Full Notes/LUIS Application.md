2026-09-08 22:09

Status: #baby

Tags: [[Natural Language Understanding Systems]]

# LUIS Application

A LUIS application is the configured language model containing intents, example utterances, training state, and published endpoint information. Its application identifier distinguishes the model when a bot creates the recognition client.

Model design is an application contract because the bot's intent-response matrix uses the intent names returned by LUIS. Renaming or removing an intent can therefore break response selection even when the model still publishes successfully.

# References

[[c8andnetcore30projectsusingazure.pdf]]
