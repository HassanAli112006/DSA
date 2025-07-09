"""
🔹 Problem: Smallest Subarray with Sum ≥ Target
🔁 Pattern: Sliding Window (Variable Size)
⭐ Difficulty: Medium
📘 Source: Leetcode 209 (Modified)
"""
arr = [2, 3, 1, 2, 4, 3]
target = 7

def smallest_subarray_with_sum_greater(number: list, tr: int) -> int:
    n = len(number)
    minimum_length = float("inf")
    l = 0
    cur_sum = 0
    for r in range(n):
        cur_sum += number[r]
        while cur_sum >= tr:
            cur_sum -= number[l]
            length = r-l+1
            minimum_length = min(minimum_length , length)
            l += 1
    return minimum_length if minimum_length is not float("inf") else 0
print(smallest_subarray_with_sum_greater(arr, target))