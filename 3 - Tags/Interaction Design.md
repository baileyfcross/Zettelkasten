# Interaction Design

Parent topic: [[Computer Science]]

Interfaces, interaction techniques, feedback, devices, and the design of human-system relationships.

## Overview Chapter

Interaction design shapes the loop through which people express intentions, systems interpret them, and feedback supports the next action. Conversational assistants make this loop unusually visible because the interface uses the same medium people use with one another. A spoken request may feel simple, but the system must transform sound into words, words into meaning, meaning into action, and results back into language while preserving conversational context.

[[Human-Computer Interaction Foundations]] supplies the broader principles behind this loop: conceptual models, affordances, input and output devices, feedback, ergonomics, social context, and the relationship between a user's goal and the operations an interface provides. These foundations make it possible to evaluate a conversational interface as an interaction system rather than only as a language technology.

### From speech to actionable meaning

[[Speech Recognition Systems]] begin the pipeline by converting an acoustic signal into a textual hypothesis. Recognition must handle speaker differences, continuous speech, accents, noise, distance, and a vocabulary that may be either tightly constrained or very broad. Confidence matters because the transcript is evidence, not certainty. A voice interface should use prompts and context to narrow likely responses when possible, while preserving a recovery path when the signal is misunderstood.

The transcript then enters [[Natural Language Understanding Systems]]. Understanding identifies an intent, extracts entities, and composes them into a representation that the assistant can act upon. Grammars can provide precise structures for narrow tasks, while statistical classifiers and embeddings generalize across varied wording. Neither approach eliminates ambiguity. The system needs a domain model that defines what actions and arguments are meaningful, as well as a way to recognize when the input falls outside that model.

### Managing a conversation

[[Dialog Management Systems]] decide what should happen next. The dialog manager combines the interpreted input with prior turns, personal or display context, external service state, and a policy. It may ask for a missing value, resolve an elliptical expression, clarify competing interpretations, invoke a service, or recover from a timeout or error.

This layer turns independent utterances into a conversation. A phrase such as “the second one” can only be understood by retaining the alternatives presented earlier. A correction or help request may interrupt the expected flow and then return to it. Finite-state structures make narrow tasks predictable, while more flexible policies support information arriving in an unexpected order. In either case, the system should preserve what it has understood and avoid making the user restart unnecessarily.

### Producing the response

[[Language and Speech Generation]] transforms a symbolic action or result into an expression appropriate to the situation. A generator decides what information to include, how to organize it, which words and grammatical forms to use, and whether related facts should be aggregated. Template systems offer control for recurring messages, while more flexible generation supports greater variation.

For spoken output, text normalization expands dates, numbers, abbreviations, and symbols; phonetic transcription supplies pronunciations; prosodic prediction supplies rhythm, emphasis, and intonation; and a synthesizer generates the waveform. A correct sentence can still be a poor interaction if it is too long, repeats information, uses an unclear reference, or speaks with timing that disrupts turn-taking.

### Joining the modules

[[Virtual Assistant Architecture]] connects recognition, understanding, dialog, generation, and digital services into a modular system. It also distinguishes forms such as virtual agents, personal assistants, chatbots, and interactive voice response systems. Wake-word detection, local and remote processing, service integration, and assistant skills determine where computation occurs and which capabilities can be reached.

Modularity makes the system maintainable, but the user experiences one assistant rather than a collection of components. An error introduced during recognition may surface as an inappropriate service action or an incoherent reply. Interaction design therefore evaluates the complete path from intention to outcome, including latency, uncertainty, privacy, and the cost of recovery.

### Designing conversational conduct

[[Conversational Assistant Design]] governs initiative, prompting, turn-taking, multimodality, proactivity, social behavior, and personality. Directed prompts constrain the next response, while open prompts give the user more initiative. Mixed-initiative interaction lets both parties advance the task. Proactive and asynchronous behavior can be valuable, but it also introduces interruption and privacy risks because the assistant chooses when to act.

Speech may be combined with touch, displays, gaze, or physical embodiment. These channels must share context so that words such as “this” and “there” refer to the same visible or spatial objects. Personality and nonverbal behavior should make the interaction coherent without encouraging users to overestimate the system's understanding. The best conversational interface is not the one that most closely imitates a person; it is the one that makes capabilities, uncertainty, control, and consequences easy to understand.

Together, these topics show conversation as an engineered interaction loop. Recognition supplies hypotheses, understanding supplies structure, dialog supplies continuity and action, generation supplies expression, architecture joins the capabilities, and conversational design makes the entire system usable and trustworthy.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Interaction Design]]"
```
