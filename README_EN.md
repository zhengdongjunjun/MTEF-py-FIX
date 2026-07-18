# mtef-py

**Python MTEF parser — convert MathType equations from Word OLE objects to LaTeX.**

Zero external dependencies. Works with any Python ≥ 3.9.

## Quick Start

```python
from mtef_py.mtef import MTEF

with open("oleObject.bin", "rb") as f:
    mtef, err = MTEF.OpenBytes(f.read())

if err is None:
    latex = mtef.Translate()
    print(latex)  # e.g. $$ \frac { -b \pm \sqrt { b^{2} -4ac } } { 2a } $$
```

From the command line:

```bash
python -m mtef_py path/to/oleObject.bin
```

## What is MTEF?

MTEF (MathType Equation Format) is a binary format used by [MathType](https://www.wiris.com/en/mathtype/) to store mathematical equations inside OLE objects in Word documents. This library decodes those binaries and outputs LaTeX.

## Installation

```bash
pip install mtef-py
```

Or install from source:

```bash
git clone https://github.com/your-username/mtef-py
cd mtef-py
pip install -e .
```

## Running Tests

```bash
cd mtef-py
pip install -e ".[dev]"
pytest tests/
```

---

## Credits

This project is a Python implementation inspired by:

- **zhexiao/mtef-go** — original Go implementation ([GitHub](https://github.com/zhexiao/mtef-go))
- Licensed under Apache-2.0

## License

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
