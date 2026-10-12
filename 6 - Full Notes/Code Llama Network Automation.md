2026-09-27 18:30

Status: #baby

Tags: [[Local LLM Network Engineering]]

# Code Llama Network Automation

A code-oriented local model can draft Python network automation from natural-language requirements. A prompt may begin with a Netmiko connection to Cisco devices and then add concurrency, exception handling, logging, or structured output in successive iterations.

The generated program is a starting point rather than a safe executable. Connection handling, credential use, device commands, concurrency limits, and failure behavior require inspection and tests against non-production targets. Running locally protects the prompt path from a hosted provider but does not make the code semantically correct.

# References

[[ainetworkingcookbook.pdf]]
