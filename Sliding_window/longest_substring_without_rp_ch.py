"""
🔹 Problem: Longest Substring Without Repeating Characters
🔁 Pattern: Sliding Window (Variable Size)
⭐ Difficulty: Medium
📘 Source: LeetCode #3 (https://leetcode.com/problems/longest-substring-without-repeating-characters/)
🎯 Goal: Return the length of the longest substring with all unique characters.
"""
# Output: 3
# Explanation: The answer is "abc", which has length 3.



s = "abcabcbb"
def longest_unique_substring(string: str) -> int:
    max_len = 0
    seen = set()
    n = len(string)
    l = 0
    for r in range(n):
        while string[r] in seen:
            seen.remove(string[l])
            l += 1
        seen.add(string[r])
        max_len = max(max_len, r-l+1)
    return max_len
print(longest_unique_substring(s))



