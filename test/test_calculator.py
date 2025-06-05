import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import suma, resta

class CalculatorTest(unittest.TestCase):
    
    #perubea unitaria ora la funcion suma
    def test_suma(self):
        """Test the suma function."""
        self.assertEqual(suma(4, 3), 7)
 