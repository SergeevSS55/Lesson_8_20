import calk
import unittest

class CalcTest(unittest.TestCase):

    def setUp(self):
        print('setup')
    def test_add(self):
        self.assertEqual(calk.add(1, 2), 3)
        '''
        Test for add function in calculator 
        '''
    def test_sub(self):
        self.assertEqual(calk.sub(5, 3), 2)

if __name__ == '__main__':
    unittest.main()