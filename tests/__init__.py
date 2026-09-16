"""
fastcrc test suite.

The tests import ``fastcrc`` from the repository root, so build the extension in place first
(``uv sync``, ``pip install -e .`` or ``maturin develop``), then run from the root::

    python -m unittest -v                     # everything
    python -m unittest -v tests.test_api      # one module

``tests/catalogue.py`` lists every algorithm with its parameters and check value; the test
modules are driven by it, so a new algorithm needs one line there and nothing else.
"""
