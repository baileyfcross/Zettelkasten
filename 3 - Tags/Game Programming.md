# Game Programming

Parent topic: [[Computer Science]]

Game Programming is the implementation-focused chapter for the real-time systems that turn game rules, content, and player actions into a running interactive program. Full Notes should use one of the focused topics below instead of this chapter tag.

## Overview Chapter

Game programming coordinates many systems that must agree on time, state, space, input, presentation, and communication while meeting the strict responsiveness expected of interactive software. A running game repeatedly accepts player and network input, advances a simulated world, and generates visual and audio output. Each stage depends on representations and algorithms from the other stages, so the programmer's central task is not merely to implement isolated features but to preserve coherent behavior across the whole frame.

[[Game Loop and Object Architecture]] provides the execution backbone. The game loop measures elapsed real time, converts it into game time, processes input, updates world objects, generates output, and optionally limits the frame rate. Delta time makes movement independent of rendering speed, while a game-time factor can pause or scale simulation time. Updateable and drawable object interfaces let the world maintain explicit registries of objects that participate in each phase without forcing every object into the same behavior.

[[2D Game Rendering]] explains how a two-dimensional scene reaches the display. Double buffering separates drawing from presentation so the viewer does not see a partially rendered frame, while synchronization with the vertical blank interval reduces tearing. Sprites, sprite sheets, animation frames, painter-order drawing, scrolling backgrounds, and tile maps provide compact ways to assemble and move large scenes from reusable images.

[[Game Linear Algebra]] supplies the spatial vocabulary shared by graphics, physics, cameras, and AI. Vectors represent positions, directions, and displacements. Norms, normalization, dot and cross products, projection, reflection, and interpolation answer recurring geometric questions. Transformation matrices combine scale, rotation, and translation, and matrix concatenation expresses several changes of coordinate space as one ordered operation.

[[3D Game Rendering]] follows an object through the rendering pipeline. Model-space vertices are placed into world space, transformed relative to the camera, projected, and mapped to screen coordinates. Point and directional lights contribute differently to surface illumination, while a reflection model combines ambient, diffuse, and specular terms. Depth buffering resolves visibility at the pixel level, and quaternions provide a compact, stable representation for object rotation before a world transform is sent to the renderer.

[[Game Input Systems]] converts hardware state into meaningful player action. Digital controls require transitions such as just pressed and just released, not merely an on-or-off value. Analog controls need dead zones and filtering to suppress noise. Chords and sequences recognize combinations over time, while event-based systems decouple device details from gameplay commands. Touch gestures, accelerometers, and gyroscopes extend the same abstraction to mobile and spatial devices.

[[Game Audio Programming]] treats sound as both a sampled signal and a spatial event. Frequency and amplitude shape pitch and loudness, while sampling turns a waveform into digital data. Sound cues attach playback rules and metadata to assets. In three-dimensional audio, listeners and emitters establish relative position; attenuation, stereo panning, reverb, occlusion, and obstruction then make playback respond to distance, direction, environment, and intervening geometry.

[[Game Physics and Collision]] replaces complex visible models with collision geometry that is inexpensive to test. Bounding spheres and boxes offer different tradeoffs between fit and computation. Rays and line segments support queries such as visibility and picking. Instantaneous tests examine one moment, whereas continuous techniques such as swept-sphere collision account for motion between frames. Linear mechanics and numerical integration then advance position and velocity from forces and acceleration using a stable time step.

[[Game Camera Systems]] turns world geometry into a controlled point of view. First-person, follow, spring-follow, orbit, and spline cameras store and update their targets differently because they serve different play and presentation goals. Field of view and projection establish the visible volume. Collision handling keeps the camera from passing through or being blocked by scenery, while unprojection converts screen positions back into world-space rays for object picking.

[[Game Artificial Intelligence]] aims for behavior that appears purposeful within the constraints of play. Pathfinding represents traversable space as a graph, grid, path-node network, or navigation mesh and commonly applies A-star search with an admissible heuristic. State machines organize local behavior, and the State pattern makes transitions easier to maintain. Fuzzy states permit blended behavior, while strategy and planning operate over longer horizons and groups of agents.

[[Game User Interface Programming]] organizes menus and heads-up information as interactive software rather than static artwork. Menu state machines, screen stacks, button states, and transitions govern navigation. Reticles, radar displays, and waypoint indicators translate world or player information into useful screen-space cues. Coordinate conversion, localization, and middleware help the same interface adapt to different resolutions, languages, workflows, and content iterations.

[[Game Scripting and Data Formats]] separates frequently changed behavior and content from lower-level engine code. Embedded or custom languages can improve iteration speed and let designers author gameplay, while visual scripting exposes operations as connected elements. A script implementation still requires tokens, syntax, representations, and execution. Text formats are readable and diff-friendly; binary formats are compact and efficient. Data-driven add-on systems combine scripts with declarative files while protecting privileged engine operations.

[[Networked Game Programming]] extends state beyond one process. Internet Protocol routes packets, ports identify endpoints, and sockets expose transport services to the game. TCP provides ordered reliable streams, whereas UDP avoids connection and retransmission overhead when current state matters more than old packets. Client-server and peer-to-peer topologies assign authority differently. Synchronization, validation, encryption, and cheat countermeasures preserve a playable shared state across delay, loss, and hostile clients.

[[C++ Game Engine Architecture]] organizes that work into durable runtime objects. A central game class owns subsystem initialization, loading, input, updating, rendering, and shutdown. Actors provide world identity and transforms, while components add movement, input, rendering, audio, or collision behavior without creating an unwieldy inheritance tree. Explicit update order and deferred removal protect iteration from structural changes, and resource caches keep shared assets from being loaded repeatedly.

[[OpenGL Rendering Pipeline]] follows data from engine memory to the graphics processor. An OpenGL context owns rendering state; vertex and index buffers describe reusable geometry; a vertex array captures how buffer bytes become attributes. Vertex and fragment shaders transform geometry and determine pixel color after they are compiled and linked into a program. Textures, coordinates, blending, and mesh-rendering components connect authored assets to those GPU operations.

[[Skeletal Animation Systems]] lets a deformable character move through a hierarchy of rigid bones. Local poses are composed through parent relationships to produce global transforms. The inverse bind pose brings a bind-space vertex into a bone's coordinates, while an animated pose returns it to its current location. Skin weights blend several bone contributions, and a matrix palette lets a vertex shader deform many vertices efficiently for each sampled animation clip.

[[Advanced Real-Time Rendering]] improves quality and supports multi-pass effects. Nearest and bilinear filtering answer how texels become pixels; mipmaps and anisotropic filtering address minification and oblique surfaces. Rendering into framebuffer-attached textures makes mirrors and other off-screen views possible. Deferred shading first records surface properties in a G-buffer, then evaluates lighting in screen space, trading memory and transparency complexity for efficient scenes with many lights.

[[Game Asset and Level Serialization]] moves an authored world across the boundary between files and runtime objects. A level schema records global settings, actors, components, types, and properties. Loading dispatches type names to construction functions and then applies properties through virtual hooks; saving walks the same object graph in reverse. Text formats such as JSON favor inspection and revision, while binary mesh layouts favor compact size and direct loading when their header and field order are controlled.

Together these topics form a dependency chain rather than a set of independent specialties. Timing drives physics and animation; linear algebra connects rendering, cameras, collision, audio, and pathfinding; input and networking introduce events that change shared state; scripting and data formats make that state authorable; interfaces make it legible. A robust game architecture keeps those connections explicit so each system can evolve without hiding assumptions about coordinate space, update order, authority, or time.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Game Programming]]"
```
