#!/usr/bin/env python3
"""Score the office-bookkeeping skill against the test cases.

Usage:  python3 score.py results.json

results.json is a list of objects, one per case, produced by Claude
(see tests/README.md for the exact prompt and format).
Standard library only. No data leaves your computer.
"""
import json, sys, pathlib

HERE = pathlib.Path(__file__).parent
TOL = 0.01  # money tolerance per field

def norm(s):
    return str(s).strip().upper().replace("_", " ")

def check(exp, got):
    problems = []
    if got is None:
        return ["no result for this case"]
    for f in ("net", "tax", "gross"):
        if f in exp:
            try:
                if abs(float(got.get(f)) - float(exp[f])) > TOL:
                    problems.append(f"{f}: expected {exp[f]}, got {got.get(f)}")
            except (TypeError, ValueError):
                problems.append(f"{f}: expected {exp[f]}, got {got.get(f)!r}")
    if "doc_type" in exp and norm(got.get("doc_type", "")) != norm(exp["doc_type"]):
        problems.append(f"doc_type: expected {exp['doc_type']}, got {got.get('doc_type')}")
    if "issue_date" in exp and str(got.get("issue_date", "")) != exp["issue_date"]:
        problems.append(f"issue_date: expected {exp['issue_date']}, got {got.get('issue_date')}")
    if "claimable" in exp:
        ok = [norm(c) for c in exp["claimable"]]
        if not any(norm(got.get("claimable", "")).startswith(c) for c in ok):
            problems.append(f"claimable: expected one of {exp['claimable']}, got {got.get('claimable')}")
    flags = {norm(f) for f in got.get("flags", [])}
    for f in exp.get("required_flags", []):
        if norm(f) not in flags:
            problems.append(f"missing flag {f}")
    for f in exp.get("forbidden_flags", []):
        if norm(f) in flags:
            problems.append(f"should NOT flag {f}")
    return problems

def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    results = {r.get("id"): r for r in json.load(open(sys.argv[1], encoding="utf-8"))}
    passed = 0
    cases = sorted((HERE / "cases").glob("*/expected.json"))
    for p in cases:
        exp = json.load(open(p, encoding="utf-8"))
        problems = check(exp, results.get(exp["id"]))
        if problems:
            print(f"FAIL {exp['id']}  {exp['title']}")
            for pr in problems:
                print(f"       - {pr}")
        else:
            passed += 1
            print(f"PASS {exp['id']}  {exp['title']}")
    print(f"\n{passed}/{len(cases)} cases passed")
    sys.exit(0 if passed == len(cases) else 1)

if __name__ == "__main__":
    main()
