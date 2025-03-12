import unittest
import re


def add(numbers):
    if not numbers:
         return 0
    if ',\n' in numbers:
         return "error"
    numbers = map(int, re.split('[,\n]',numbers)) 
    return sum(numbers)

class Test(unittest.TestCase):
    def testfunction(self):
        self.assertEqual(add("2,3"), 5)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add(""), 0)
        self.assertEqual(add("1,2,3,4,5,6,7"), 28)
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("1\n2\n3\n4"), 10)
        self.assertEqual(add("1,\n2\n3\n4"), "error")
       

        
if __name__ == '__main__':
        unittest.main()
