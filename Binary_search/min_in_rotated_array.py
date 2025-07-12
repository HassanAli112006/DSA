"""""""""""""""""""""
🔹 Problem: Find Minimum in Rotated Sorted Array
🔁 Pattern: Binary Search (Modified)
⭐ Difficulty: Medium
📘 Source: LeetCode #153 → https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
🎯 Goal: Find the minimum element in a rotated sorted array with distinct values.
"""""""""""""""""""""
# nums = [3, 4, 5, 1, 2]
# Output: 1

nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0

# nums = [11, 13, 15, 17]
# Output: 11

def minimum_in_sorted_array(number: list) -> int:
    l = 0
    r = len(number) - 1

    while l < r:
        m = l + (r-l)//2

        if number[m] > number[r]:
            l = m + 1
        else:
            r = m
    return number[l]
print(minimum_in_sorted_array(nums))
