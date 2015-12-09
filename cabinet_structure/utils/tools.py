class MultipleIter(object):
    def __init__(self):
        self.a, self.b = 0, 0

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.b + 6
        if self.a > 100:
            raise StopIteration()
        return self.a
