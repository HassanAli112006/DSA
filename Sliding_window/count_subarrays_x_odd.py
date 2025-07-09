"""
🔹 Problem: Count Subarrays with Exactly X Odd Numbers
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [1, 2, 3, 4, 5, 6]
k = 3
x = 2

def number_of_subarrays(number: list, ws: int, tr: int) -> int:
    odd_count = 0
    count = 0
    n = len(number)

    for i in range(ws):
        if number[i] % 2 != 0:
            odd_count += 1
    if odd_count == tr:
        count += 1
    for i in range(ws,n):
        if number[i - ws] % 2 != 0:
            odd_count -= 1
        if number[i] % 2 != 0:
            odd_count +=1
        if odd_count == tr:
            count += 1
    return count

print(number_of_subarrays(arr,k,x))
