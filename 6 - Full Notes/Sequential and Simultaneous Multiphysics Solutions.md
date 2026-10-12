2026-09-14 00:55

Status: #baby

Tags: [[Conjugate Heat Transfer Systems]]

# Sequential and Simultaneous Multiphysics Solutions

In a sequential multiphysics solution, one physics is solved first and its field is passed as input to another. This can reduce the size of each solve and is appropriate when feedback from the later physics to the earlier one is negligible.

A simultaneous solution assembles interdependent fields so they converge together. It is needed when fluid motion changes temperature and temperature also changes the flow, as in [[Nonisothermal Flow|nonisothermal systems]], but the tighter coupling can demand better initial states and solver control.

# References

[[cosmolheattransfermodels.pdf]]

