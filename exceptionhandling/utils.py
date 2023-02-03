from expression.collections import seq

from exceptionhandling.exception_handler import ExceptionHandler, AllList, IdentityPolicy, AllDict
from exceptionhandling.functor import Functor


class ForEach(Functor):

    def __init__(self, element_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.element_Functor = element_Functor

    def apply(self, input):
        return seq.of_iterable(input).map(self.element_Functor)

class Identity(Functor):

    def __init__(self, policy: ExceptionHandler = IdentityPolicy()):
        super().__init__(policy)

    def apply(self, input):
        return input

class ToList(Functor):

    def __init__(self, list_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.list_Functor = list_Functor

    def apply(self, input):
        return [Functor(input) for Functor in self.list_Functor]

class ToDictionary(Functor):

    def __init__(self, Functor_dict, policy: ExceptionHandler = AllDict()):
        super().__init__(policy)
        self.Functor_dict = Functor_dict

    def apply(self, input):
        return {key(input) : value(input) for (key, value) in self.Functor_dict.items()}