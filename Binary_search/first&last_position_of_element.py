"""""""""""""""""""""""""""
🔹 Problem: Find First and Last Position of Element in Sorted Array
🔁 Pattern: Binary Search (Modified)
⭐ Difficulty: Medium
📘 Source: LeetCode #34 (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
🎯 Goal: Given a sorted array, find the first and last position of a given target value.
"""""""""""""""""""""""""""

nums = [5,7,7,8,8,10]
target = 8
# Output: [3, 4]

# nums = [5,7,7,8,8,10]
# target = 6
# Output: [-1, -1]

# nums = []
# target = 0
# Output: [-1, -1]

def searchRange(number: list[int], tr: int) -> list[int]:
    indices = []
    l = 0
    r = len(number)

    while l >= r:
        m = l + ((r-l)//2)

        if number[m] == tr:
            return m
        elif tr > number[m]:
            l = m+1
        else:
            r = m-1
    # if len(indices) == 0:
    #     return [-1,-1]
    # else:
    #     return indices
    return -1
print(searchRange(nums, target))
