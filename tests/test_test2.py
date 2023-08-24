import unittest
import test2

class test_test2(unittest.TestCase):
    
    def test_add(self):
        calculator = test2.Calculator(2,3)

        self.assertEqual(calculator.add(), 5, "incorrect addition")

    def test_sub(self):
        calculator = test2.Calculator(2,3)

        self.assertEqual(calculator.subtract(), -1, "incorrect subtraction")

    def test_divide(self):
        calculator = test2.Calculator(4,2)

        self.assertEqual(calculator.divide(), 2, "incorrect division")

    def test_multiply(self):
        calculator = test2.Calculator(2,5)

        self.assertEqual(calculator.multiply(), 10, "incorrect multiplication")

    def test_min(self):
        calculator = test2.Calculator(2,3)

        self.assertEqual(calculator.min(), 2, "incorrect min")
        



unittest.main()


