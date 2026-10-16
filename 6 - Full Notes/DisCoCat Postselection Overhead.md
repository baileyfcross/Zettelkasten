2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# DisCoCat Postselection Overhead

The DisCoCat circuit extracts the sentence state only from measurement outcomes that satisfy the grammatical contractions. In the transitive-sentence example, the two noun registers must both be observed in their all-zero states before the remaining register is accepted as the sentence meaning $|s\rangle$.

This classical postselection discards unsuccessful executions. Increasing the number of qubits used for each noun-space wire enlarges the condition that must be met and can make the total runtime grow sharply even if the accepted circuit output is compact.

Postselection is therefore a resource cost that is hidden by the abstract equivalence between grammar diagrams and circuits. It compounds the CPU simulation constraint in [[DisCoCat Sentiment Simulation Bottleneck]] and should be included when comparing DisCoCat with recurrent alternatives.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
