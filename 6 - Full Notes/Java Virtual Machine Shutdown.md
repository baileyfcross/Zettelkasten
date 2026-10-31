2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java Virtual Machine Shutdown

`System.exit(status)` begins the JVM shutdown sequence and supplies an integer result to the environment that launched the process. By convention, zero represents normal completion and a nonzero status identifies abnormal termination.

At shutdown, registered shutdown hooks start in an unspecified order. The virtual machine terminates after those hooks have finished. Named status constants make distinct exit reasons clearer than repeating unexplained integer literals at several termination points.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
