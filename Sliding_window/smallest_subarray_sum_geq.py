"""
🔹 Problem: Smallest Subarray With Sum ≥ K  
🔁 Pattern: Sliding Window (Variable Size)  
⭐ Difficulty: Medium  
📘 Source: LeetCode #209 (https://leetcode.com/problems/minimum-size-subarray-sum/)  
🎯 Goal: Return the length of the smallest contiguous subarray whose sum is ≥ K. If none, return 0.
"""

# 🧠 Problem Statement:
# Given an array of positive integers and a target value `k`,
# find the length of the smallest contiguous subarray whose sum ≥ `k`.
# If no such subarray exists, return 0.

arr = [2, 3, 1, 2, 4, 3]
k = 7

def smallest_subarray_with_sum_at_least_k(nums: list, target: int) -> int:
    n = len(nums)
    left = 0
    min_len = float("inf")
    current_sum = 0

    for right in range(n):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0

# Call the function
print(smallest_subarray_with_sum_at_least_k(arr, k))
