# Kotlin Programming Language

Parent topic: [[Software Engineering]]

Kotlin Programming Language is the chapter-level topic for Kotlin syntax, object-oriented design, functional techniques, collections, asynchronous and reactive programming, testing, domain-specific languages, data work, APIs, and multiplatform development. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

### A concise language with explicit safety boundaries

Kotlin programs begin with the declarations, expressions, and control structures gathered in [[Kotlin Syntax Types and Control Flow]]. A value declared with `val` cannot be reassigned, while `var` names mutable state. Type inference can remove repeated type names without making a declaration dynamically typed. Basic numeric, character, Boolean, and string values remain subject to their declared types, and explicit conversions make changes of representation visible. String templates place values or expressions inside text, arrays provide indexed fixed-size storage, and operators express arithmetic, comparison, Boolean logic, membership, ranges, and other relationships.

Kotlin treats several familiar control structures as expressions. An `if` or `when` branch can therefore select a value as well as choose an action. Loops traverse ranges, arrays, and collections, while `break`, `continue`, and `return` alter the surrounding flow. Type checks with `is` can enable a smart cast when the compiler can prove that the checked value has not changed. Exception handling adds another expression-oriented boundary: a `try` and its `catch` clauses can produce a result, `finally` supplies work that runs regardless of the selected path, and `throw` transfers an exceptional condition to a handler.

### Types that organize state and behavior

[[Kotlin Object-Oriented Type Design]] develops programs from classes and objects. A class defines properties and functions, and each object is an instance with its own state. Nested classes are separated from an outer instance, whereas an `inner` class can reach that instance. Primary constructors place the main construction contract in the class header and can cooperate with `init` blocks; secondary constructors provide alternate entry points and delegate through `this` when required.

Inheritance is deliberately visible. A superclass or member must be marked `open` before ordinary subclassing or overriding, and a replacement member uses `override`. Interfaces specify capabilities and may supply default behavior, while visibility modifiers set the boundary around declarations. Properties expose generated or custom accessors instead of requiring callers to manipulate backing state directly. Kotlin also supplies purpose-shaped class forms: abstract classes leave behavior for descendants, data classes generate common value-oriented operations, sealed classes bound a hierarchy for exhaustive reasoning, and enum classes define a fixed family of named instances.

### Functions, absent values, and reusable behavior

In [[Kotlin Functions Null Safety and Delegation]], a function has a name, typed parameters, an optional return type, and a body. Default and named arguments make selected call sites clearer without multiplying overloads. Recursion expresses a problem through smaller calls, and a suitable `tailrec` function puts its recursive call in tail position so the compiler can optimize the repeated step.

Functions can also be values. A higher-order function accepts or returns another function, while a lambda provides an unnamed behavior that collection operations and other APIs can consume. Extension functions make an operation callable with receiver syntax without changing the receiver's class. These mechanisms support Kotlin's functional style without removing its static type system.

Nullability makes the possibility of absence part of a type. Safe calls propagate `null`, the Elvis operator supplies an alternative, safe casts return `null` on failure, and non-null assertions deliberately accept the risk of an exception. Scope functions such as `let` can confine work to a non-null receiver. Lazy initialization defers construction until first access, and delegated properties transfer accessor behavior to another object. Together these facilities make initialization and absence explicit design choices instead of hidden assumptions.

### Collections, library operations, and files

[[Kotlin Collections Standard Library and File I-O]] organizes groups of values through lists, sets, and maps. Lists preserve an ordered sequence, sets emphasize distinct membership, and maps associate keys with values. Kotlin distinguishes read-only collection interfaces from mutable variants, while generics preserve the element type across reusable containers and algorithms.

The standard library turns collections into transformation pipelines. Filtering retains elements that satisfy a predicate, mapping transforms elements, and sorting produces an order from natural values or a selector. String operations expose common inspection and transformation tasks, and extension functions allow similarly shaped APIs to be added to existing types. File functions create, read, write, append, and delete local data; because those operations cross a system boundary, their paths, encodings, failures, and lifetimes remain part of the program's contract.

### Concurrent work, streams, and executable evidence

[[Kotlin Coroutines Reactive and Testing]] connects nonblocking work to verification. A coroutine can suspend without permanently occupying its current thread. Builders such as `launch` start work within a scope, `delay` suspends it, and `runBlocking` bridges ordinary code to a coroutine context. Structured concurrency ties child work to a scope so completion, cancellation, and failure have a visible owner. Jobs expose lifecycle and joining, while coroutine exception handlers and cancellation rules determine how failures move through the hierarchy.

Reactive programming represents changing values as observable streams. RxKotlin supplies Kotlin-oriented access to RxJava, with observable sequences that may be cold—producing values for each subscription—or hot—sharing an ongoing source. Operators filter, remove duplicates, or create timed emissions before subscribers handle values, completion, and errors. Coroutines and reactive streams solve related asynchronous problems with different control models, so the boundary between them should remain explicit.

Tests make those contracts executable. Unit tests isolate a small behavior and compare its result with an expectation. MockK creates controlled test doubles and verifies interactions when a dependency must be isolated. Integration tests assemble more of the system, such as a Ktor application and its routes, to verify that components cooperate through their real framework boundary.

### Domain vocabularies, data exploration, APIs, and shared platforms

[[Kotlin DSL Data and Multiplatform Applications]] shows Kotlin acting beyond ordinary application syntax. An internal domain-specific language uses Kotlin features—especially lambdas with receivers, extension functions, builders, and `apply`—to express a constrained domain in readable form. A type-safe builder collects configuration before constructing a value, and `@DslMarker` prevents an inner receiver from accidentally modifying an outer one.

The language also serves application integration and exploratory data work. Kotlin APIs reach Android, networking, storage, graphics, machine learning, IoT, multimedia, cloud, and backend systems. The book's Google Maps and MQTT cases illustrate that using an API includes dependency setup, permissions or connectivity, callbacks, and lifecycle handling rather than merely calling one function. Kotlin Notebook provides executable cells for exploration; DataFrame can load structured sources; and Kandy constructs visualizations from that data.

Kotlin Multiplatform moves selected logic into common source sets while platform source sets retain code that depends on Android, iOS, web, desktop, or server facilities. A shared module can feed more than one client artifact, and multiplatform dependencies must declare which source set and target they support. The aim is not to erase platform differences, but to make the reusable boundary explicit enough that common logic and native integration can evolve together.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Kotlin Programming Language]]"
```
