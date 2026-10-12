2026-09-06 18:44

Status: #baby

Tags: [[Statistical Computing Workflows]] · [[R Programming Environment]]

# R Object Assignment

R object assignment binds a name to the result of an expression, conventionally with the left-arrow operator `<-`. A frequency table, fitted model, vector, data frame, or function can therefore be preserved as an object and supplied to later operations.

Without assignment, a function commonly prints its result for inspection; with assignment, the same result becomes part of a reproducible workflow. This distinction supports a compositional style in which one operation creates the object consumed by the next.

The book consistently uses assignment to preserve imported data, partition indices, fitted models, predictions, and evaluation objects. Meaningful object names turn an interactive calculation into a sequence whose intermediate state can be examined.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[essentialsofdatascience.pdf]]
