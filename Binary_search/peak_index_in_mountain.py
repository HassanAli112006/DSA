"""""""""""""""""""""""""""
🔹 Problem: Peak Index in a Mountain Array
🔁 Pattern: Binary Search (Peak Finding)
⭐ Difficulty: Easy-Medium
📘 Source: LeetCode #852 → https://leetcode.com/problems/peak-index-in-a-mountain-array/
🎯 Goal: Given a mountain array, return the index of the peak element.
"""""""""""""""""""""""""""

arr = [0, 2, 4, 7, 6, 3, 1]
# Output: 3 Because arr[3] = 7 is the peak

def peak_index_in_mountain_array(number: list[int]) -> int:
    l = 0
    r = len(number) - 1

    while l < r:
        m = l + (r-l)//2

        if number[m] > number[m+1]:
            r = m
        else:
            l = m+1
    return r
print(peak_index_in_mountain_array(arr))