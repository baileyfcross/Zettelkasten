# Computer Science

Computer Science is the broad index for computing-related topics in the vault. Full Notes should normally use one of the more focused topics below instead of this root topic.

## Overview Chapter

Computer science studies how information can be represented, transformed, and used to produce reliable behavior. Its subject is larger than programming alone. It includes the logical foundations of computation, the engineering of software, the behavior of complex systems, the design of human-facing interfaces, the construction of learning and conversational machines, and the production of interactive systems such as games. These areas are connected by a common question: how can a desired capability be expressed precisely enough that a computational system can perform it, while remaining useful and understandable in the world where it operates?

### From logical rules to system behavior

At the most abstract level, [[Formal Logic]] provides a language for propositions, valid inference, equivalence, and Boolean operations. These ideas make it possible to state conditions precisely and reason about whether a conclusion follows from a set of premises. Programs turn this formal structure into executable behavior, but useful programs are rarely isolated collections of rules. [[Software Engineering]] adds requirements, architecture, implementation practices, testing, documentation, and iteration so that software can remain dependable as its size and context change.

The behavior of a program also depends on how its parts interact. [[Systems Foundations]] introduces boundaries, state, hierarchy, models, and the distinction between a system and its environment. [[System Dynamics]] then explains change through stocks, flows, feedback loops, delays, and nonlinear relationships. A reinforcing loop can amplify growth, while a balancing loop can stabilize a system around a target. When many local interactions produce a global pattern that was not directly specified, the result belongs to [[Emergent Systems]]. Emergence reminds us that understanding every component separately may not be enough to predict the behavior of the whole.

Computational behavior ultimately meets human interpretation. [[Human Cognition]] covers perception, attention, memory, reasoning, skill acquisition, and cognitive load. These capacities determine what people notice, remember, misunderstand, or learn when using a system. Computer science therefore cannot treat the user as an interchangeable input device: the design of representations and controls must account for the strengths and limits of human information processing.

### Interaction expands the system boundary

[[Interaction Design]] treats the exchange between person and machine as a reciprocal loop. An interface presents possible actions, receives input, changes system state, and provides feedback that helps the user decide what to do next. Good interaction depends on a clear conceptual model and short semantic and articulatory distances between a person's goal and the operations supplied by the interface. [[UX Evaluation]] tests whether those relationships actually work through task analysis, usability inspection, walkthroughs, formative studies, and summative measurement.

When interaction moves beyond a flat screen, spatial perception becomes part of computation. [[Spatial Perception and Navigation]] explains depth cues, orientation, cognitive maps, landmarks, and route finding. [[Spatial Interaction]] turns those abilities into techniques for selecting, positioning, rotating, scaling, traveling, and controlling systems in three dimensions. The experience is shaped by the available output technology: [[XR Display Systems]] describes visual, auditory, and haptic displays together with latency, refresh rate, resolution, and field of view. These devices support [[XR Environments]], including virtual, augmented, mixed, and remotely embodied spaces. Presence and usability emerge from the entire perception-action loop, not from display fidelity alone.

### Learning, speech, and conversational machines

Some computational problems are too variable to solve with an exhaustive collection of hand-written rules. [[Machine Learning and Neural Networks]] addresses them by fitting models to examples or rewards. Supervised learning uses labeled data, unsupervised learning searches for latent structure, and reinforcement learning improves a policy through consequences. Neural architectures add layers, recurrence, attention, convolution, and memory mechanisms that can learn complex mappings from large datasets.

Speech illustrates why data-driven modeling matters. [[Speech and Acoustic Modeling]] represents a changing waveform as short frames and feature vectors, then relates that evidence to phonetic units, pronunciations, and probable word sequences. [[Speech Recognition Systems]] use these representations to convert speech into text across speakers, accents, vocabularies, and acoustic conditions. Recognition determines what words were spoken, but it does not determine what those words mean.

That interpretive step belongs to [[Natural Language Understanding Systems]]. An assistant can classify an intent, extract entities, and assemble them into a meaning representation defined by a domain schema or ontology. The [[Dialog Management Systems]] layer combines that representation with conversational and personal context, selects the next action, resolves references, requests missing information, and recovers from ambiguity or errors. Once an action or result is ready, [[Language and Speech Generation]] plans the response, realizes it as text, predicts pronunciation and prosody, and may synthesize a spoken waveform.

[[Virtual Assistant Architecture]] joins recognition, understanding, dialog, generation, and external digital services into a modular pipeline. Architecture alone does not make the interaction natural. [[Conversational Assistant Design]] governs prompts, initiative, turn-taking, multimodality, proactivity, personality, and social expectations. A capable assistant must coordinate its technical modules while making uncertainty, available actions, privacy boundaries, and conversational control legible to the user.

The effects of computational systems cannot be separated from their capabilities. [[AI Ethics]] connects the design and deployment of intelligent systems to questions about human identity, machine moral status, data power, responsibility, explainability, fairness, governance, labor, and environmental sustainability. It treats an AI application as part of a larger sociotechnical system whose outcomes depend on institutions, infrastructure, and the distribution of power as well as code and models.

### Games as computational systems

Games provide a concentrated example of computation, systems, interaction, and experience working together. [[Game Foundations]] organizes the defining structures and expressive forms of games. [[Game Systems]] examines the parts, attributes, resources, engines, ecologies, and progression structures that generate gameplay, while [[Game Interactivity]] focuses on the reciprocal loop through which player action changes the game and feedback changes later action.

The system becomes meaningful only through a player. [[Player Experience Design]] connects goals, motivation, challenge, flow, fun, mental models, onboarding, and different styles of play. These desired experiences do not follow automatically from a rule set. [[Game Design Methods]] supplies concept statements, prototypes, design documents, playtests, and iterative methods that let a team explore the relationship between rules and experience before committing to a complete production.

Several specialized areas make those relationships measurable and tunable. [[Game Economies]] studies resources, currencies, production, exchange, sources, sinks, prices, inflation, and stagnation. [[Game Balance and Progression]] asks how costs, benefits, difficulty, pacing, and advancement can preserve meaningful choices over time. [[Game Analytics and Probability]] adds probability distributions, random systems, quantitative models, cohorts, retention, and behavioral data. Together, these topics show that balance is neither purely mathematical nor purely intuitive: models propose relationships, play reveals actual behavior, and evidence guides revision.

### Organizing the work

Large computational systems require a development process that can learn while delivering. [[Scrum and Agile Foundations]] describes empirical development, agile values, product ownership, facilitation, and self-managing cross-discipline teams. [[Scrum Iteration Practices]] turns those principles into timeboxed goals, planning, daily coordination, review, and retrospective adaptation. [[Agile Backlog and Estimation]] connects user needs to ordered work through user stories, acceptance criteria, refinement, relative estimates, and release forecasts.

Process also depends on people and organizational structure. [[Agile Team Leadership]] emphasizes coaching, facilitation, psychological safety, shared accountability, and leadership adapted to a team's situation. [[Scaling Agile Teams]] addresses communication overhead, feature and component structures, integration, dependencies, and coordination across many teams. In the specialized setting of [[Game Production]], these practices meet creative vision, scope, milestones, stage gates, quality assurance, live operations, and release constraints.

Across all of these areas, computer science moves repeatedly between abstraction and experience. Logic supplies precision; engineering makes change manageable; systems thinking exposes interactions; human cognition and interface design connect computation to people; machine learning handles variation; and production practices turn uncertain ideas into maintained artifacts. The field is unified less by a single technology than by this disciplined movement from representations and models to behavior, evidence, and revision.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Computer Science]]"
```
