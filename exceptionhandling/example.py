from exceptionhandling.access import Access


class ExampleObject():
    def __init__(self, variable_name):
        self.variable_name = variable_name

example_object = ExampleObject('foobar')

variable_name_accessor = Access('variable_name')

print(variable_name_accessor(example_object))