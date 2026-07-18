#!/usr/bin/env python3
"""Example: parse a MathType OLE object and print LaTeX."""

import sys
import os

# Add src to path so mtef_py can be imported
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mtef_py.mtef import MTEF


def main():
    if len(sys.argv) < 2:
        print("Usage: python examples/parse_mtef.py <path_to_oleObject.bin>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "rb") as f:
        data = f.read()

    mtef, err = MTEF.OpenBytes(data)
    if err:
        print(f"Error parsing MTEF: {err}", file=sys.stderr)
        sys.exit(1)

    latex = mtef.Translate()
    print(latex)


if __name__ == "__main__":
    main()
