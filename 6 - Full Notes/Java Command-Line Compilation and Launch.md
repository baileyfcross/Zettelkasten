2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Command-Line Compilation and Launch

The `javac` command transforms `.java` source files into `.class` bytecode files, and the `java` command launches a class containing an accepted main entry point. Package names affect both the source declaration and the directory or class name used at launch, so compilation output must preserve that namespace structure.

Command-line execution exposes the boundary that an IDE normally automates: source paths, output directories, classpaths or module paths, VM options, program arguments, and the selected JDK all participate in the result. An IDE run configuration is therefore a stored form of these launch decisions.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
