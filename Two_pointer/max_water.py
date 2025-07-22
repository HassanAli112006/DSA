# 🔁 Pattern: Two Pointers
# ⭐ Difficulty: Medium
# 📘 Source: https://leetcode.com/problems/container-with-most-water
# 🎯 Goal: Given an array of heights, find the maximum area of water a container can store. The container is formed by two lines (array indices) and the x-axis.


height = [1,8,6,2,5,4,8,3,7]
# Output: 49

def max_water(height: list[int]) -> int:
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        width = r - l
        area = width * min(height[l], height[r])
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
print(max_water(height))

