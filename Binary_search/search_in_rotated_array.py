"""""""""""""""""""""
🔹 Problem: Search in Rotated Sorted Array
🔁 Pattern: Binary Search (Two Phases or Smart One-Pass)
⭐ Difficulty: Medium
📘 Source: LeetCode #33 → https://leetcode.com/problems/search-in-rotated-sorted-array/
🎯 Goal: Search for a target in a rotated sorted array and return its index. Return -1 if not found.
"""""""""""""""""""""

nums = [4,5,6,7,0,1,2]
target = 0
# Output: 4

# nums = [4,5,6,7,0,1,2]
# target = 3
# Output: -1

# nums = [1]
# target = 0
# Output: -1

def search_in_sorted_array(number: list, tr: int) -> int:
    l = 0
    r = len(number) - 1
    while l <= r:
        m = l + (r-l)//2

        if number[m] == tr:
            return m

        elif number[l] <= number[m]:
            if number[l] <= tr < number[m]:
                r = m - 1
            else:
                l = m + 1

        else:
            if number[m] < tr <= number[r]:
                l = m + 1
            else:
                r = m - 1

    return -1
print(search_in_sorted_array(nums, target))

