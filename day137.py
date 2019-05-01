class BitArray(object):

    def __init__(self, size):
        self.array = [0] * size

    def set(self, index, val):
        if val == 0 or val == 1:
            self.array[n-index-1] = val
        else:
            raise Exception("Value in a bit array must be either 0 or 1")

    def get(self, index):
        return self.array[n-index-1]
