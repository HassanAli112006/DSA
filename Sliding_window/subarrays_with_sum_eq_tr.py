"""
🔹 Problem: Count Subarrays With Sum Exactly Equal to K
🔁 Pattern: Sliding Window (Variable Size)
⭐ Difficulty: Medium-Hard
📘 Source: LeetCode #560 (https://leetcode.com/problems/subarray-sum-equals-k/)
🎯 Goal: Count the number of subarrays whose sum is exactly equal to the target K.
"""
# Output: 2
# Explanation: [1,1] appears twice


arr = [1, 1, 1]
k = 2

def count_subarrays_with_sum_eq_tr(number: list, tr: int) -> int:
    n = len(number)
    l = 0
    count = 0
    cur_sum = 0
    for r in range(n):
        cur_sum += number[r]
        while cur_sum != tr:
            cur_sum -= number[l]
            l += 1
        if cur_sum == tr:
            count += 1
    return count
print(count_subarrays_with_sum_eq_tr(arr,k))
