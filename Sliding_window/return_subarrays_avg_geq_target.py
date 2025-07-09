"""
🔹 Problem: Return Subarrays of Size K with Average ≥ Target
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [2, 1, 3, 4, 1, 2, 1, 5]
k = 3
target_avg = 3

def subarrays_with_avg_greater_than_target(number:list, ws:int, ta:int) -> list:
    n = len(number)

    result = []
    cur_sum = sum(number[:k])

    cur_avg = cur_sum/k

    if cur_avg >= ta:
        n_sub_ar = number[:k]
        result.append(n_sub_ar)

    for i in range(k,n):
        cur_sum += number[i]
        cur_sum -= number[i-k]
        cur_avg = cur_sum/ws

        if cur_avg >= ta:
            result.append(number[i-k+1:i+1])
    return result
print(subarrays_with_avg_greater_than_target(arr,k,target_avg))
