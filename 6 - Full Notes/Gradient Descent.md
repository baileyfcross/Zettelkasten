2026-09-06 22:42

Status: #baby

Tags: [[Parallel Neural Network Training]]

# Gradient Descent

Gradient descent updates model parameters in the direction that locally reduces a loss function. Backpropagation calculates the required derivatives for a neural network, while the learning rate determines the size of the update.

Parallel training can accelerate gradient calculation, but workers must coordinate parameter values and combine their contributions without introducing excessive communication.

# References

[[bigdatamanagementandprocessing.pdf]]
