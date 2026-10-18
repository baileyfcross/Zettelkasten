2026-10-18 16:07

Status: #baby

Tags: [[Java OpenAI API Integration]]

# API Token Usage Metadata

API token usage metadata reports how many model tokens a request consumed. The source's chat response separates prompt tokens, completion tokens, and their total, making the cost of input context and generated output visible to the calling application.

Recording these values lets a Java client compare prompt designs, detect unusually large calls, and relate a response to the model's context and billing constraints. The count is not the same as Java string length because [[Text Tokenization]] divides text according to the model's tokenizer. Usage should be attached to the request outcome even when the visible answer is short, since a long conversation history can dominate the input cost.

# References

[[chatgptforjava.epub]]
