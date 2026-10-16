2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# QLSTM Sentiment Training Behavior

On the low-complexity financial sentences, both the classical LSTM and QLSTM learn within 20 epochs and reach validation accuracy above 80%. On the moderate-complexity data, the QLSTM remains near its initial performance for about 100 epochs before clear learning begins, and the simulated run takes roughly ten hours on the study's small cloud-compute setup.

During hyperparameter exploration, the delayed progress is strongly associated with increasing the number of ansatz layers. The authors interpret this as a possible barren-plateau effect because deeper parameterized circuits introduce more trainable parameters, but the experiment does not measure gradient concentration and therefore does not establish that mechanism.

The result is best read as a time-quality tradeoff under a particular [[QLSTM Variational Subnetwork Ansatz]]. More expressive circuits may improve the model while making classical simulation and optimization substantially slower.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
