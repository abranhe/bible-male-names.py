import unittest
import bible_male_names

class TestGetLength(unittest.TestCase):
    def test(self):
        self.assertEqual(len(bible_male_names.get()), 1)

class TestValueInAll(unittest.TestCase):
	def test(self):
		self.assertEqual(bible_male_names.all()[0], 'Aaron')

class TestDifferenceBetweenTwo(unittest.TestCase):
	def test_rand(self):
		self.assertNotEqual(bible_male_names.rand(), bible_male_names.rand())

if __name__ == '__main__':
    unittest.main()
