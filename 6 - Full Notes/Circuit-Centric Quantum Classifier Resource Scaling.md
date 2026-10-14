2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Circuit-Centric Quantum Classifier Resource Scaling

For an $N$-feature input and a degree-$d$ tensorial map, the circuit-centric classifier uses $d\lceil\log_2 N\rceil$ data qubits plus one ancilla during gradient estimation. A model with $K$ entangling blocks has a number of parameterized gates polynomial in the qubit count, making the trainable circuit polylogarithmic in $N$ when $d$ and $K$ remain controlled.

General [[Amplitude Encoding for Circuit-Centric Classification|amplitude state preparation]] is the main depth bottleneck. Preparing an arbitrary $N$-component state can require on the order of $N$ gates, so the compact model circuit does not by itself produce a polylogarithmic end-to-end algorithm. Structured, approximately factorizable, or natively quantum inputs are the cases in which data loading may be cheaper.

Readout adds a sampling cost. Directly estimating the measured probability to additive error $\epsilon$ requires a number of repetitions scaling as $O(\operatorname{Var}(Z)/\epsilon^2)$. Amplitude estimation can improve this to $O(1/\epsilon)$ repetitions, but it increases circuit depth by a corresponding factor and is less suited to the low-depth design goal.

The width-depth tradeoff appears across encoding choices. Product encoding uses one shallow rotation and one qubit per feature; amplitude-style encodings use logarithmically many qubits but can need exponentially deep exact preparation; data re-uploading can distribute the cost between width and depth but still needs enough free parameters to distinguish points in the original feature space. [[Sparse Staircase Quantum Image Encoding Ansatz|structure-aware approximate encoders]] reduce constants and compilation depth without removing the classical optimization and per-input preparation costs.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
