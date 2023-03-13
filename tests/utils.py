import unittest

from expression import Ok

from exceptionhandling.utils import Filter, Lambda
from tests.test_utils import FunctorTest


class UtilsTest(unittest.TestCase):
    def test_filter(self):
        FunctorTest.test(self, Filter(lambda x: x == 'c' or x == 'b'),
                         ['a', 'b', 'c', 'd'], Ok(['b', 'c']))
    def test_lambda(self):
        FunctorTest.test(self, Lambda(lambda x : x * 2), 'blah', Ok('blahblah'))

if __name__ == '__main__':
    unittest.main()