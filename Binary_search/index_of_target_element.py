"""
🔹 Problem: Classic Binary Search
🔁 Pattern: Binary Search (Divide and Conquer)
⭐ Difficulty: Easy
📘 Source: LeetCode #704 (https://leetcode.com/problems/binary-search/)
🎯 Goal: Return the index of the target element in a sorted array. If not found, return -1.
"""

nums = [-1, 0, 3, 5, 9, 12]
target = 9
# Output: 4

# nums = [-1, 0, 3, 5, 9, 12]
# target = 2
# Output: -1

def binarySearch(number: list, tr: int) -> int:
    l = 0
    r = len(number) - 1

    while l <= r:
        m = l + ((r-l)//2)

        if number[m] == tr:
            return m
        elif tr > number[m]:
            l = m+1
        else:
            r = m-1
    return -1
print(binarySearch(nums, target))
