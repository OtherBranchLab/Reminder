class State:
    def __eq__(self, other):
        return isinstance(self, other)
