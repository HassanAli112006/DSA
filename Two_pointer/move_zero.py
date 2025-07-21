"""""""""""""""""""""
🔹 Problem: Move Zeroes
🔁 Pattern: Two Pointers
⭐ Difficulty: Easy
📘 Source: https://leetcode.com/problems/move-zeroes/
🎯 Goal: Move all 0s to the end of the array while maintaining the relative order of non-zero elements. Do it in-place.
"""""""""""""""""""""

nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move_zero(number: list[int]) ->  list[int]:

    insert_pos = 0
    for r in range(len(number)):
        if number[r] != 0:
            number[insert_pos] = number[r]
            insert_pos += 1

    while insert_pos < len(number):
        number[insert_pos] = 0
        insert_pos+=1
    return number
print(move_zero(nums))



