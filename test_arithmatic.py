import unittest
import arithmatic as mat

class TestArithmatic(unittest.TestCase):
    
    def test_add(self):
        self.assertEquals(mat.add(5,5),10)

if __name__ == '__main__':
    unittest.main()
