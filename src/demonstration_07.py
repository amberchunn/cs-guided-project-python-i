"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
# UPER
# Understand
# Inputs: array, n
# Plan
# if n > len return none, sort array, return arr[n-1]
# Execute
# Reflect/Revise
def nth_smallest(lst, n):
    # Your code here
    if n > len(lst) or n >= 0:
        return None
    sorted_arr = sorted(lst)
    return sorted_arr[n - 1]

print(nth_smallest([7, 5, 3, 1], 5))

