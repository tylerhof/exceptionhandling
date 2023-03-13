import json

from exceptionhandling.functor import Functor

class Decode(Functor):

    def __init__(self, decode="utf-8"):
        super().__init__()
        self.decode = decode

    def apply(self, object_to_parse, **kwargs):
        return object_to_parse.decode(self.decode)


class Json(Functor):

    def apply(self, object_to_parse, **kwargs):
        return json.loads(object_to_parse)