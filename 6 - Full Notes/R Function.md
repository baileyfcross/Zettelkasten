2026-09-16 00:09

Status: #baby

Tags: [[R Function Design]] · [[R Scripts Functions and Debugging]] · [[R Programming Environment]]

# R Function

An R function packages a sequence of operations behind a named interface and returns a result. Functions reduce duplication, clarify intent, and let the same logic operate on different data through arguments.

A well-designed function limits hidden dependencies and documents the inputs, output, and important side effects.

The book builds a function by assigning `function(...)` to a descriptive name, placing the calculation inside braces, and returning the intended object. Once the definition script is executed, the function can be called repeatedly from the console or composed inside larger scripts.

An R function returns the value of its final evaluated expression unless an explicit return is used. Lexical scoping lets it resolve names in its defining environment, so reusable functions should prefer explicit arguments over accidental dependence on workspace objects.

# References

[[essentialsofdatascience.pdf]]

[[rstudentcompanion.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
