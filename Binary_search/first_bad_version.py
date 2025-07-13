"""""""""""""""""""""""""""
🔹 Problem: First Bad Version
🔁 Pattern: Binary Search (Boundary Finding)
⭐ Difficulty: Easy-Medium
📘 Source: LeetCode #278 → https://leetcode.com/problems/first-bad-version/
🎯 Goal: Find the first version that is bad using isBadVersion(version) API.
"""""""""""""""""""""""""""
n = 5
bad = 4

# Versions:  1  2   3  4   5
#           ✅ ✅ ✅ ❌ ❌

# Output → 4

def is_bad_version(version):
    return version >= bad
def first_bad_version(number: int) -> int:
    l = 1
    r = number
    bad_version = -1
    while l <= r:
        m = l + (r-l)//2
        if is_bad_version(m):
            bad_version = m
            r = m-1
        else:
            l = m+1
    return bad_version

print(first_bad_version(n))

