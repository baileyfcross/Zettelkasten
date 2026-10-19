2026-10-18 23:53

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# Persistent Chat Memory with MapDB

The source demonstrates a LangChain4j chat-memory store backed by MapDB so conversation messages survive application restarts. The store maps a memory identifier to serialized messages and supports retrieving, replacing, or deleting the conversation state expected by the framework.

Persistence changes the operational boundary of chat history. The application must protect the database, isolate users, handle incompatible serialization changes, and apply retention rules because prompts and responses may contain sensitive data.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
