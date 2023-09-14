import unittest
from utils import utils

class utils_tests(unittest.TestCase):
    def test1Reversed(self):
        self.assertEqual(432, utils().reversed(234))
    def test2Reversed(self):
        with self.assertRaises(TypeError): 
            utils().reversed(2.3)
    def test3Reversed(self):
        with self.assertRaises(TypeError):
            utils().reversed("two")
    def test1Formatter(self):
        self.assertEqual(('0b10111', '0o27'), utils().formatter(23))
    def test2Formatter(self):
        with self.assertRaises(TypeError):
            utils().formatter(2.3)
    def test3Formatter(self):
        with self.assertRaises(TypeError):
            utils().formatter("two")

if __name__ == '__main__':
    unittest.main()