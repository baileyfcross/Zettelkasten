2026-09-05 13:11

Status: #baby

Tags: [[XR Display Systems]] · [[Online Multiplayer and Persistent Worlds]] [[Distributed Network Caching Monitoring and Inspection]]

# Latency

Latency is the delay between an input event and the corresponding system response. In a tracked visual system, motion-to-photon latency covers the time from measuring the user's pose to displaying graphics from the resulting viewpoint.

Latency breaks the temporal agreement between bodily motion and external [[Feedback]]. It can reduce control performance, create registration errors in [[Augmented Reality]], and contribute to [[Cybersickness]]. Variability in the delay can also matter.

Sources include sensing, processing, simulation, rendering, and display refresh. Raising update rates, reducing scene complexity, or predicting motion may reduce parts of the delay, but improving only one stage does not remove every source.

For AR, latency is also a [[Temporal Registration|temporal-registration]] error: the physical view reflects the present while a virtual object is rendered from an older pose. Motion prediction can estimate the viewpoint expected at display time, but variable delay and sudden changes limit how well prediction can compensate.

In an online game, network latency delays the response to a remote player's command and may give faster connections a competitive advantage. Turn-based mechanics, regional or connection-quality matchmaking, prediction, and designs tolerant of timing variation can reduce its effect, but the acceptable delay depends on how precisely play must be synchronized.

# References

[[3duserinterfaces2ande.pdf]]
[[augmentedreality_pearson.pdf]]

[[fundamentalsofgamedesign3e.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
