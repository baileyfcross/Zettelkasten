2026-10-07 17:18

Status: #baby

Tags: [[R Programming Environment]]

# R Method Dispatch

R method dispatch selects an implementation of a [[R Generic Function]] from the classes in the call's signature. Different statistical objects can therefore respond to the same operation with behavior appropriate to their stored data.

In the formal S4 system, setMethod associates a generic name and signature with a method definition. Dispatch allows a base-class interface to remain stable while derived or otherwise distinct classes specialize construction, display, prediction, or summary behavior.

# References

[[statisticalcomputingincplusplusandr.pdf]]
