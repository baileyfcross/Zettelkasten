2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Critical Image Eager Loading

Images that define the initial experience—such as a hero, primary product view, or immediately visible story image—should normally retain native eager discovery. Delaying them behind JavaScript can make the page feel incomplete even if total transferred bytes fall.

Criticality is contextual rather than determined by file size alone. Begin with obvious above-the-fold content, measure actual visibility and timing, and expand lazy loading only where it does not postpone the user’s main task. See [[Browser Image Request Prioritization]].

# References

[[highperformanceimages.pdf]]
