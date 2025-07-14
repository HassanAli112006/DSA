"""""""""""""""""""""""""""
🔹 Problem: Find Peak Element
🔁 Pattern: Binary Search (Peak Element)
⭐ Difficulty: Medium
📘 Source: LeetCode #162 → https://leetcode.com/problems/find-peak-element/
🎯 Goal: Return the index of any peak element. A peak is strictly greater than both neighbors.
"""""""""""""""""""""""""""
# nums = [1, 2, 3, 1]
# Output: 2  # nums[2] = 3 is a peak

nums = [1, 2, 1, 3, 5, 6, 4]
# Output: 1 or 5  # nums[1] = 2 or nums[5] = 6 are both peaks

def peak_value(number: list[int]) -> int:
    l = 0
    r = len(number) - 1
    while l <= r:
        m = l + (r-l)//2
        if m > 0 and number[m] < number[m-1]:
            r = m - 1
        elif m < len(number) -1 and number[m] < number[m+1]:
            l = m + 1
        else:
            return m

print(peak_value(nums))