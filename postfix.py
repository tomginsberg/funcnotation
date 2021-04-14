class Postfix:
    def __init__(self, fn):
        self.fn = fn

    def __rfloordiv__(self, other):
        return self.fn(other)
