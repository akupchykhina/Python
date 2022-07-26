import unittest

class TestMyCode(unittest.TestCase):

    def setUp(self) -> None:
        print("Starting testing...")
        print("Set data or something else")


    def test_is_a_greater_than_b(self):
        print("test_is_a_greater_than_b")
        a = 4
        b = 3
        self.assertTrue(a > b, "A is not greater than B") #если тест упадет, увидим эту фразу


    def test_x_is_equal_to_y(self):
        print("test_x_is_equal_to_y")
        x = 45
        y = 45
        self.assertTrue(x == y, f"Is {x} equal to {y}? NO")
        # or self.assertEqual(x, y)

    def tearDown(self) -> None:
        print("Clean data or do somethinf else after the test")
        print("Testing is done")
        print("--------------------------")


if __name__ == '__main__':
    unittest.main()