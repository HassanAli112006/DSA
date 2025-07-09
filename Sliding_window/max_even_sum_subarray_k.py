"""
🔹 Problem: Maximum Even Sum in Any Subarray of Size K
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [2, 4, 1, 6, 3, 5]
k = 3

def max_even_sum(number: list, ws: int) -> int:
    n = len(number)
    max_sum = None
    cur_sum = sum(number[:ws])
    if cur_sum % 2 == 0:
        max_sum = cur_sum
    for i in range(ws, n):
        cur_sum -= number[i - ws]
        cur_sum += number[i]
        if cur_sum % 2 == 0:
            max_sum = cur_sum
    return max_sum if max_sum is not None else -1

print(max_even_sum(arr,k))
