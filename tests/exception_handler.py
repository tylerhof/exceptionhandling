import unittest

from expression import Ok

from exceptionhandling.access import Access
from exceptionhandling.functor import Functor
from tests.test_utils import FunctorTest

class FunctorUsingKwargs(Functor):
    def apply(self, input, **kwargs):
        return kwargs['var']

class ExceptionHandlerTest(unittest.TestCase):
    def test_safe(self):
        FunctorTest.test(self, FunctorUsingKwargs(),
                         None, Ok('blah'), var='blah')

if __name__ == '__main__':
    unittest.main()