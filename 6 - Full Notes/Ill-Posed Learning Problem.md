2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning Foundations]]

# Ill-Posed Learning Problem

Function learning is ill posed when the available examples do not determine one unique mapping from inputs to outputs. Kelleher illustrates this with several candidate arithmetic rules: more than one rule can match the observed examples, even though they disagree on unseen inputs.

Noise and a large space of possible functions make the problem harder. More examples may distinguish candidates, but collecting them can be expensive or impossible. A [[Machine Learning]] algorithm therefore combines evidence from a [[Training Dataset]] with an [[Inductive Bias in Machine Learning|inductive bias]] that favors some candidate functions. The bias makes learning possible without proving that the favored function is the one true explanation.

Even a short number sequence admits many exact continuations, and a more complex rule can always be invented to absorb recording errors. The learning problem becomes determinate only after adding preferences such as smoothness or simplicity. These assumptions should match the task: they are the reason the learner can choose one explanation, not facts proven by the sample itself.

# References

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]
