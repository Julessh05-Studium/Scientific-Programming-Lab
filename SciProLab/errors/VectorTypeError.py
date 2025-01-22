class VectorTypeError(Exception):

    @classmethod
    def get_description(cls):
        return "Vector components must be of type int or float"
