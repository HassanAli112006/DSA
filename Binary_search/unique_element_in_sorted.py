"""""""""""""""""""""""""""
🔹 Problem: Single Element in a Sorted Array
🔁 Pattern: Binary Search (Index Parity Trick)
⭐ Difficulty: Medium
📘 Source: LeetCode #540 → https://leetcode.com/problems/single-element-in-a-sorted-array/
🎯 Goal: Find the element that appears only once in a sorted array where all others appear exactly twice.
"""""""""""""""""""""""""""
# nums = [1,1,2,2,3,3,4,5,5]
# Output: 4

nums = [3,3,7,7,10,11,11]
# Output: 10

def single_element_in_array(number: list[int]) -> int:
    l = 0
    r = len(number) - 1
    while l <= r:
        m = l+(r-l)//2
        if len(number) == 1:
            return number[m]

        if m == 0 and number[m] != number[m+1]:
            return number[m]

        if m == len(number) -1 and number[m] != number[m-1]:
            return number[m]

        if number[m] != number[m+1] and number[m] != number[m-1]:
            return number[m]
        
        if m%2 == 0:
            if number[m] == number[m+1]:
                l = m+1
            else:
                r = m-1
        else:
            if number[m] == number[m-1]:
                l = m+1
            else:
                r = m-1
    return -1
print(single_element_in_array(nums))