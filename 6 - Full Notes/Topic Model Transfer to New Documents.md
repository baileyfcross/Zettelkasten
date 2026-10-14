2026-10-11 12:45

Status: #baby

Tags: [[Probabilistic Topic Modeling]]

# Topic Model Transfer to New Documents

Topic model transfer infers a [[Document Topic Distribution]] for unseen documents while holding a fitted topic vocabulary and topic-term structure fixed. The new text must undergo the same preprocessing and matrix construction used during training.

Terms absent from the training vocabulary cannot contribute to the inferred mixture. As language and subject matter change, periodic retraining is necessary so the model does not silently ignore an increasing share of new documents.

# References

[[textminingandvisualization.pdf]]
