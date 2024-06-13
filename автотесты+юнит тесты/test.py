assert 2+2==4
import unittest

class DevisionTest(unittest.TestCase):
    def test_devision(self):
        self.assertEqual(2+2,5)

if __name__=='__main__':
    unittest.main()