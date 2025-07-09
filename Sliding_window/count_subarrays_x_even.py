"""
🔹 Problem: Count Subarrays with Exactly X Even Numbers
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [2, 4, 1, 6, 8, 10, 3, 12]
k = 3
x = 2

def count_subarrays_with_x_evens(number: list, ws: int, tr: int) -> int:
    count = 0
    even_count = 0
    n = len(number)

    for i in range(ws):
        if number[i] %  2 == 0:
            even_count += 1
    if even_count == tr:
        count += 1

    for i in range(ws,n):
        if number[i-ws] % 2 == 0:
            even_count -=1
        if number[i] % 2 == 0:
            even_count +=1
        if even_count == tr:
            count += 1
    return count
print(count_subarrays_with_x_evens(arr,k,x))
