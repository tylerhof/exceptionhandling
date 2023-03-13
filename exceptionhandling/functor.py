from abc import ABC,abstractmethod

from expression import Result, Ok

from exceptionhandling.exception_handler import ExceptionHandler, Safe


class Functor(ABC):

    def __init__(self, policy: ExceptionHandler = Safe()):
        self.policy = policy

    def __call__(self, input, **kwargs):
        return self.policy(self.apply, self.wrap(input), **kwargs)

    @abstractmethod
    def apply(self, input, **kwargs):
        pass

    def wrap(self, input):
        if isinstance(input, Result):
            return input
        else:
            return Ok(input)