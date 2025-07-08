"""
🔹 Problem: Maximum Average Subarray of Size K
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

array = [1, 12, -5, -6, 50, 3]
number = 4
def max_avg(arr:int, k:int) -> float:
    n = len(arr)
    curr_sum = 0
    curr_sum = sum(arr[:k])
    max_avg = curr_sum/k

    for i in range(k,n):
        curr_sum += arr[i]
        curr_sum -= arr[i-k]
        avg = curr_sum/k

        max_avg = max(max_avg,avg)
    return max_avg
print(max_avg(array,number))
