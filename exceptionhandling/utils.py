from expression import compose
from expression.collections import seq

from exceptionhandling.exception_handler import ExceptionHandler, AllList, IdentityPolicy, AllDict
from exceptionhandling.functor import Functor


class Compose(Functor):

    def __init__(self, *args):
        super().__init__(IdentityPolicy())
        self.functors = list(args)
    def apply(self, input, **kwargs):
        return compose(*self.functors)



class ForEach(Functor):

    def __init__(self, element_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.element_Functor = element_Functor

    def apply(self, input, **kwargs):
        return seq.of_iterable(input).map(self.element_Functor)

class Identity(Functor):

    def __init__(self, policy: ExceptionHandler = IdentityPolicy()):
        super().__init__(policy)

    def apply(self, input, **kwargs):
        return input

class ToList(Functor):

    def __init__(self, list_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.list_Functor = list_Functor

    def apply(self, input, **kwargs):
        return [Functor(input) for Functor in self.list_Functor]

class ToDictionary(Functor):

    def __init__(self, Functor_dict, policy: ExceptionHandler = AllDict()):
        super().__init__(policy)
        self.Functor_dict = Functor_dict

    def apply(self, input, **kwargs):
        return {key(input) : value(input) for (key, value) in self.Functor_dict.items()}