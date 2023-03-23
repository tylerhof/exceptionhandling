import unittest

from expression import Ok

from exceptionhandling.access import Constant
from exceptionhandling.utils import Filter, Lambda, ToDictionary, ForEachParallel
from tests.test_utils import FunctorTest


class UtilsTest(unittest.TestCase):
    def test_filter(self):
        FunctorTest.test(self, Filter(lambda x: x == 'c' or x == 'b'),
                         ['a', 'b', 'c', 'd'], Ok(['b', 'c']))
    def test_lambda(self):
        FunctorTest.test(self, Lambda(lambda x : x * 2), 'blah', Ok('blahblah'))

    def test_to_dict(self):
        FunctorTest.test(self, ToDictionary({Constant('a') : Constant(1),
                                             Constant(2) : Constant('b')}), '', Ok({'a' : 1, 2 : 'b'}))

    def test_for_each_parallel(self):
        FunctorTest.test(self, ForEachParallel(Lambda(lambda x : x * 2)),
                         [0, 1, 3], Ok([0, 2, 6]))

if __name__ == '__main__':
    unittest.main()