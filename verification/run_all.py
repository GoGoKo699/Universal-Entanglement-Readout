"""Run deterministic scientific checks and compare the committed reference outputs.

No external libraries or network access are used. --record deliberately updates
the expected JSON after a scientifically reviewed change; the default is read-only.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
CHECKS = (
    "verify_corner",
    "verify_outcome_criterion",
    "verify_binary_detector",
    "verify_gap_filter",
    "verify_collective_measurements",
)


def main():
    if not __debug__:
        raise RuntimeError("Run without -O: scientific assertions must be enabled")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true", help="write reviewed expected JSON outputs")
    args = parser.parse_args()
    sys.path.insert(0, str(ROOT))
    results = []
    for name in CHECKS:
        spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
        if spec is None or spec.loader is None:
            raise RuntimeError("Cannot load " + name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        output = module.check()
        if output.get("all_checks_passed") is not True:
            raise AssertionError(name + " did not certify its finite checks")
        target = ROOT / "expected" / (name + ".json")
        if args.record:
            target.parent.mkdir(exist_ok=True)
            target.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        else:
            expected = json.loads(target.read_text(encoding="utf-8"))
            if output != expected:
                raise AssertionError(name + " differs from its committed output; inspect the scientific change")
        results.append({"check": name, "passed": True, "reference": "recorded" if args.record else "matched"})
    print(json.dumps({"all_checks_passed": True, "checks": results}, indent=2))


if __name__ == "__main__":
    main()
