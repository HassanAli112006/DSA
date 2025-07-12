"""""""""""""""""""""
🔹 Problem: Search Insert Position
🔁 Pattern: Binary Search
⭐ Difficulty: Easy-Medium
📘 Source: LeetCode #35 → https://leetcode.com/problems/search-insert-position/
🎯 Goal: Return the index where the target is found, or the index where it should be inserted to maintain the sorted order.
"""""""""""""""""""""
# nums = [1, 3, 5, 6]
# target = 5
# ➤ Output: 2

nums = [1, 3, 5, 6]
target = 2
# ➤ Output: 1

# nums = [1, 3, 5, 6]
# target = 7
# ➤ Output: 4

# nums = [1]
# target = 0
# ➤ Output: 0

def insert_position(number: list[int], tr: int) -> int:
    r = len(number) - 1
    l = 0

    while l <= r:
        m = l + (r-l)//2

        if number[m] == tr:
            return m
        elif number[m] < tr:
            l = m + 1
        else:
            r = m - 1
    return l
print(insert_position(nums, target))