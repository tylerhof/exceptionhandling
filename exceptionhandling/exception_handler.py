import traceback
from abc import abstractmethod, ABC

from expression import Ok, Error


class ExceptionHandler(ABC):
    def __init__(self):
        pass

    def __call__(self, parser, object_to_parse, **kwargs):
        return self.get(parser, object_to_parse, **kwargs)

    @abstractmethod
    def get(self, parser, object_to_parse, **kwargs):
        pass


class IdentityPolicy(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        return parser(object_to_parse, **kwargs)

class Unwrap(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        if (isinstance(object_to_parse, Ok)):
            return parser(object_to_parse.value, **kwargs)
        else:
            return parser(object_to_parse, **kwargs)

class Safe(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        return object_to_parse.map(parser, **kwargs)


class Truthy(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        return object_to_parse.map(parser, **kwargs).map(self.check)

    def check(self, inner_object):
        if inner_object:
            return Ok(inner_object)
        else:
            return Error("Falsy returned via " + traceback.format_exc())

class AllDict(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        dict = parser(object_to_parse, **kwargs)
        if all(k.is_ok() and v.is_ok() for (k, v) in dict.items()):
            return Ok({k.value: v.value for (k, v) in dict.items()})
        else:
            return Error('/n'.join([str(key) + " : " + str(value) for (key, value) in dict.items() if
                                      not (key.is_ok() and value.is_ok())]))



class AnyList(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        return Ok([object for object in object_to_parse.map(parser, **kwargs) if (object.is_ok())])


class AllList(ExceptionHandler):

    def __init__(self):
        super().__init__()

    def get(self, parser, object_to_parse, **kwargs):
        list = object_to_parse.map(parser, **kwargs)
        return list.map(self.all)

    def all(self, list_to_parse):
        if all(isinstance(x, Ok) for x in list_to_parse):
            return [x.value for x in list_to_parse]
        else:
            return Error([str(index) + " : " + str(object.error) for index, object in enumerate(list) if object.is_error()])
