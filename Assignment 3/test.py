import unittest
import main


class TestMain(unittest.TestCase):

    def test_when_all_are_negative(self):
        self.assertEqual(main.maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4]),-1)
    
    def test_when_all_are_positive(self):
        self.assertEqual(main.maxSubArray([2,1,3,4,1,2,1,5,4]),23)
    
    def test_when_mix_array(self):
        self.assertEqual(main.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
        
    def test_when_array_has_zero(self):
        self.assertEqual(main.maxSubArray([-2,1,-3,4,0,0,1,-5,4]),5)
    
    def test_when_array_has_zero(self):
        self.assertEqual(main.maxSubArray([-3]),-3)
        

unittest.main()
