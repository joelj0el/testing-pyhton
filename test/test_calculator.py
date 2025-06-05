import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import suma, resta, multiplicacion

class CalculatorTest(unittest.TestCase):
    
    #perubea unitaria ora la funcion suma
    def test_suma(self):
        """Test the suma function."""
        self.assertEqual(suma(4, 3), 7)
        
    #perubea unitaria ora la funcion resta
    def test_resta(self):
        """Test the resta function."""
        self.assertEqual(resta(4, 3), 1)
        
    #perubea unitaria ora la funcion multiplicacion
    def test_multiplicacion(self):  
        """Test the multiplicacion function."""
        from src.calculator import multiplicacion
        self.assertEqual(multiplicacion(4, 3), 12)
 