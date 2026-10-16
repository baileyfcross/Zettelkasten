2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# DisCoCat Diagram-to-Circuit Translation

DisCoCat translates a grammar-aware sentence model into a quantum circuit in three stages: parse a pregroup expression, reduce it to a compositional diagram, and replace the diagram's semantic components with parameterized quantum word embeddings.

Atomic grammatical types are mapped to vector spaces and type concatenation becomes a tensor product. In the resulting diagram, state boxes are implemented as prepared states $|\psi\rangle$, adjoint boxes as $\langle\psi|$, and straight wires as identity operations. Reading the diagram in circuit order preserves the same categorical composition represented by the pregroup reduction.

For a transitive sentence, the noun wires are contracted against the verb representation while the sentence wire remains as the class-carrying output. The translation preserves structure but introduces the measurement condition described by [[DisCoCat Postselection Overhead]].

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
