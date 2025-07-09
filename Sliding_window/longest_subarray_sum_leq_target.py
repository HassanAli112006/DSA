"""
🔹 Problem: Longest Subarray with Sum ≤ Target
🔁 Pattern: Sliding Window (Variable Size)
⭐ Difficulty: Medium
📘 Source: Custom
"""

arr = [1, 2, 1, 0, 1, 1, 0]
target = 4
def longest_subarray_with_sum_leq_target(number: list, tr: int) -> int:
    n = len(number)
    l = 0
    max_length = 0
    cur_sum = 0
    for r in range(n):
        cur_sum += number[r]
        while cur_sum > tr:
            cur_sum -= number[l]
            length = r-l+1
            max_length = max(max_length, length)
            l += 1
    return max_length
print(longest_subarray_with_sum_leq_target(arr, target))
