"""""""""""""""""
🔹 Problem: Reverse String
🔁 Pattern: Two Pointers
⭐ Difficulty: Easy
📘 Source: LeetCode #344 → https://leetcode.com/problems/reverse-string/
🎯 Goal: Reverse the characters of the input array in-place using O(1) extra memory.
"""""""""""""""""


s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]

def reverse_string(array):
    l = 0
    r = len(array) - 1
    while l <= r:
        array[l], array[r] = array[r], array[l]

        l += 1
        r -= 1
    return array
print(reverse_string(s))
