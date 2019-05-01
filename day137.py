"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.

"""


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
