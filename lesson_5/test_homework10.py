import unittest
from parameterized import parameterized
import homework10 as hw

class TestMyHomeWork(unittest.TestCase):
    def setUp(self) -> None:
        print("Starting testing...")
        print("Set data or something else")

    # def test_compare_function(self):
    #     print("----x<y----")
    #     self.assertEqual(hw.compare_function(2, 3), True)
    #     self.assertEqual(hw.compare_function(3, -2), False)
    #     self.assertEqual(hw.compare_function(2, 2), False)
    #     self.assertRaises(TypeError, hw.compare_function, True)


    # def test_pos_compare_function(self):
    #     print("----x<y for positive numbers----")
    #     self.assertEqual(hw.pos_compare_function(1, 2), True)
    #     self.assertEqual(hw.pos_compare_function(15, 2), False)
    #     self.assertEqual(hw.pos_compare_function(-1, 2), "Can compare only positive numbers!")
    #     self.assertEqual(hw.pos_compare_function(1, -2), "Can compare only positive numbers!")
    #
    #
    # def test_sum_function(self):
    #     print("----x+y-----")
    #     self.assertEqual(hw.sum_function(75, 15), 90)
    #     self.assertEqual(hw.sum_function(-75, 15), -60)
    #     self.assertEqual(hw.sum_function(0, 15), 15)


    @parameterized.expand([
        ("uppercase", "Tonya", "aynoT"),
        ("lowercase", "something", "gnihtemos"),
    ])
    def test_reverse(self, name, string, expected):
        self.assertEqual(hw.reverse(string), expected)




    def tearDown(self) -> None:
        print("Clean data or do something else after the test")
        print("Testing is done")
        print("--------------------------")