import unittest
import main


class TestMain(unittest.TestCase):

    def test_when_one_input_given(self):
        self.assertRaises(ValueError,main.find_min_minutes_def,["23:59"])
    
    def test_when_two_input_given(self):
        self.assertEqual(main.find_min_minutes_def(["23:59", "00:00"]), 0)
        
    def test_when_multiple_input_given(self):
        self.assertEqual(main.find_min_minutes_def(["00:00","23:59","00:00"]), 0)
        

unittest.main()
