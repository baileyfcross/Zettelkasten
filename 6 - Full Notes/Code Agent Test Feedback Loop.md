2026-09-30 17:53

Status: #baby

Tags: [[Code LLM Development Workflows]]

# Code Agent Test Feedback Loop

A code agent test feedback loop alternates between implementation, execution, failure interpretation, and revision. Test output gives the model concrete evidence about syntax, dependencies, and behavior that cannot be established from generation probability alone.

The loop needs a bounded retry count and should not weaken or delete failing tests merely to obtain a green result. Persistent failures, unclear requirements, or broad side effects should stop the agent and request review.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
