"""
The public surface of the four algorithm modules: what they export, that every checksum
function has the documented signature, identity, docstring and argument handling, and that
the type stubs say the same.
"""
import ast
import inspect
import pickle
import re
import unittest
from pathlib import Path

import fastcrc

from tests.catalogue import CATALOGUE, CHECK_INPUT, MODULES, public_functions

PARAMETERS = ("poly", "init", "xorout", "refin", "refout")


def documented_parameters(doc):
    """The algorithm parameters a docstring states, as a dict like ``parameters``."""
    found = dict(re.findall(r"^\s*- (\w+): (\w+)$", doc, re.MULTILINE))
    return {
        key: {"True": True, "False": False}[value] if key.startswith("ref") else int(value, 16)
        for key, value in found.items()
    }


def parameters(algorithm):
    return {key: getattr(algorithm, key) for key in PARAMETERS}


class TestModules(unittest.TestCase):
    def test_exports(self):
        for name in MODULES:
            module = getattr(fastcrc, name)
            guaranteed = {a.name for a in CATALOGUE if a.module == name and not a.experimental}
            with self.subTest(module=name):
                public = {attr for attr in vars(module) if not attr.startswith("_")}
                self.assertEqual(public, set(module.__all__))
                self.assertEqual(guaranteed, module.algorithms_guaranteed)
                self.assertEqual(guaranteed, module.algorithms_available)

    def test_stubs(self):
        for name in MODULES:
            stub = Path(fastcrc.__file__).with_name(f"{name}.pyi")
            tree = ast.parse(stub.read_text())
            defined = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
            with self.subTest(stub=stub.name):
                self.assertEqual({a.name for a in CATALOGUE if a.module == name}, set(defined))
            for algorithm in CATALOGUE:
                if algorithm.module != name or algorithm.name not in defined:
                    continue
                node = defined[algorithm.name]
                with self.subTest(function=str(algorithm)):
                    args = node.args
                    self.assertEqual(["data", "initial"], [a.arg for a in args.args])
                    self.assertFalse(args.posonlyargs or args.kwonlyargs)
                    self.assertIsNone(args.vararg)
                    self.assertIsNone(args.kwarg)
                    self.assertEqual(1, len(args.defaults))
                    self.assertIsNone(args.defaults[0].value)
                    self.assertEqual("int", node.returns.id)
                    doc = ast.get_docstring(node)
                    self.assertEqual(parameters(algorithm), documented_parameters(doc))


class TestFunctions(unittest.TestCase):
    def test_signature(self):
        for name, fn in public_functions().items():
            with self.subTest(function=name):
                params = list(inspect.signature(fn).parameters.values())
                self.assertEqual(["data", "initial"], [p.name for p in params])
                self.assertIs(params[0].default, inspect.Parameter.empty)
                self.assertIs(params[1].default, None)
                for param in params:
                    self.assertIs(param.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD)

    def test_identity(self):
        for algorithm in CATALOGUE:
            fn = algorithm.function
            with self.subTest(function=str(algorithm)):
                self.assertEqual(algorithm.name, fn.__name__)
                self.assertEqual(f"fastcrc.{algorithm.module}", fn.__module__)
                self.assertIs(fn, pickle.loads(pickle.dumps(fn)))

    def test_docstring(self):
        # The docstring states the algorithm parameters; they must be the catalogue's.
        for algorithm in CATALOGUE:
            doc = algorithm.function.__doc__
            with self.subTest(function=str(algorithm)):
                self.assertTrue(doc.startswith(f"Compute a CRC-{algorithm.width} checksum of data"))
                self.assertIn(":param data:", doc)
                self.assertIn(":param Optional[int] initial:", doc)
                self.assertEqual(parameters(algorithm), documented_parameters(doc))

    def test_arguments(self):
        for algorithm in CATALOGUE:
            fn = algorithm.function
            check = algorithm.check
            with self.subTest(function=str(algorithm)):
                self.assertIsInstance(fn(CHECK_INPUT), int)
                self.assertEqual(check, fn(CHECK_INPUT, None))
                self.assertEqual(check, fn(data=CHECK_INPUT))
                self.assertEqual(check, fn(data=CHECK_INPUT, initial=None))
                self.assertEqual(check, fn(initial=fn(CHECK_INPUT[:4]), data=CHECK_INPUT[4:]))
                with self.assertRaises(TypeError):
                    fn()
                with self.assertRaises(TypeError):
                    fn(CHECK_INPUT, 0, 0)
                with self.assertRaises(TypeError):
                    fn(CHECK_INPUT, foo=0)
                with self.assertRaises(TypeError):
                    fn(CHECK_INPUT.decode())

    def test_initial_range(self):
        # ``initial`` is a previous checksum, so any value of the algorithm's width is valid
        # and nothing else is; continuing empty data from it gives it back.
        for algorithm in CATALOGUE:
            fn = algorithm.function
            limit = 1 << algorithm.width
            with self.subTest(function=str(algorithm)):
                self.assertEqual(0, fn(b"", 0))
                self.assertEqual(limit - 1, fn(b"", limit - 1))
                self.assertEqual(algorithm.check, fn(b"", algorithm.check))
                for bad in (-1, limit):
                    with self.assertRaises(OverflowError):
                        fn(b"", bad)
                for bad in (1.0, "0", b"\0"):
                    with self.assertRaises(TypeError):
                        fn(b"", bad)
