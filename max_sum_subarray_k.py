"""
🔹 Problem: Maximum Sum Subarray of Size K
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [3, -1, 4, 12, -8, 5, 6]
k = 4

def max_sum(num:int, k:int) -> int:
    n = len(num)
    if n<k:
        return -1
    cut_sum = sum(num[:k])
    max_sum = cut_sum

    for x in range(k,n):
        cut_sum += num[x]
        cut_sum -= num[x-k]

        max_sum = max(max_sum,cut_sum)
    return max_sum

print(max_sum(arr,k))
