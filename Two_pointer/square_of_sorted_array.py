"""""""""""""""""
🔹 Problem: Squares of a Sorted Array
🔁 Pattern: Two Pointers
⭐ Difficulty: Easy
📘 Source: LeetCode #977 → https://leetcode.com/problems/squares-of-a-sorted-array/
🎯 Goal: Return a new array of the squares of each number from the input, sorted in non-decreasing order.
"""""""""""""""""

nums = [-7, -3, 2, 3, 11]
# output: [4, 9, 9, 49, 121]


def sortedSquare(number: list[int]) -> list[int]:
    l = 0
    r = len(number) - 1
    result = []
    while l<=r:
        if abs(number[l]) < abs(number[r]):
            result.append(number[r] ** 2)
            r-=1
        else:
            result.append(number[l] ** 2)
            l+=1
    result.reverse()
    return result
print(sortedSquare(nums))
