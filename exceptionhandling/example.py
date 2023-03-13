from exceptionhandling.access import Access
from exceptionhandling.utils import Compose


class ExampleObject():
    def __init__(self, variable_name):
        self.variable_name = variable_name

example_object = ExampleObject('foobar')

variable_name_accessor = Access('variable_name')

print(variable_name_accessor(example_object))

class ExampleObject2():
    def __init__(self, variable_name):
        self.blah = variable_name


example_object2 = ExampleObject2(example_object)

composed = Compose(Access('blah'), Access('variable_name'))

print(composed(example_object2))