import unittest

from expression import Ok

from exceptionhandling.access import Access
from exceptionhandling.utils import Filter, Lambda
from tests.test_utils import FunctorTest

class ExampleObject():

    def __init__(self, var1, var2) -> None:
        super().__init__()
        self.var1 = var1
        self.var2 = var2

class AccessTest(unittest.TestCase):
    def test_access_obj(self):
        FunctorTest.test(self, Access('var2'),
                         ExampleObject('a', 'c'), Ok('c'))

    def test_access_dict(self):
        FunctorTest.test(self, Access('var2'),
                         {'var1' : 'a', 'var2' : 'c'}, Ok('c'))

if __name__ == '__main__':
    unittest.main()