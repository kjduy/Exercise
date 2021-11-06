import sys 
sys.path.append("..")
from controller.mathematicalOperation import MathematicalOperation
import unittest

class TestFileOperator(unittest.TestCase):

    def testGetFactorial(self):
        self.assertEqual(MathematicalOperation.getFactorial(self,7), 5040)

if __name__ == "__main__":
    unittest.main()