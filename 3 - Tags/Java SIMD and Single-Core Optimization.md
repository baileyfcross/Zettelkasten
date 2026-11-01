# Java SIMD and Single-Core Optimization

Parent topic: [[Java Programming Language]]

Java SIMD and Single-Core Optimization is the chapter-level topic for portable vector programming, masked data movement, reductions and scans, numerical accuracy, algorithm reformulation, and measurement-guided single-core performance engineering. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

### Portable SIMD begins with a semantic contract

[[Java SIMD Foundations and Hardware Portability]] starts from data-level parallelism: one operation is applied to several independent primitive values held in hardware lanes. The Java Vector API exposes that computation through vectors and species rather than binding source code directly to x86 SSE, AVX, or AVX-512 instructions, ARM NEON or SVE, or the RISC-V vector extension. A species determines the element type and requested shape, while the lane count follows from vector width divided by element width.

Portability does not mean identical machine code or identical speed. A fixed 128-bit species favors predictability and broad support, a wider fixed species can target known hardware, and a preferred species asks the runtime for an appropriate width. Vector-length-agnostic code must therefore derive loop strides, masks, and transformations from the chosen species instead of assuming a constant number of lanes. When the requested shape cannot be accelerated, the runtime can preserve semantics through scalarized execution. That graceful degradation protects correctness but can make an explicit vector implementation slower than a well-optimized scalar loop, so portability and performance must be evaluated separately.

### Masks and data movement express selection without scalar branches

[[Java Vector Masks and Data Movement]] describes how the API moves and rearranges values when straightforward lane-wise arithmetic is insufficient. A mask identifies active lanes. A masked operation changes only selected lanes, while a blend selects values from two vectors according to the mask. These operations translate per-element conditions into bulk data flow and let all lanes follow one instruction stream.

Slice carries neighboring data across a vector boundary, shuffle and rearrange permute lanes, and zip or unzip patterns transpose groups of vectors. Compress packs selected lanes at the beginning of a vector; expand performs the inverse placement into masked positions. Gather loads values from indexed addresses and scatter writes them back. The latter operations are powerful but irregular: repeated scatter indices can conflict, unused addresses can create holes, and both indexed loads and stores may serialize memory traffic. A vector algorithm should prefer sequential memory access and ordinary lane operations when they express the same computation.

### Reductions and scans connect lanes at a cost

[[SIMD Reductions and Scan Algorithms]] distinguishes vertical operations, which act independently at corresponding lane positions, from horizontal operations that combine or exchange values within a vector. A reduction collapses lanes to one scalar. Repeated reduction inside a loop is usually expensive, so partial results should stay in vector accumulators and cross lanes only after the bulk traversal when the algorithm permits it.

A scan produces every cumulative result rather than only the final reduction. Inclusive and exclusive forms differ in whether the current element participates, while prefix and suffix forms differ in traversal direction. A shift-combine vector scan completes in logarithmic stages for an associative operation, but its stages form a dependency chain and perform unused element work. Carrying the last local result into the next vector preserves continuity across blocks. Blelloch's upsweep and downsweep reduce total work, and transposition can turn several scans into fully occupied lane-wise operations, but shuffles and register pressure can erase the theoretical benefit. Scans are often valuable as building blocks even when the isolated scan loses to scalar code.

### Floating-point vectorization changes the order of error

[[SIMD Numerical Accuracy and Statistics]] treats numerical equivalence as a design concern. Floating-point values have finite significands, so a small addend can disappear beside a much larger running sum. Sequential and pairwise summation create different dependency trees and therefore different rounding results. Kahan compensation records low-order information lost by addition, improving accuracy at the cost of more dependent arithmetic. A vector Kahan implementation maintains one sum and correction per lane before the final reduction.

Vector width also changes how inputs are partitioned among partial accumulators. Correct implementations can consequently return slightly different results at different widths even when every lane performs the intended operations. Mean and standard-deviation kernels expose the broader tradeoff: a two-pass centered calculation uses more memory traffic, while a one-pass formula based on the sum and sum of squares can lose precision through cancellation. The acceptable approach depends on the application's error contract, not merely on which loop is shorter.

### Reformulation determines whether parallel lanes have useful work

[[SIMD Algorithm Reformulation Patterns]] moves beyond transliterating scalar control flow. Structure-of-arrays layout places corresponding fields contiguously, avoiding the gathers that an array of structures may require. Linear recurrences can sometimes become products of small transition matrices, allowing several positions to be generated together. A conditional can be computed as two alternatives followed by a mask blend, while residue-class lookahead can replace several irregular iterations with a table-selected affine transformation.

The same principles support compacting unique values, rejecting biased random candidates, and rewriting the maximum-subarray problem as scans over prefix sums and prefix minima. Divergent workloads remain difficult because lanes finish at different times. Work piling fills completed lanes with new tasks, whereas memoization may eliminate far more work by reusing previously computed suffixes. The book's Collatz case demonstrates that combining every optimization can be slower than simple memoization when additional gather, scatter, compress, and expand operations dominate. Algorithmic simplification should precede vectorization.

### Measurements arbitrate between elegant transformations

[[Java SIMD Performance Engineering]] supplies the final discipline. Data-level parallelism operates across lanes, while instruction-level parallelism lets a superscalar core overlap independent instructions. Dependency chains prevent overlap. Loop unrolling exposes independent streams, but identical streams can compete for the same execution units; an asymmetric schedule can interleave different operations to reduce that structural hazard. Excessive unrolling consumes registers and can spill temporary values into memory.

The JVM adds another layer. Tiered execution begins with interpretation, moves through quickly compiled and profiled code, and may reach a more optimizing compiler. Generated assembly can reveal strength reduction, vector instructions, masks, safepoint checks, or scalar fallback that source inspection alone cannot prove. Microbenchmarks must warm the JIT, isolate single-core work, compare against a meaningful scalar baseline, and run on the hardware families the code is meant to support. A speedup on one AVX-512 processor does not establish a portable improvement on AVX2, NEON, or SVE. The reliable optimization loop is therefore: identify a bottleneck, reformulate it, inspect what the runtime produced, benchmark across relevant machines, verify numerical and functional correctness, and keep the simplest version that satisfies the measured goal.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Java SIMD and Single-Core Optimization]]"
```
