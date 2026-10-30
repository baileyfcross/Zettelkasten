2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Swing Event Dispatch Thread

Swing creates and updates most interface components on the Event Dispatch Thread. Event listeners also run there, so a long computation inside a listener blocks repainting and input until it returns.

An application schedules initial UI construction with `SwingUtilities.invokeLater` and moves slow work to a background task, returning only component updates to the dispatch thread. The rule is ownership rather than speed: one thread serializes live UI state so handlers do not race with painting and layout.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
