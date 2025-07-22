# 🔹 Problem: Move Zeroes  
# 🔁 Pattern: Two Pointers  
# ⭐ Difficulty: Easy  
# 📘 Source: https://leetcode.com/problems/move-zeroes/  
# 🎯 Goal: Move all 0s to the end of the array while maintaining the relative order of the non-zero elements.

nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move_zeros(number: list[int]):
    insert_position = 0

    for R in range(len(number)):
        if number[R] != 0:
            number[insert_position] = number[R]
            insert_position += 1
    while insert_position < len(number):
        number[insert_position] = 0
        insert_position += 1
    return number
print(move_zeros(nums))


