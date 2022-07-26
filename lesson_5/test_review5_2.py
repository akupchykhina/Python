import unittest
import review5_2 as r5


class Test_review5_2(unittest.TestCase):
    def test_power(self):
        self.assertEqual(r5.power(2, 3), 8, 'error')


    def test_spell(self):
        self.assertEqual(r5.spell("hello"), "olleh", "something's wrong")



if __name__ == '__main__':
    unittest.main()