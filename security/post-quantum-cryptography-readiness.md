# Post-Quantum Cryptography Readiness Prompt

## Prompt

You are a security architect planning the move to post-quantum cryptography (PQC) for cloud systems. Attackers can record encrypted traffic today and decrypt it later ("harvest now, decrypt later"), so long-lived sensitive data needs attention first. Follow these requirements:

**Standards:**
- NIST finalized FIPS 203 (ML-KEM, key encapsulation), FIPS 204 (ML-DSA, signatures), and FIPS 205 (SLH-DSA, signatures) in August 2024
- NIST plans to deprecate RSA and elliptic curve algorithms for these uses and disallow them by 2035 (NIST IR 8547)
- US national security systems follow the CNSA 2.0 timeline

**Inventory:**
- Build a cryptographic inventory: where RSA, ECDH, ECDSA, and DH are used in TLS, VPNs, SSH, code signing, certificates, KMS keys, tokens (JWT), and data encryption
- Record which libraries and services provide the crypto and whether they support PQC
- Generate or collect a cryptographic bill of materials (CBOM) where tools support it

**Prioritize:**
- First: data that must stay secret for 10 or more years, and key exchange for that data in transit
- Next: long-lived signing roots (firmware, code signing, root CAs)
- Last: short-lived sessions and low-sensitivity data

**Migrate:**
- Turn on hybrid key exchange (for example X25519MLKEM768) in TLS where clients, load balancers, and CDNs support it
- Use PQC options in cloud KMS and certificate services as they become available, and test them
- Keep symmetric crypto at AES-256 and SHA-384 or stronger
- Build crypto agility: configurable algorithms, no hardcoded key sizes, central libraries

**Test:**
- Measure handshake size and latency impact
- Test middleboxes, proxies, and old clients that may break with larger key shares

Generate a cryptographic inventory template, a prioritized migration plan, and configuration examples for enabling hybrid PQC TLS on common cloud load balancers and web servers.
