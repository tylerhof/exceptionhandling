from exceptionhandling.functor import Functor


class Access(Functor):

    def __init__(self, variable_name):
        super().__init__()
        self.variable_name = variable_name

    def apply(self, object_to_parse, **kwargs):
        return object_to_parse.__dict__[self.variable_name]

class AccessIndex(Functor):

    def __init__(self, index):
        super().__init__()
        self.index = index

    def apply(self, object_to_parse, **kwargs):
        return object_to_parse[self.index]

class Constant(Functor):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def apply(self, object_to_parse, **kwargs):
        return self.value