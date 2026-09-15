"""
Guard the public surface of the four algorithm modules: every listed function
is callable positionally and by keyword, is introspectable, and picklable by
reference.
"""
import inspect
import pickle
import unittest

import fastcrc

MODULES = ("crc8", "crc16", "crc32", "crc64")


class TestPublicApi(unittest.TestCase):
    def test_exports(self):
        for name in MODULES:
            module = getattr(fastcrc, name)
            with self.subTest(module=name):
                self.assertTrue(module.algorithms_guaranteed <= set(module.__all__))
                self.assertEqual(module.algorithms_guaranteed, module.algorithms_available)
                for attr in module.__all__:
                    self.assertTrue(hasattr(module, attr), attr)

    def test_functions(self):
        for name in MODULES:
            module = getattr(fastcrc, name)
            functions = [a for a in module.__all__ if not a.startswith("algorithms_")]
            self.assertTrue(functions)
            for attr in functions:
                fn = getattr(module, attr)
                with self.subTest(function=f"{name}.{attr}"):
                    params = list(inspect.signature(fn).parameters.values())
                    self.assertEqual([p.name for p in params], ["data", "initial"])
                    self.assertIs(params[1].default, None)
                    self.assertEqual(fn.__name__, attr)
                    self.assertEqual(fn.__module__, f"fastcrc.{name}")
                    self.assertTrue(fn.__doc__.startswith(f"Compute a CRC-{name[3:]} checksum"))
                    self.assertIn(":param bytes data:", fn.__doc__)
                    self.assertIs(pickle.loads(pickle.dumps(fn)), fn)
                    whole = fn(b"123456789")
                    self.assertIsInstance(whole, int)
                    self.assertEqual(whole, fn(data=b"123456789", initial=None))
                    self.assertEqual(whole, fn(b"56789", fn(b"1234")))
                    self.assertEqual(whole, fn(data=b"56789", initial=fn(b"1234")))
                    with self.assertRaises(TypeError):
                        fn("123456789")


if __name__ == "__main__":
    unittest.main()
