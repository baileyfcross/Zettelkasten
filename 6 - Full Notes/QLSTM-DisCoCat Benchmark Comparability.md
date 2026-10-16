2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# QLSTM-DisCoCat Benchmark Comparability

The finance case study shows that QLSTM is more practical than DisCoCat under the tested software, but it does not support the general claim that QLSTM is the better QNLP architecture. The two systems are evaluated under materially different constraints.

QLSTM has GPU-supported simulation, retains all three sentiment classes, and is trained on both complexity levels. DisCoCat uses a CPU-only simulator, drops the neutral class to minimize its sentence register, runs only on the low-complexity data, and is stopped after a much longer wall-clock budget while still showing gradual learning.

The comparison therefore concerns end-to-end applicability of available implementations. QLSTM approaches the classical baseline and trains faster in that environment, while DisCoCat's measured weakness mixes model behavior with parser, postselection, simulator, and budget limitations. Neither result demonstrates quantum advantage because all quantum circuits are classically simulated.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
