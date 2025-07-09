"""
🔹 Problem: Smallest Subarray with Sum ≥ Target
🔁 Pattern: Sliding Window (Variable Size)
⭐ Difficulty: Medium
📘 Source: Custom
"""

arr = [2, 3, 1, 2, 4, 3]
target = 7

def smallest_subarray(number: list, tr: int) -> int:
    n = len(number)
    l = 0
    min_length = float('inf')
    cur_sum =  0

    for r in range(n):
        cur_sum += number[r]

        while cur_sum >= tr:
            length = r - l + 1
            min_length = min(min_length, length)
            cur_sum -= number[l]
            l += 1

    return min_length if min_length != float('inf') else 0

print(smallest_subarray(arr, target))
