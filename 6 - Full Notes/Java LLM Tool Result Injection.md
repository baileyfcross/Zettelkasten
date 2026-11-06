2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Java LLM Tool Result Injection

Java LLM tool result injection adds the application's tool output to the conversation in the role expected by the model protocol, then asks the model to produce a final response. The model does not directly execute the external operation; it receives the result after Java code has completed it.

Tool output is untrusted context even when the application called the tool successfully. Size limits, escaping, provenance, and prompt-injection defenses are needed before external content is returned to the model.

The current source's function callbacks define response converters for building, contact, and weather services before the results reenter the model exchange. Conversion is therefore a policy boundary: the application can select fields, normalize structure, and bound output rather than exposing a raw database row, scraped page, or third-party API response to the next model turn.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
