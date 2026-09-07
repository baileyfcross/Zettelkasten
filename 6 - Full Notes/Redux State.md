2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux State

Redux state is the read-only snapshot of shared application data held by the store. Code does not edit that snapshot in place; it dispatches an action and lets a reducer calculate the replacement state.

This constraint makes each transition traceable to a particular action. Components can select only the portion they need while the store retains one coherent source of truth.

# References

[[aspnetcore3andreact.pdf]]
