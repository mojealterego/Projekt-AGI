# Research protocol v0.1

## Research question
Can a receiver infer a deliberately embedded structural bit after a transformation that preserves the correct answer? Does a canonical representation remove that bit?

## Initial controlled test
Synthetic traces have an identical mathematical answer but differ in order of two independent calculations. The receiver reads ordering; the identity and order-preserving transformations retain it, while canonical sorting removes it.

This is a **software sanity check**, not evidence that LLMs spontaneously learn conceptual steganography. No model is trained or queried.

## Primary measures
- Bit recovery accuracy vs chance 0.5 (balanced synthetic labels)
- Primary answer correctness
- Difference in recovery between transformations

## Threats to validity
Synthetic templates trivially expose ordering; canonicalization may erase legitimate proof dependencies in non-synthetic settings. Real evaluations require independent tasks, human-approved semantic equivalence, multiple seeds, confidence intervals, held-out receivers and pre-registered thresholds.

## Safety
Use synthetic non-sensitive bits, offline traces, no secrets, no exfiltration and no deceptive production agents.
