"""""""""""""""""""""""""""
🔹 Problem: Find First and Last Position of Element in Sorted Array
🔁 Pattern: Binary Search (Modified)
⭐ Difficulty: Medium
📘 Source: LeetCode #34 (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
🎯 Goal: Given a sorted array, find the first and last position of a given target value.
"""""""""""""""""""""""""""

nums = [5,7,7,8,8,10]
target = 8
# Output: [3, 4]

def searchRange(number: list[int], tr: int) -> list[int]:
    if len(number) == 0: #emtpy list as input
        return [-1,-1]
    #create two seperate functions for finding first and last occurance

    #first occurance
    def firstSearch():
        l = 0
        r = len(number) - 1
        first = -1
        while l <= r:
            m = l + (r-l)//2
            if tr == number[m]:
                first = m
                r = m - 1
            elif tr < number[m]:
                r = m - 1
            else:
                l = m + 1
        return first


    #last occurance
    def lastSearch():
        l = 0
        r = len(number) - 1
        last = -1
        while l <= r:
            m = l + (r-l)//2
            if number[m] == tr:
                last = m
                l = m + 1
            elif number[m] < tr:
                l = m + 1
            else:
                r = m - 1
        return last
    return [firstSearch(), lastSearch()]

print(searchRange(nums, target))
