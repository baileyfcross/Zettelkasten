2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Single-Qubit Re-Uploading Classifier Benchmark

The hardware study trains on 200 randomly sampled points and evaluates 1,000 unseen points for synthetic binary and multiclass geometries. Four-layer circuits address circles, crowns, nonconvex curves, spheres, hyperspheres, tricrowns, nested circles, squares, and wavy boundaries; quantum measurements use 100 repetitions and have a reported accuracy uncertainty of $\pm2$ percentage points.

Before device fine-tuning, experimental accuracies range from 64 percent for the hypersphere to 93 percent for the circle and squares. Exact circuit simulations range from 74 to 97 percent. The device is usually a few points below simulation, although the tricrown experiment reaches 95 percent versus 91 percent in simulation; only the circle and hypersphere receive the second hardware-optimization stage.

Single-hidden-layer neural networks and support-vector machines provide classical comparisons, with their best tested configurations generally matching or exceeding the quantum scores. The experiment demonstrates that one trapped ion can execute varied nonlinear and multiclass tasks with performance close to its own simulation. It does not establish quantum advantage, scaling superiority, or competitive performance on natural high-dimensional datasets.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
