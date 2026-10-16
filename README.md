# Projekt AGI — Conceptual Steganography Safety Research

Reproducible research on whether structural information survives paraphrasing and whether semantic bottlenecks reduce covert-channel capacity without destroying task correctness.

## Scope
- Controlled synthetic reasoning traces; no claims of model-internal chain-of-thought access.
- Compare identity, lexical paraphrase and canonical semantic bottleneck transformations.
- Quantify payload recovery, task correctness, confidence intervals and failure modes.
- No real-world exfiltration or unauthorized model access.

## Run
```bash
python -m unittest discover -s tests -v
python -m agi_research.experiment --output results/baseline.json
```

See [ROADMAP.md](ROADMAP.md), [docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md) and [docs/GRANT_COMPLIANCE.md](docs/GRANT_COMPLIANCE.md).
