"""Deterministic synthetic structural-channel experiment (not an LLM result)."""
import argparse
import json
from pathlib import Path


def make_trace(bit: int) -> tuple[str, str]:
    if bit not in (0, 1):
        raise ValueError("bit must be 0 or 1")
    steps = ("2+3=5", "4+6=10")
    ordered = steps if bit == 0 else steps[::-1]
    return "; ".join(ordered), "15"


def transform(trace: str, mode: str) -> str:
    steps = trace.split("; ")
    if mode == "identity":
        return trace
    if mode == "paraphrase":
        return " then ".join(steps)
    if mode == "bottleneck":
        return "; ".join(sorted(steps))
    raise ValueError("unsupported mode")


def decode(trace: str) -> int:
    first = trace.split(" then ")[0].split("; ")[0]
    return 0 if first == "2+3=5" else 1


def run(n: int = 100) -> dict:
    if n < 2 or n % 2:
        raise ValueError("n must be even and >= 2")
    results = {}
    for mode in ("identity", "paraphrase", "bottleneck"):
        recovered = 0
        correct = 0
        for i in range(n):
            bit = i % 2
            trace, expected = make_trace(bit)
            output = transform(trace, mode)
            recovered += decode(output) == bit
            correct += sum(int(part.split("=")[-1]) for part in output.replace(" then ", "; ").split("; ")) == int(expected)
        results[mode] = {"bit_recovery_accuracy": recovered / n, "task_accuracy": correct / n, "samples": n}
    return {"experiment": "synthetic_structural_channel", "limitations": "No LLM training, inference or statistical generalization", "results": results}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--output", type=Path, default=Path("results/baseline.json"))
    args = parser.parse_args()
    report = run(args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
