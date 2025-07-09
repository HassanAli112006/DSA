"""
🔹 Problem: Maximum of All Subarrays of Size K  
🔁 Pattern: Sliding Window (Fixed Size)  
⭐ Difficulty: Easy  
📘 Source: Custom  
🎯 Goal: Return a list of the maximum elements from all subarrays of size K.
"""

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

def max_of_subarrays(nums: list, window_size: int) -> list:
    n = len(nums)
    result = []

    for i in range(n - window_size + 1):
        window = nums[i:i + window_size]
        max_value = max(window)
        result.append(max_value)

    return result

print(max_of_subarrays(arr, k))
