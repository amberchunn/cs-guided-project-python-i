"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""

def get_length(str):
    return len(str)

# def sort_by_length(lst):
#     # Your code here
#     return sorted(lst, key=lambda str: len(str))

def sort_by_length(lst):
    # Your code here
    return sorted(lst, key=len)

str_list = ["amber", "elle", "magnus", "mochi"]

print(sort_by_length(str_list))

