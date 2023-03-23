from expression import compose
from expression.collections import seq
from joblib import Parallel, delayed

from exceptionhandling.exception_handler import ExceptionHandler, AllList, IdentityPolicy, AllDict, Safe
from exceptionhandling.functor import Functor
from functools import partial

class Compose(Functor):

    def __init__(self, *args):
        super().__init__(IdentityPolicy())
        self.functors = list(args)
    def apply(self, input, **kwargs):
        functor_list= [partial(f, **kwargs) for f in self.functors]
        return compose(*functor_list)(input)


class ForEach(Functor):

    def __init__(self, element_Functor, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.element_Functor = element_Functor

    def apply(self, input, **kwargs):
        return seq.of_iterable(input).map(self.element_Functor)

class ForEachParallel(Functor):

    def __init__(self, element_Functor, n_jobs = 4, policy: ExceptionHandler = AllList()):
        super().__init__(policy)
        self.element_Functor = element_Functor
        self.n_jobs = n_jobs

    def apply(self, input, **kwargs):
        return Parallel(self.n_jobs)(delayed(self.element_Functor)(i) for i in seq.of_iterable(input))

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

class Filter(Functor):

    def __init__(self, predicate, policy: ExceptionHandler = Safe()):
        super().__init__(policy)
        self.predicate = predicate

    def apply(self, input, **kwargs):
        return [element for element in input if self.predicate(element, **kwargs)]

class ToDictionary(Functor):

    def __init__(self, Functor_dict, policy: ExceptionHandler = AllDict()):
        super().__init__(policy)
        self.Functor_dict = Functor_dict

    def apply(self, input, **kwargs):
        return {key(input) : value(input) for (key, value) in self.Functor_dict.items()}


class Lambda(Functor):

    def __init__(self, lambda_to_use, policy: ExceptionHandler = Safe()):
        super().__init__(policy)
        self.lambda_to_use = lambda_to_use

    def apply(self, input, **kwargs):
        return self.lambda_to_use(input, **kwargs)