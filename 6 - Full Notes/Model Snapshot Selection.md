2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Model Snapshot Selection

Model snapshot selection chooses a dated model identifier instead of a moving alias when the API offers both. The source explains that an alias may be updated over time, while a snapshot gives the application a more stable target for testing and response expectations.

Stability has a lifecycle cost. A pinned snapshot will not automatically receive improvements and may later be labeled legacy or deprecated, so the application must monitor the [[OpenAI Model Catalog Request|available model catalog]] and plan migration. A moving alias reduces manual upgrades but can change behavior without a code change. The choice should match whether the application values repeatable evaluation or automatic adoption of provider updates.

# References

[[chatgptforjava.epub]]
