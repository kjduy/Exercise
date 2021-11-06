import sys 
sys.path.append("..")
from controller.fileOperator import FileOperator
import unittest

class TestFileOperator(unittest.TestCase):

    def testFileName(self):
        self.assertEqual(FileOperator.askFileName(""), "./model/1stWeek.txt")

    def testCountFileLines(self):
        self.assertEqual(FileOperator.countFileLines(self,"../model/1stWeek.txt"), 3)

    def testSeparateNames(self):
        self.assertEqual(FileOperator.separateNames(self,[],0,"../model/1stWeek.txt"), ['RENE','MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'])

if __name__ == "__main__":
    unittest.main()