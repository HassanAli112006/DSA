"""""""""""""""""""""""""""
🧠 Problem: Sorted Two Sum (Two Sum II)
🔁 Pattern: Two Pointers (Start–End)
📘 LeetCode #167
🎯 Goal: Given a sorted array and a target, find the indices of the two numbers such that they add up to the target.
🔐 Constraint: Only one valid pair exists, and array is 1-indexed (LeetCode-specific).
"""""""""""""""""""""""""""



nums = [2, 7, 11, 15]
target = 9  
# Output: [1, 2]  # (2 + 7 = 9)

def two_sum(number: list[int], tr: int) -> int:
    l = 0
    r = len(number) - 1
    while l < r:
        if number[l] + number[r] == tr:
            return [l+1,r+1]
        elif number[l] + number[r] <= tr:
            l += 1
        else:
            r -= 1
    return [-1,-1]
print(two_sum(nums, target))