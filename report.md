# Comparison of Naive RAG and Parent-Child Retrieval

## Introduction
This report compares two retrieval approaches used in RAG systems: Naive RAG and Parent-Child Retrieval.

## Naive RAG
- Uses fixed-size chunks stored in a vector database.
- Retrieves top-k similar chunks directly for generation.
- Simple to implement, but may lose broader context.

## Parent-Child Retrieval
- Retrieves small child chunks for precise matching.
- Expands them to larger parent chunks for richer context.
- Improves contextual integrity and supports more complex queries.

## Comparison
| Aspect | Naive RAG | Parent-Child Retrieval |
|---|---|---|
| Simplicity | High | Medium |
| Context quality | Lower | Higher |
| Retrieval precision | Basic | Better |
| Best for | Simple Q&A | Complex reasoning |

## Conclusion
Naive RAG is a good baseline, while Parent-Child Retrieval is more suitable for tasks where preserving context is important.
