2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Agent Tool Call Accuracy Evaluation

Agent tool call accuracy evaluation measures whether an agent selects the correct tool, supplies valid arguments, avoids unnecessary calls, and interprets the result faithfully. Final-answer scoring alone can miss cases where the agent reached a plausible response through the wrong system or with malformed parameters.

A useful test set includes requests for every tool, requests that require no tool, ambiguous cases, authorization failures, and invalid or incomplete inputs. Traces reveal the selected tool and arguments, while expected-call labels support comparison. Findings can improve tool names, descriptions, schemas, routing instructions, and clarification behavior.

# References

[[microsoftfoundryinaction.pdf]]
