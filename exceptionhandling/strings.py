from exceptionhandling.functor import Functor

class Decode(Functor):

    def __init__(self, decode="utf-8"):
        super().__init__()
        self.decode = decode

    def parse(self, object_to_parse):
        return object_to_parse.decode(self.decode)