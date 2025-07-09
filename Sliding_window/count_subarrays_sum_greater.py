"""
🔹 Problem: Count Subarrays with Sum Greater Than Target
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [1, 3, 2, 6, 4, 1]
k = 3
targe = 8

def target(numbers:int,ws:int,tr:int) ->int:
    count = 0
    cur_sum = sum(numbers[:ws])
    n = len(numbers)
    if cur_sum>tr:
        count+=1
    for x in range(ws,n):
        cur_sum += numbers[x]
        cur_sum -= numbers[x-ws]

        if cur_sum > tr:
            count+=1
    return count

print(target(arr,k,targe))
