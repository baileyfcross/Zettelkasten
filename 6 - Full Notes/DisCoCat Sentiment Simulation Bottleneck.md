2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# DisCoCat Sentiment Simulation Bottleneck

The available DisCoCat implementation becomes the dominant constraint in the financial-sentiment experiment. Its circuit simulator is CPU-only, and training for 100 epochs on the low-complexity data requires roughly 82 hours on the same setup used for the QLSTM evaluation.

To reduce that cost, the experiment drops all neutral examples and trains a binary classifier. The sentence space $S$ can then be represented by one qubit, minimizing the output register, yet accuracy after 100 epochs remains only slightly above the 50% random-guessing level despite a visible learning trend.

This result measures a particular software stack and restricted training budget, not the ultimate quality of [[DisCoCat Compositional Sentence Model]]. GPU circuit simulation or a more efficient implementation could change both the feasible dataset and the attained accuracy, which is why [[QLSTM-DisCoCat Benchmark Comparability]] rejects a universal ranking.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
