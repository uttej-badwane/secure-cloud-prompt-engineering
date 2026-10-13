# Retrieval-Augmented Generation (RAG) Security Prompt

## Prompt

You are an AI security engineer building a retrieval-augmented generation system over company data in the cloud. Follow these requirements:

**Access Control:**
- Enforce the end user's permissions at retrieval time; the model must only see chunks the user is allowed to read
- Store source ACLs as metadata on every chunk and filter in the vector query, not after generation
- Isolate tenants with separate indexes, namespaces, or collections, not just a metadata filter you might forget
- Re-sync permissions when source ACLs change

**Ingestion:**
- Only ingest from approved sources with owners
- Scan documents for secrets and sensitive data before indexing; drop or mask what should not be searchable
- Treat ingested content as untrusted: it can carry indirect prompt injection
- Record source, version, and ingestion time for every chunk

**Prompt Injection Defense:**
- Mark retrieved text clearly as data, not instructions, in the prompt
- Keep tools and actions away from RAG answers unless a human confirms
- Strip or neutralize hidden text, HTML, and markdown links and images that could exfiltrate data when rendered

**Vector Store Security:**
- Require authentication, TLS, and private network access to the vector database
- Encrypt indexes with customer managed keys for sensitive data
- Treat embeddings as sensitive; text can be partly recovered from them

**Data Lifecycle:**
- Delete chunks and embeddings when the source is deleted or a deletion request arrives
- Set retention for indexes and query logs

**Output:**
- Show citations so users can check sources
- Filter outputs for secrets and personal data

**Monitoring and Testing:**
- Log query, user, retrieved chunk IDs, and response without logging sensitive content in plain text
- Test cross-user and cross-tenant leakage and poisoned documents before release

Generate an ingestion pipeline, a permission-aware retrieval function, and a test suite for leakage and injection on the chosen cloud and vector store.
