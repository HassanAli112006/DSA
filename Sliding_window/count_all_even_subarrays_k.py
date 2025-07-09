"""
🔹 Problem: Count Subarrays with All Even Numbers
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [2, 4, 1, 6, 8, 10, 3, 12]
k = 3
def count_even_subarrays(number, ws):
    n = len(number)
    count = 0
    even_count = 0
    valid = False
    for i in range(ws):
        if arr[i] % 2 == 0:
            even_count += 1
    if even_count == ws:
        count += 1
    for i in range(k,n):
        if arr[i-ws] % 2 == 0:
            even_count -= 1
        if arr[i] % 2 == 0:
            even_count +=1
        if even_count == ws:
            count += 1

    return count
print(count_even_subarrays(arr,k))
