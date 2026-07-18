"""Tests for MTEF-py: parallel operator parsing."""
import os
import sys

# Add source to path
SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "src")
sys.path.insert(0, SRC_DIR)

from mtef_py.mtef import MTEF  # noqa: E402


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def load_test_file(name: str) -> bytes:
    path = os.path.join(DATA_DIR, name)
    with open(path, "rb") as f:
        return f.read()


def test_parallel_operator():
    """Regression: parallel symbol (∥) should be decoded as \\parallel."""
    data = load_test_file("parallel.mtef")
    mtef, err = MTEF.OpenBytes(data)
    assert err is None, f"OpenBytes returned error: {err}"
    latex = mtef.Translate()
    assert r"\parallel" in latex, f"Expected \\parallel in output, got: {latex}"
    assert len(latex) > 0, "Empty LaTeX output"


def test_parse_no_crash():
    """Sanity: all provided test .mtef files parse without crash."""
    for fname in os.listdir(DATA_DIR):
        if not fname.endswith(".mtef"):
            continue
        data = load_test_file(fname)
        mtef, err = MTEF.OpenBytes(data)
        assert err is None, f"{fname}: OpenBytes error: {err}"
        latex = mtef.Translate()
        assert latex is not None, f"{fname} returned None"
        assert len(latex) > 0, f"{fname} produced empty LaTeX"
        # LaTeX output should not fail to render
        assert "$$" not in latex.replace(" ", ""), f"{fname}: double $$ may cause rendering issues"
