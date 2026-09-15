2026-09-05 16:28

Status: #baby

Tags: [[Recurrent Sequence Architecture]]

# Long Short-Term Memory

Long short-term memory is a recurrent neural architecture whose gated memory controls what information is stored, exposed, or forgotten. The gates help useful signals persist across more sequence steps than in a basic [[Recurrent Neural Network]].

LSTM networks became important for speech and language tasks because they can model dependencies that extend beyond adjacent sounds or words.

In Kelleher's account, an [[LSTM Cell State|internal cell state]] is carried forward separately from the immediate hidden output. A [[LSTM Forget Gate|forget gate]] filters previous memory; an [[LSTM Input Gate|input gate]] selects and adds new candidate information; and an [[LSTM Output Gate|output gate]] controls which parts of the updated state are revealed. Each gate uses ordinary neural units, so the LSTM is itself a small network whose controlled memory path reduces the training difficulty of basic recurrence.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
