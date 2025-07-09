"""
🔹 Problem: Maximum Sum of Subarray of Size K (All Positive)
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [1, -1, 3, 4, 5, -2, 6, 1]
k = 3

def max_sum_of_positive_numbers(number: list, ws: int) -> int:
    n = len(number)
    positive_count = 0
    max_sum = 0

    for i in range(ws):
        if number[i] > 0:
            positive_count += 1
    if positive_count == ws:
        cur_sum = sum(number[:ws])
        max_sum = cur_sum

    for i in range(ws,n):
        if number[i-ws] > 0:
            positive_count -= 1
        if number[i] > 0:
            positive_count += 1
        if positive_count == ws:
            cur_sum = sum(number[i-ws+1:i+1])
            max_sum = max(max_sum, cur_sum)
    return max_sum
print(max_sum_of_positive_numbers(arr,k))
