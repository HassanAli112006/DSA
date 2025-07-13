"""""""""""""""""""""""""""
🔹 Problem: Find Ceiling of Target in Sorted Array
🔁 Pattern: Binary Search (Basic Variant)
⭐ Difficulty: Easy
📘 Custom Problem (Confidence Builder)
🎯 Goal: Given a sorted array, return the index of the smallest element ≥ target. If not found, return -1.
"""""""""""""""""""""""""""

def find_ceiling(number: list[int], target: int) -> int:
    l = 0
    r = len(number) - 1
    ans = -1  # Default if not found

    while l<=r:
        m = (l+r)//2
        if number[m] >= target:
            ans = m
            r = m-1
        else:
            l = m+1

    return ans


# Test Example
nums = [2, 3, 5, 9, 14, 20]
target = 15
print(find_ceiling(nums, target))  # Output: 5
