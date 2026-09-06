import unittest

try:
    from material import Material
except ImportError:
    import importlib
    calc = importlib.import_module("Basic calculation")
    Material = getattr(calc, "Material", None)


class TestMaterial(unittest.TestCase):

    def test_material_initialization(self):
        """Verify Material initializes attributes correctly."""
        if Material is None:
            self.skipTest("Material class not found")
        mat = Material(name="Steel", yield_strength=250.0, ultimate_strength=400.0)
        self.assertEqual(mat.name, "Steel")
        self.assertEqual(mat.yield_strength, 250.0)
        self.assertEqual(mat.ultimate_strength, 400.0)


if __name__ == "__main__":
    unittest.main()
