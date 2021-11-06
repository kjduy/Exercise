import sys 
sys.path.append("..")
from controller.listOperator import ListOperator
import unittest

class TestListOperator(unittest.TestCase):

    def testCountTimesMatchOffice(self):
        self.assertEqual(ListOperator.countTimesMatchOffice(self,
        [['RENE','MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'],
        ['ASTRID','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'],
        ['ANDRES','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']],0,2), 1)

    def testCreateListOnlyNames(self):
        self.assertEqual(ListOperator.createListOnlyNames(self,3,
        [['RENE','MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'],
        ['ASTRID','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'],
        ['ANDRES','MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']]),
        ['RENE','ASTRID','ANDRES'])

if __name__ == "__main__":
    unittest.main()