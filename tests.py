import unittest
from material import Material
from properties import StressStrainTest
from database import CalculatorSession, TestRecord

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
try:
    from properties import StressStrainTest
except ImportError:
    import importlib
    calc = importlib.import_module("Basic calculation")
    StressStrainTest = getattr(calc, "StressStrainTest", None)


class TestStressStrainTest(unittest.TestCase):

    def test_stress_calculation(self):
        """Verify axial stress calculation (Force / Area)."""
        if StressStrainTest is None:
            self.skipTest("StressStrainTest class not found")
        test_obj = StressStrainTest(force=10000.0, area=50.0, change_in_length=0.02, original_length=2.0)
        self.assertAlmostEqual(test_obj.calculate_stress(), 200.0)

    def test_strain_calculation(self):
        """Verify engineering strain calculation (dL / L0)."""
        if StressStrainTest is None:
            self.skipTest("StressStrainTest class not found")
        test_obj = StressStrainTest(force=10000.0, area=50.0, change_in_length=0.02, original_length=2.0)
        self.assertAlmostEqual(test_obj.calculate_strain(), 0.01)

    def test_zero_area_raises_error(self):
        """Ensure zero area raises ValueError."""
        if StressStrainTest is None:
            self.skipTest("StressStrainTest class not found")
        with self.assertRaises(ValueError):
            test_obj = StressStrainTest(force=10000.0, area=0.0, change_in_length=0.02, original_length=2.0)
            test_obj.calculate_stress()
            
try:
    from database import CalculatorSession
except ImportError:
    import importlib
    calc = importlib.import_module("Basic calculation")
    CalculatorSession = getattr(calc, "CalculatorSession", None)


class TestCalculatorSession(unittest.TestCase):

    def test_session_history_logging(self):
        """Verify history tracking inside session object."""
        if CalculatorSession is None:
            self.skipTest("CalculatorSession class not found")
        session = CalculatorSession()
        session.add_test_result({"test_id": 1, "stress": 200.0, "strain": 0.01})
        self.assertEqual(len(session.history), 1)
        self.assertEqual(session.history[0]["stress"], 200.0)

if __name__ == "__main__":
    unittest.main()
