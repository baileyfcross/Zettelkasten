2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Scalability and Security]]

# Object Scope and Relevancy

Object scope and relevancy determine which replicated game objects matter to a particular client. Excluding irrelevant objects reduces server work and bandwidth while also limiting information that an untrusted client can inspect.

Distance is a useful first filter but is not universally correct: a distant explosion can still matter, and an unseen nearby object may be irrelevant. Games can combine radius, [[Static Zone Relevancy|zones]], [[Potentially Visible Set|potential visibility]], ownership, team, sound, or game rules. Objects that remain in scope can then be ordered by [[Replication Priority]].

# References

[[multiplayergameprogramming.pdf]]
