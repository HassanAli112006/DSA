"""""""""""""""""""""""""""""""""
🔹 Problem: Longest Substring Without Repeating Characters
🔁 Pattern: Sliding Window (with Two Pointers)
⭐ Difficulty: Medium
📘 Source: LeetCode #3
🎯 Goal: Find the length of the longest substring in a given string that contains no repeating characters.
"""""""""""""""""""""""""""""""""

s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with length 3.

def len_of_longest_substring(word: str) -> int:
    # tracks duplicate
    seen = set()
    l = 0
    longest_length = 0
    # to mark where the longest begins
    max_start_index = 0
    for r in range(len(word)):
        # First addressess the false case
        while word[r] in seen:
            seen.remove(word[l])
            l += 1
        # Below operation gets performed first from the above one which tracks the false case
        seen.add(word[r])
        # added an if check so that it does not get overriden every time until the last iteration
        # we only want the longest and start_index to be assigned when we have the largest possible window
        if r-l+1>longest_length:
            longest_length = max(longest_length, r-l+1)
            max_start_index = l
            # the word[start_index:start_index+longest_length] is returns the actual value of window instead of just returning length
    return longest_length, word[max_start_index:max_start_index + longest_length]

print(len_of_longest_substring(s))
