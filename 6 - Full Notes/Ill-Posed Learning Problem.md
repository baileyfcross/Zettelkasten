2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning and Neural Networks]]

# Ill-Posed Learning Problem

Function learning is ill posed when the available examples do not determine one unique mapping from inputs to outputs. Kelleher illustrates this with several candidate arithmetic rules: more than one rule can match the observed examples, even though they disagree on unseen inputs.

Noise and a large space of possible functions make the problem harder. More examples may distinguish candidates, but collecting them can be expensive or impossible. A [[Machine Learning]] algorithm therefore combines evidence from a [[Training Dataset]] with an [[Inductive Bias in Machine Learning|inductive bias]] that favors some candidate functions. The bias makes learning possible without proving that the favored function is the one true explanation.

# References

[[deeplearning_mit.epub]]
