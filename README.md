# mtef-py

[📖 English README](README_EN.md)

**Python MTEF 解析器 — 将 Word OLE 对象中的 MathType 公式转换为 LaTeX。**

零外部依赖，支持 Python ≥ 3.9。

## 快速开始

```python
from mtef_py.mtef import MTEF

with open("oleObject.bin", "rb") as f:
    mtef, err = MTEF.OpenBytes(f.read())

if err is None:
    latex = mtef.Translate()
    print(latex)  # 例如 $$ \frac { -b \pm \sqrt { b^{2} -4ac } } { 2a } $$
```

命令行方式：

```bash
python -m mtef_py path/to/oleObject.bin
```

## 什么是 MTEF？

MTEF（MathType Equation Format）是 [MathType](https://www.wiris.com/en/mathtype/) 用于在 Word 文档的 OLE 对象中存储数学公式的二进制格式。本库解码这些二进制数据并输出 LaTeX。

## 安装

```bash
pip install mtef-py
```

或从源码安装：

```bash
git clone https://github.com/your-username/mtef-py
cd mtef-py
pip install -e .
```

## 运行测试

```bash
cd mtef-py
pip install -e ".[dev]"
pytest tests/
```

---

## Credits

本项目是基于以下项目的 Python 实现：

- **zhexiao/mtef-go** — 原始 Go 实现 ([GitHub](https://github.com/zhexiao/mtef-go))
- 遵循 Apache-2.0 协议

## License

Apache License 2.0。详见 [LICENSE](LICENSE) 和 [NOTICE](NOTICE)。
