## [1.0.1] — 2026-07-18

### Fixed

- Fixed MTEF CHAR parsing issue where FONT_STYLE_DEF / COLOR_DEF / COLOR metadata
  records could consume subsequent valid CHAR record bytes, causing character loss
  in the parsed LaTeX output (e.g., `OC\parallel` → `OC\parallel AD`). (#1)
- Added fallback handling for MTEF symbol encoding variants: when a CHAR record
  with typeface != fnMTEXTRA is encountered, the parser now retries the lookup
  with the alternate key (with/without `/mathmode` suffix). (#2)
- Unknown symbols now emit LaTeX-safe `[U+XXXX]` placeholders instead of raw
  Unicode characters, preventing invalid LaTeX output. (#3)

### Added

- Symbol mapping for MTEF internal codepoint U+0002 (`\parallel`) used by
  Symbol / MT Extra font encoding. (#1)
- `char/0x2225` and `char/0x2226` fallback entries without `/mathmode` suffix
  for compatibility with non-fnMTEXTRA typeface encodings. (#2)

## [1.0.0] — Initial release

Python port of zhexiao/mtef-go.
