import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add(self):
        self.assertEqual(self.calc.add(-1,-2),-3)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(5,3),2)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(-4,-7),3)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(4,5),20)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(4,5),20)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(4,-5),-20)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(-4,5),-20)

    def test_div(self):
        self.assertEqual(self.calc.divide(20,5),4)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(20,5),4)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(20,-5),-4)

    def test_div(self):
        self.assertEqual(self.calc.divide(-20,5),-4)
    
    def test_mod(self):
        self.assertEqual(self.calc.modulo(10,3),1)
    
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(7,0)

    def test_mod_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(7,0)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()