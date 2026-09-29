# Web Image Performance

Parent topic: [[Web Performance and Scalability]]

Web Image Performance is the chapter-level topic for representing, compressing, loading, selecting, decoding, delivering, and operationalizing images for fast web experiences. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

Web image performance is the discipline of preserving the communicative value of imagery while controlling its costs across the network, browser, device, and production system. An image that looks small in a layout may still contain millions of samples, expensive metadata, or a format that the client cannot decode efficiently. Optimization therefore begins before a request is made and continues through loading, rendering, caching, and the generation of future variants.

[[Digital Image Representation and Quality]] supplies the vocabulary for those decisions. Pixels are samples rather than continuous reality, channels encode color and transparency, and color spaces separate or combine information in different ways. Compression works because neighboring samples and transformed coefficients contain predictable structure. Objective metrics such as PSNR and SSIM can compare versions, but perceptual measures are valuable because equal numerical error does not always produce equal visible error. The format decision is consequently a choice about the kind of information that can be discarded, reconstructed, or preserved.

[[Lossless Web Image Formats]] examines GIF and PNG as structured containers rather than interchangeable “small image” choices. GIF organizes indexed-color frames and can animate them, but its palette and one-bit transparency constrain fidelity. PNG uses typed chunks, scanline prediction filters, optional interlacing, and full alpha transparency. Knowing these mechanics makes optimization concrete: palette size, filter choice, ancillary data, and interlacing all affect bytes without changing the intended pixels.

Photographic compression receives deeper treatment in [[JPEG Encoding and Optimization]]. JPEG separates luminance from chrominance, may subsample color, transforms 8-by-8 blocks into frequencies, quantizes those coefficients, and entropy-encodes the result. Quantization is the irreversible step; marker arrangement, metadata removal, scan design, and entropy coding can be optimized without another round of pixel loss. Progressive scans can reveal a coarse whole image early, while specialized encoders can spend more computation to find smaller representations.

[[Modern Web Image Formats]] shows how WebP, JPEG XR, and JPEG 2000 extended the design space with prediction, wavelets, alpha support, lossless modes, and stronger entropy coding. Their compression benefits matter only when the client can decode the selected representation. Capability negotiation and fallback are therefore part of the format decision, not an afterthought.

For resolution-independent graphics, [[SVG Authoring and Optimization]] represents shapes, paths, groups, transforms, and filter graphs as document structure. The viewport and `viewBox` relate internal coordinates to display dimensions. Because SVG is text and structure, its performance depends on reducing unnecessary precision and complexity, reusing groups, avoiding expensive effects, and applying general-purpose compression.

Once an asset exists, [[Browser Image Loading]] explains when the browser discovers it. HTML images are often found during speculative parsing, while CSS backgrounds wait for stylesheet and style resolution. The preloader, connection limits, protocol priorities, and service workers all affect when bytes arrive. Images usually do not block page rendering, but they still compete with resources that do.

[[Image Lazy Loading]] deliberately delays requests that are unlikely to become visible. That can eliminate waste below the fold, but it also bypasses or postpones the browser’s early discovery machinery. Viewport observation, thresholds, fallbacks, placeholders, and explicit eager treatment for critical images are needed to balance bandwidth savings against late or jarring presentation.

Network completion is not the end of the cost. [[Browser Image Decoding and Memory]] covers the CPU work of turning compressed bytes into pixels and the memory required to retain those pixels. Displaying an oversized source can waste decode time and decoded storage even when the transfer was well compressed. Memory pressure can evict decoded images and force later work to repeat; GPU paths and subsampled color storage can mitigate some of that cost.

[[Image Request Consolidation]] addresses the opposite scale problem: many tiny assets whose headers, cache records, and scheduling overhead outweigh their payloads. Raster sprites, data URIs, icon fonts, and SVG symbol collections trade request count against cacheability, decoding scope, maintainability, and compatibility. Consolidation works best when assets with similar lifetimes and change rates are grouped together.

Device diversity is handled first in markup through [[Responsive Image Selection]]. Density and width descriptors give the browser candidates, the `sizes` attribute describes expected layout width, and `picture` supplies ordered sources for art direction or format fallback. These mechanisms let the browser choose before downloading instead of fetching a desktop asset and hiding or shrinking it afterward.

Server-side adaptation expands those choices in [[Adaptive Image Delivery and Caching]]. Client hints communicate viewport, density, resource width, network conditions, and data-saving preference. Responses must describe how they vary so shared caches remain correct, yet too many variation dimensions can fragment a CDN cache. Breakpoint budgets, quality tiers, URL design, protocol behavior, and intermediary controls must be designed as one delivery policy.

Finally, [[Image Derivative Workflows]] turns all of these techniques into a repeatable system. A controlled master feeds normalized derivatives whose size, crop, format, metadata, and watermark rules are explicit. Static build pipelines suit bounded libraries; dynamic image servers suit large or rapidly changing collections but introduce fetch latency, decode memory, encoder throughput, caching, and security concerns. The strongest workflow treats performance, visual quality, operations, privacy, and sandboxing as parts of the same lifecycle rather than isolated optimizations.

Together, these topics show why “make the file smaller” is necessary but incomplete. A high-performance image is appropriate to its content, selected for the receiving context, discovered at the right time, decoded within device limits, cached at the right granularity, and generated by a system whose variants remain manageable and secure.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Web Image Performance]]"
```
