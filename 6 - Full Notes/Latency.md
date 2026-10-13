2026-09-05 13:11

Status: #baby

Tags: [[XR Display Systems]] [[XR Human Factors and Safety]] · [[Online Multiplayer and Persistent Worlds]] [[Distributed Network Caching Monitoring and Inspection]]

# Latency

Latency is the delay between an input event and the corresponding system response. In a tracked visual system, motion-to-photon latency covers the time from measuring the user's pose to displaying graphics from the resulting viewpoint.

Latency breaks the temporal agreement between bodily motion and external [[Feedback]]. It can reduce control performance, create registration errors in [[Augmented Reality]], and contribute to [[Cybersickness]]. Variability in the delay can also matter.

Sources include sensing, processing, simulation, rendering, and display refresh. Raising update rates, reducing scene complexity, or predicting motion may reduce parts of the delay, but improving only one stage does not remove every source.

For AR, latency is also a [[Temporal Registration|temporal-registration]] error: the physical view reflects the present while a virtual object is rendered from an older pose. Motion prediction can estimate the viewpoint expected at display time, but variable delay and sudden changes limit how well prediction can compensate.

In an immersive headset, the base motion-to-photon delay accumulates while sensors measure head pose, the application updates the viewpoint, two eye images are rendered, and the display scans out new pixels. That total can break agreement between proprioceptive motion and visible response, weakening [[Presence]] and increasing [[Cybersickness]] even when no individual stage appears exceptionally slow.

In an online game, network latency delays the response to a remote player's command and may give faster connections a competitive advantage. Turn-based mechanics, regional or connection-quality matchmaking, prediction, and designs tolerant of timing variation can reduce its effect, but the acceptable delay depends on how precisely play must be synchronized.

Game latency also accumulates outside the network through input sampling, simulation, a multithreaded render pipeline, vertical synchronization, display refresh, and pixel response. Network delay adds propagation, transmission, processing, and queuing components. [[Round-Trip Time]] measures a message and response together, while [[Network Jitter]] describes variation that can make a steady update stream arrive unevenly.

An immersive renderer can preserve CPU/GPU overlap while reducing perceived delay by sampling tracked pose late, after most game work is complete. Timewarp or reprojection then transforms an already rendered eye image using a newer head orientation immediately before scan-out. On a predictable mobile pipeline, front-buffer scanline racing can update the warped image close to the display's line-by-line refresh. These techniques reduce particular latency components and provide fallback for missed timing; they do not excuse an application from sustaining its target frame rate.

Immersive systems are especially sensitive because the physical head has already moved while the delayed scene still depicts an older viewpoint. Delays on the order of only tens of milliseconds can become perceptible when visual, auditory, and haptic events no longer agree. The requirement is therefore end-to-end coordination across modalities, not merely a fast graphics benchmark.

# References

[[3duserinterfaces2ande.pdf]]
[[augmentedreality_pearson.pdf]]
[[practicalaugmentedreality.pdf]]

[[fundamentalsofgamedesign3e.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[multiplayergameprogramming.pdf]]
[[unrealenginevrcookbook.pdf]]
[[virtualreality.epub]]
