2026-09-06 22:42

Status: #baby

Tags: [[Parallel Neural Network Training]]

# Gradient Descent

Gradient descent updates model parameters in the direction that locally reduces a loss function. Backpropagation calculates the required derivatives for a neural network, while the learning rate determines the size of the update.

Parallel training can accelerate gradient calculation, but workers must coordinate parameter values and combine their contributions without introducing excessive communication.

Kelleher pictures each parameter combination as a point in [[Model Weight Space|weight space]] with an elevation given by a [[Loss Function|loss]]. Repeated updates follow local slopes downhill, and the [[Learning Rate]] scales each step. Squared error for a simple linear model yields a convex bowl in his example, whereas a nonlinear neural network has a more complicated surface with multiple valleys. A useful training run therefore need not find a global minimum, and runs from different starts may explore different parts of the landscape. Large datasets can also be split into batches instead of using every example for each update.

# References

[[bigdatamanagementandprocessing.pdf]]

[[deeplearning_mit.epub]]
