"""""""""""""""""""""""""""
🔹 Problem: Find Floor of Target in Sorted Array
🔁 Pattern: Binary Search (Basic Variant)
⭐ Difficulty: Easy
📘 Custom Problem (Confidence Builder)
🎯 Goal: Given a sorted array, return the index of the largest element ≤ target. If not found, return -1.
"""""""""""""""""""""""""""

nums = [2, 3, 5, 9, 14, 20]
target = 15
# Output: 4   # nums[4] = 14 is the largest number ≤ 15

# nums = [2, 3, 5, 9, 14, 20]
# target = 1
# Output: -1  # No element ≤ 1

def floor_of_tr(number: list[int] , tr: int) -> int:
    l = 0
    r = len(number) - 1
    ans = -1
    while l <= r:
        m = l + (r-l)//2

        if number[m] <= tr:
            ans = m
            l = m + 1
        else:
            r = m-1
    return ans
print(floor_of_tr(nums, target))