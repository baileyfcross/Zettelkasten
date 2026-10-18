2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Prompt Instruction and Data Separation

Prompt instruction and data separation distinguishes what the model should do from the material it should analyze. The book first uses a visible delimiter inside one prompt, then shows how separate user messages can keep a summarization command apart from the conversation being summarized.

The boundary improves readability and makes it easier for code to replace the data without rewriting the instruction. It also exposes which input came from an application designer and which came from a user or external system. Separation is organizational rather than a complete security control: untrusted data can still contain misleading instructions, so the application must combine clear structure with validation and a stable [[Agent System Prompt as Behavioral Contract]].

# References

[[chatgptforjava.epub]]
