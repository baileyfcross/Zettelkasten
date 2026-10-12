2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# Speech-to-Speech Translation

Speech-to-speech translation turns an utterance in one language into synthesized speech in another. A conventional pipeline recognizes the source audio, translates the transcript, and generates target-language speech, often under the latency constraints of a live conversation.

Its errors are cumulative: a misrecognized name or word cannot be translated correctly downstream, and translation delay can disrupt turn taking. Narrow services such as spoken database queries are more tractable than unrestricted multilingual conversation because their vocabulary and expected actions are bounded. Practical evaluation must include recognition accuracy, translation fidelity, latency, and conversational usability together.

# References

[[machinetranslation.epub]]
