import unittest
import main


class TestMain(unittest.TestCase):

    def test_find_min_minutes_def(self):
        self.assertEqual(main.find_min_minutes_def(["23:59", "00:00"]), 1)
        self.assertEqual(main.find_min_minutes_def(["00:00","23:59","00:00"]), 0)
