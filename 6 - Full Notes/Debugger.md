2026-09-06 20:37

Status: #baby

Tags: [[Application Debugging]] [[C Sharp Functions Diagnostics and Testing]]

# Debugger

A debugger runs a program under controlled conditions so a developer can inspect its behavior and changing state. It can pause execution, step through instructions, and display variables, the call stack, and other runtime information.

In a full-stack application, [[Server-Side Debugging]] follows .NET request handling while [[Client-Side Debugging]] follows TypeScript and browser behavior. Both use breakpoints to stop at relevant operations.

Once execution pauses, stepping controls whether the debugger enters a called method, advances over it, or returns to the caller. Locals, watches, and the call stack then connect the current values to the sequence of method calls that produced them.

The software-development source adds that a debugger is strongest when used to test a hypothesis rather than to wander through one execution. Breakpoints, watchpoints, single stepping, and backtraces expose runtime state, but their local view should be combined with reading the surrounding design and reproducing the failure first.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
