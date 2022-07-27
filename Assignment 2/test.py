import unittest
import main


class TestMain(unittest.TestCase):

    def test_when_one_input_given(self):
        self.assertRaises(ValueError,main.find_min_minutes_def,["23:59"])
        
    def test_when_all_inputs_before_12(self):
        self.assertEqual(main.find_min_minutes_def(["01:20","11:20","09:20"]), 120) #JUST
    
    def test_when_all_inputs_after_12(self):
        self.assertEqual(main.find_min_minutes_def(["13:20","23:20","21:20"]), 120) #JUST
    
    def test_when_time_of_other_date_is_near(self):
        self.assertEqual(main.find_min_minutes_def(["01:20","20:20","23:55"]), 85)
    
    def test_when_time_of_this_date_is_near(self):
        self.assertEqual(main.find_min_minutes_def(["01:20","23:20","23:30"]), 10)
        
    def test_when_has_duplicate_inputs_before_12(self):
        self.assertEqual(main.find_min_minutes_def(["01:20","01:20","09:20"]), 0)
        
    def test_when_has_duplicate_inputs_after_12(self):
        self.assertEqual(main.find_min_minutes_def(["13:20","13:20","21:20"]), 0)


unittest.main()
