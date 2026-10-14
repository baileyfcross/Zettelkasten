2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Circuit-Centric Quantum Classifier Benchmark

The paper classically simulates its circuit-centric classifier on tabulated cancer, sonar, wine, handwritten-digit, and reduced-MNIST datasets. Multiclass tasks are converted to [[One-Versus-Rest Classification|one-versus-rest]] binary problems, and inputs are padded to powers of two, normalized, and—in the MNIST case—coarse-grained to 256 features.

The quantum models use 28 to 124 trainable parameters across the datasets, compared with hundreds to tens of thousands for the tested [[Multilayer Perceptron|multilayer perceptrons]]. Their validation errors are generally comparable to the neural baselines and lower than those of the degree-one and degree-two [[Polynomial Kernel Classifier|polynomial-kernel support-vector machines]], although separately tested degrees six through eight perform better than the reported low-degree SVM baselines.

The classifier overfits the sonar and wine training sets despite its small parameter count, and its test errors are usually worse than the shallow and deep nonlinear perceptrons. Most results average repeated five-fold cross-validation, but the two largest quantum-circuit simulations use only one five-fold run. The benchmark therefore demonstrates parameter efficiency and viable prediction quality in simulation, not speedup, hardware performance, or state-of-the-art accuracy.

A later hardware benchmark uses [[Flexible Representation of Quantum Images|FRQI]] circuits to encode all 70,000 Fashion-MNIST images and trains ten-class variational classifiers in simulation. Noiseless test accuracy rises into roughly the 70-82% range as encoding and classifier depth increase, while an exact-state quadratic-kernel SVM reaches 89.48%. Deployment on ibmq-kolkata reaches only about 40% on the first 100 test images and worsens with deeper circuits. This extends the evidence from small simulations to full-dimensional image encoding, but still supports feasibility rather than competitive accuracy or quantum advantage.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
