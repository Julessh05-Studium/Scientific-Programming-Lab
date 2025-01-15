class ComplexZeroError(Exception):

    @classmethod
    def get_description(cls):
        return "Error rose, because the complex number is zero."
