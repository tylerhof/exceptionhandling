import traceback
from abc import abstractmethod, ABC

from expression import Ok, Error
from expression.core.result import bind


class ExceptionHandler(ABC):
    def __init__(self):
        pass

    def __call__(self, parser, object_to_parse):
        return self.get(parser, object_to_parse)

    @abstractmethod
    def get(self, parser, object_to_parse):
        pass


class IdentityPolicy(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        return parser(object_to_parse)

class Unwrap(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        if (isinstance(object_to_parse, Ok)):
            return bind(object_to_parse, parser)
        else:
            return parser(object_to_parse)

class Safe(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        return object_to_parse.map(parser)


class Truthy(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        return object_to_parse.map(parser).map(self.check)

    def check(self, inner_object):
        if inner_object:
            return Ok(inner_object)
        else:
            return Error("Falsy returned via " + traceback.format_exc())

class AllDict(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        dict = parser(object_to_parse)
        if (all(map(lambda x: x.is_ok(), dict.values()))):
            return Ok({key.default_value(): value.default_value() for (key, value) in dict.items()})
        else:
            return Error('/n'.join([str(key) + " : " + str(value) for (key, value) in dict.items() if
                                      not (key.is_ok() and value.is_ok())]))



class AnyList(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        return Ok([object for object in object_to_parse.map(parser) if (object.is_ok())])


class AllList(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse):
        list = object_to_parse.map(parser)
        return list.map(self.all)

    def all(self, list_to_parse):
        if all(isinstance(x, Ok) for x in list_to_parse):
            return [x.value for x in list_to_parse]
        else:
            return Error([str(index) + " : " + str(object.error) for index, object in enumerate(list) if object.is_error()])
