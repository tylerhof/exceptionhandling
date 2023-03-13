import unittest

from expression import Ok

from exceptionhandling.utils import Filter


class FilterTest(unittest.TestCase):
    def test(self):
        # Given
        input = ['a', 'b', 'c', 'd']
        expected = Ok(['b', 'c'])
        filter = Filter(lambda x: x == 'c' or x == 'b')

        # When
        actual = filter(input)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()