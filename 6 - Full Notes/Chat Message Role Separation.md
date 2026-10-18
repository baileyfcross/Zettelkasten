2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Chat Message Role Separation

Chat message role separation represents a conversation as ordered messages with distinct responsibilities. In the book's 2024 interface, the system message defines the assistant's operating role, user messages supply requests or data, assistant messages preserve prior model output, and tool messages participate in function-oriented exchanges.

This structure is more reliable than flattening every instruction and datum into one undifferentiated string. The application can keep the [[Agent System Prompt as Behavioral Contract|behavioral contract]] stable, add user turns independently, and reconstruct relevant assistant turns through [[Conversation History Reconstruction]]. Roles organize the input, but they do not enforce authorization or guarantee that the model will follow every instruction.

# References

[[chatgptforjava.epub]]
