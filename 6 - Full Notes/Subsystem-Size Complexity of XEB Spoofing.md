2026-10-17 03:33

Status: #baby

Tags: [[Random-Circuit Quantum Advantage Verification]]

# Subsystem-Size Complexity of XEB Spoofing

If an $N$-qubit depth-$d$ circuit is divided into pieces of at most $l$ qubits, brute-force simulation of the pieces takes at most order $2^{O(l)}Nd/l$. Holding $l$ fixed therefore makes the total cost linear in circuit size even though exact simulation of the unpartitioned circuit is exponential in $N$.

The spoofed XEB is governed by a tradeoff. Larger subsystems cost more but require fewer omitted gates and preserve more ideal correlation; smaller subsystems are cheaper but create more boundaries. In one-dimensional random circuits, a fixed-size partition can eventually outscore a noisy quantum device for any constant physical error rate as $N$ grows because the device's correlation decays through the bulk while the partition errors remain localized.

# References

[[2024 - Limitations of Linear Cross-Entropy as a Measure for Quantum Advantage.pdf]]

