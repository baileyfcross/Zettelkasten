2026-10-04 00:30

Status: #baby

Tags: [[Game Design Documentation]]

# Game State Flowchart

A game state flowchart documents how play moves among starts, endings, processes, rule checks, player decisions, and distant subflows. Every outgoing branch from a conditional or player decision should be labeled and collectively cover the possible cases.

Distinct shapes separate sources of change: diamonds represent system conditions, parallelograms represent external player decisions, rectangles represent processes, ovals begin or end a flow, and circles connect to another diagram. Counting meaningful player-decision branches can also reveal how much of the flow is actually controlled by the player.

# References

[[playersmakingdecisions.pdf]]

