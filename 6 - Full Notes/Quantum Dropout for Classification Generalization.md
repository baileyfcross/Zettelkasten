2026-10-12 18:44

Status: #baby

Tags: [[Quantum Dropout Regularization]]

# Quantum Dropout for Classification Generalization

The classification experiment applies quantum dropout to a noisy two-class Moons dataset with a five-qubit, twenty-layer circuit containing 180 trainable parameters. Only 40 percent of the 50 examples are used for training and 60 percent for testing, deliberately exposing the overfitting behavior of the highly expressive [[Classifier]].

Without dropout, categorical cross-entropy on the test set begins rising after roughly 1,000 of the 5,000 training epochs while training loss continues falling. With dropout, test loss and test accuracy instead track their training counterparts more smoothly and with smaller run-to-run spread. [[Independent Quantum Dropout]] gives the best reported average result, lowering test cross-entropy by about 32.5 percent relative to no dropout; effective drop probabilities for the best configurations range from about 1 to 6 percent.

Canonical and canonical-forward dropout are equivalent in this architecture because each reuploading layer has one variational sublayer. Entangling dropout is the only evaluated strategy that reduces test cross-entropy by less than 30 percent and also has the largest standard deviation, while independent dropout uses more hyperparameters to obtain its advantage.

The comparison uses ten noiseless simulation runs rather than noisy quantum hardware. It supports quantum dropout as a regularizer for this deliberately small classification problem, not a general claim of quantum advantage.

# References

[[2023 - A General Approach to Dropout in Quantum Neural Networks.pdf]]
