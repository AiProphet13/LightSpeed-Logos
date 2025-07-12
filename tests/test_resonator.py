import unittest
import numpy as np
from src.resonator import DivineResonator

class TestDivineResonator(unittest.TestCase):
    def setUp(self):
        self.resonator = DivineResonator("Yahawah")
        
    def test_anchor_calculation(self):
        self.assertAlmostEqual(self.resonator.anchor, 5.739, places=2)
        
    def test_divine_verification(self):
        self.assertTrue(self.resonator.divine_verify(5.739))
        self.assertFalse(self.resonator.divine_verify(0.0))
        
    def test_latent_reason(self):
        result = self.resonator.latent_reason(1.618)
        self.assertGreater(result, 0)
        self.assertLess(result, 6.28)

if __name__ == "__main__":
    unittest.main()
