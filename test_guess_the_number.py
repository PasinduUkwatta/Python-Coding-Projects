import unittest
import guess_the_number

class TestGuessTheNumber(unittest.TestCase):

    def setUp(self):
        print('Begin the Test')
        
    def test_int_number(self):
        test_number =int(input(range(1,10)))
        result= guess_the_number.number(test_number)
        self.assertEqual(result,test_number)
        
    def tearDown(self):
        print('End of the Test')

if __name__ == '__main__':
    unittest.main()
