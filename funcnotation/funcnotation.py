class PrePostFix:
    def __init__(self, fn):
        self.fn = fn

    def __rfloordiv__(self, other):
        return self.fn(other)

    def __matmul__(self, other):
        return self.fn(other)
