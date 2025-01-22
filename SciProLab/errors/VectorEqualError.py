class VectorEqualError(Exception):

    @classmethod
    def get_description(cls):
        return "Vectors can't be compared, most likely one parameter isn't a vector"
