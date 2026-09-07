2026-09-06 20:34

Status: #baby

Tags: [[Web Forms and Validation]]

# Asynchronous Validator

An asynchronous validator evaluates a form rule whose result is not available immediately. It returns a future result, commonly through an [[Observable]], and leaves the control pending until that result arrives.

A duplicate-name validator can call a server endpoint because uniqueness depends on stored records rather than the current browser model. The request should be controlled to avoid sending a new server check for every unnecessary keystroke.

# References

[[aspnetcore3andangular9_3ed.pdf]]
