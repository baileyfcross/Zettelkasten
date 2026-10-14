2026-09-30 00:32

Status: #baby

Tags: [[React Testing Practice]]

# Redux Reducer Test

A Redux reducer test supplies a known current state and action, invokes the reducer directly, and compares the returned state with the expected value. Because a [[Redux Reducer|reducer]] should be pure, the test needs no browser, store, network, or other external setup.

The source tests each action case with explicit input objects and deep equality. Freezing the input state can additionally expose accidental mutation, distinguishing a reducer that returns the right-looking result by changing its argument from one that constructs a new state correctly.

# References

[[learningreact1.pdf]]
