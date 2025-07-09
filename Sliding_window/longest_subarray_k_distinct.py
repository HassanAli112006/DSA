"""
🔹 Problem: Longest Subarray with At Most K Distinct Elements
🔁 Pattern: Sliding Window (Variable Size)
⭐ Difficulty: Medium
📘 Source: Custom
"""

arr = [1, 2, 1, 2, 3]
k = 2

def longest_subarray_with_k(number: list, numberofelements: int) -> int:
    seen = {}
    n = len(number)
    l = 0
    max_length = 0
    for r in range(n):
        seen[number[r]] = seen.get(number[r], 0) + 1
        while len(seen) > numberofelements:
            seen[number[l]] -= 1
            if seen[number[l]] == 0:
                del seen[number[l]]
            l += 1
        length = r - l + 1
        max_length = max(max_length, length)
    return max_length

print(longest_subarray_with_k(arr, k))
