2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity MonoBehaviour

Unity MonoBehaviour is the base class used for scripts that become components on GameObjects and participate in Unity's event-driven lifecycle. Inheriting from it gives a script access to its GameObject, transform, component lookup, coroutine support, and recognized callback methods.

A MonoBehaviour is not executed like an ordinary program with one explicit main routine. Unity invokes its callbacks according to object state and engine phases. This inversion of control makes [[Unity Lifecycle Methods]] and dependencies among scripts part of the program's architecture.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

