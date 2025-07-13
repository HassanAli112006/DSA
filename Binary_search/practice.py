"""""""""""""""""""""""""""
🔹 Problem: Element Exists in Sorted Array
🔁 Pattern: Binary Search (Classic)
⭐ Difficulty: Easy
📘 Custom Practice Problem
🎯 Goal: Return True if target exists in sorted array, else False.
"""""""""""""""""""""""""""

nums = [1, 3, 5, 6, 9, 13]
target = 6
# → Output: True
# target = 8
# → Output: False


def exists(number: list, tr: int) -> int:
    l = 0
    r = len(number) - 1

    while l <= r:
        m = l + (r-l)//2
        if number[m] == tr:
            return True
        elif number[m] < tr:
            l = m + 1
        else:
            r = m - 1
    return False
print(exists(nums, target))
