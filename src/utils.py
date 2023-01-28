from expression.collections import seq

from exception_handler import ExceptionHandler, AllList, IdentityPolicy, AllDict
from functor import Functor


class ForEach(Functor):

    def __init__(self, element_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.element_Functor = element_Functor

    def parse(self, object_to_parse):
        return seq.of_iterable(object_to_parse).map(self.element_Functor)

class Identity(Functor):

    def __init__(self, policy: ExceptionHandler = IdentityPolicy()):
        super().__init__(policy)

    def parse(self, object_to_parse):
        return object_to_parse

class ToList(Functor):

    def __init__(self, list_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.list_Functor = list_Functor

    def parse(self, object_to_parse):
        return [Functor(object_to_parse) for Functor in self.list_Functor]

class ToDictionary(Functor):

    def __init__(self, Functor_dict, policy: ExceptionHandler = AllDict()):
        super().__init__(policy)
        self.Functor_dict = Functor_dict

    def parse(self, object_to_parse):
        return {key(object_to_parse) : value(object_to_parse) for (key, value) in self.Functor_dict.items()}