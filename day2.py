"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

def product_array(arr):

    left = [0] * len(arr)
    right = [0] * len(arr)
    prod = [0] * len(arr)

    left[0] = 1
    right[len(arr)-1] = 1

    for i in range(1, len(arr)):
        left[i] = left[i-1] * arr[i-1]

    for j in range(len(arr)-2, 1, -1):
        right[j] = right[j+1] * arr[j+1]

    for i in range(len(arr)):
        prod[i] = left[i] * right[i]

    return prod
