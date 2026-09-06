2026-09-05 13:11

Status: #baby

Tags: [[Human-Computer Interaction Foundations]] [[Game Interactivity]]

# User-System Loop

The user-system loop models the flow of information between a person and a computer from a system-centered perspective.

User actions are sensed by [[Input Device]]s. Transfer functions interpret the input as system effects, which update the simulation's data and models. Rendering then turns the updated state into commands for [[Output Device]]s, producing stimuli the user perceives. That perception informs the user's next action, closing the loop.

The model helps locate design problems. Device choice and input mappings affect interpretation, simulation affects the resulting state, and rendering or device [[Latency]] can delay [[Feedback]].

The same structure becomes reciprocal [[Interactivity]] when the user's updated mental state produces a new intention. In games, this cycle forms the [[Core Gameplay Loop]] and couples the [[Game Model]] with the [[Player Mental Model]] inside a larger [[Game-Player System]].

# References

[[3duserinterfaces2ande.pdf]]
[[advancedgamedesign.pdf]]
