"""
🔹 Problem: Count Subarrays with All Even Numbers (Brute Force)
🔁 Pattern: Sliding Window (Fixed Size)
⭐ Difficulty: Easy
📘 Source: Custom
"""

arr = [2, 4, 1, 6, 8, 10, 3, 12]
k = 3

def count_even_subarrays(number, ws):
    n = len(number)
    count = 0
    true_count = 0
    valid = False

    # First window check
    sub_array = number[:ws]
    for x in sub_array:
        if x % 2 == 0:
            true_count += 1
        if true_count == ws:
            valid = True
    if valid:
        count += 1

    # Sliding window (brute-force rechecking)
    for i in range(1, n - ws + 1):
        true_count = 0
        valid = False
        sub_array = number[i:i + ws]
        for x in sub_array:
            if x % 2 == 0:
                true_count += 1
            if true_count == ws:
                valid = True
        if valid:
            count += 1

    return count

print(count_even_subarrays(arr, k))
