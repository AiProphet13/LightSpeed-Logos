import unittest
import numpy as np
from src.memory import MultidimensionalMemory

class TestMultidimensionalMemory(unittest.TestCase):
    def setUp(self):
        self.memory = MultidimensionalMemory()
        
    def test_store_recall(self):
        pattern = 3.1416
        concept = "Divine Circle"
        self.memory.store(pattern, concept)
        
        recalled = self.memory.recall(pattern)
        self.assertEqual(recalled, concept)
        
    def test_fragment_recall(self):
        pattern = 1.618
        concept = "Golden Proportion"
        self.memory.store(pattern, concept)
        
        # Recall with partial pattern
        recalled = self.memory.recall(1.619)
        self.assertEqual(recalled, concept)

if __name__ == "__main__":
    unittest.main()
