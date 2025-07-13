"""""""""""""""""""""""""""
🔹 Problem: Find Ceiling of Target in Sorted Array
🔁 Pattern: Binary Search (Basic Variant)
⭐ Difficulty: Easy
📘 Custom Problem (Confidence Builder)
🎯 Goal: Given a sorted array, return the index of the smallest element ≥ target. If not found, return -1.
"""""""""""""""""""""""""""
# nums = [2, 3, 5, 9, 14, 20]
# target = 15
# Output: 5  # Because nums[5] = 20 is the smallest number ≥ 15

nums = [2, 3, 5, 9, 14, 20]
target = 21
# Output: -1  # No element ≥ 21

def small_element_g_than_tr(number: list, tr: int) -> int:
    l = 0
    r = len(number) - 1
    ans = -1

    while l <= r:
        m = l + (r-l)//2

        if number[m] >= tr:
            ans = m
            r = m-1
        else:
            l = m + 1
    return ans
print(small_element_g_than_tr(nums, target))
