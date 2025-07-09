"""
🔹 Problem: Count Subarrays with Average ≥ Target
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [2, 1, 3, 4, 1, 2, 1, 5]
k = 3
target_avg = 3
def subarrays_with_greater_than_target(numbers: list, ws:int, ta:float) ->int:
    n = len(numbers)
    count = 0
    cur_sum = sum(numbers[:ws])

    if cur_sum >= ta * ws:
        count += 1


    for i in range(ws,n):
        cur_sum += numbers[i]

        cur_sum -= numbers[i-ws]

        if cur_sum >= ta * ws:
            count += 1
    return count

print(subarrays_with_greater_than_target(arr,k,target_avg))
