'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def two_sum(arr, k):

	dic = {}

	for i, num in enumerate(arr):

		if num in dic:
			return True 

		dic[k-num] = i
		
	return False