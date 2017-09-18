"""my unit test methods"""

import unittest

class MyTestMethods(unittest.TestCase):
    """unit test class"""

    def test_test01(self):
        """upper() makes string uppercase"""
        self.assertEqual("foo".upper(), "FOO")

if __name__ == '__main__':
    unittest.main()
