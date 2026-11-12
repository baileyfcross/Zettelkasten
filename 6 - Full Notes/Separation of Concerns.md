2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]] [[Software Design Principles]]

# Separation of Concerns

Separation of concerns assigns different responsibilities to different parts of a system so each can change without carrying unrelated duties. A full-stack application separates persistence entities, API output, client communication, and presentation even when their data initially looks similar.

An [[Entity Framework Core Entity]] should model stored state, while a [[Data Transfer Object]] exposes the controlled shape needed by the client. An [[Angular Service]] handles reusable communication so an [[Angular Component]] can focus on interface state.

The current source generalizes this boundary beyond a web stack. Separating concerns makes a design modular when each part owns a coherent responsibility and presents an interface that prevents unrelated changes from spreading through the rest of the program.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
