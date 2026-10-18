2026-10-18 16:07

Status: #baby

Tags: [[AI Community Bot Engineering]]

# FAQ-Grounded Support Bot

An FAQ-grounded support bot places an editable question-and-answer document into the model context and asks the model to answer natural-language user questions from that supplied material. The source uses this pattern so non-specialists can update the support knowledge without retraining a model or changing Java code.

Supplying the file is not enough to prevent invention. The first system instruction in the example lets the model assume unsupported product features, producing plausible but false help. Tightening the behavioral instruction to stay within the provided FAQ and admit when it lacks an answer improves the result. The design applies [[Hallucination Control in AI Testing]] by treating an unsupported answer as a failure, not as helpful creativity.

# References

[[chatgptforjava.epub]]
