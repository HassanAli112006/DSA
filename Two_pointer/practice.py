""""""""""""""""""""""""""""
🧠 Problem: Remove Duplicates from Sorted Array
🔁 Pattern: Two Pointers (Slow–Fast)
📘 LeetCode #26
🎯 Goal: Remove the duplicates in-place from a sorted array, and return the number of unique elements.
"""""""""""""""""""""""""""""

# nums = [1, 1, 2]
# # Output: 2, nums = [1, 2, _]

# def remove_duplicates(number: list[int]) -> int:
#     unique = 0
#     unique_count = 0
#     for next in range(1,len(number)):
#         if number[unique] != number[next]:
#             unique += 1
#             number[unique] = number[next]
#             unique_count = unique


#     # while unique < len(number)-1:
#     #     number[unique+1] = '_'
#     #     unique += 1
#     return unique+1 , number[:unique+1]
# print(remove_duplicates(nums))
""""""""""""""""""""""
🧠 Problem: Move Zeroes
🔁 Pattern: Two Pointers (Slow–Fast)
📘 LeetCode #283
🎯 Goal: Move all 0s to the end while maintaining order of non-zero elements — in-place.
"""""""""""""""""""""""

# nums = [0, 1, 0, 3, 12]
# # Output: [1, 3, 12, 0, 0]

# def move_zero(number: list[int]) -> list:
#     insert_index = 0

#     for next_non_zero in range(len(number)):
#         if number[next_non_zero] != 0:
#             number[insert_index] = number[next_non_zero]
#             insert_index += 1
#     while insert_index < len(number):
#         number[insert_index] = 0
#         insert_index += 1

#     return number
# print(move_zero(nums))


# insert_index = 3
"""""""""""""""""""""""""""
🧩 Reverse String
Problem:
Write a function that reverses a list of characters in-place.
"""""""""""""""""""""""""""


# s = ["h","e","l","l","o"]
# # Output: ["o","l","l","e","h"]

# def reverse_string(word: list[str]) -> list[str]:
#     left = 0
#     right = len(word) - 1
#     while left < right:
#         word[left], word[right] = word[right], word[left]
#         left += 1
#         right -= 1
#     return word
# print(reverse_string(s))
"""""""""""""""""""""""
🧠 Problem: Squares of a Sorted Array
🔁 Pattern: Two Pointers (Start–End Comparison)
📘 LeetCode #977
📝 Given:
A sorted array nums (may contain negative numbers).
🎯 Goal:
Return an array of squares of each number sorted in non-decreasing order.
"""""""""""""""""""""""

nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]

def square_of_sorted_array(number: list[int]) -> list[int]:
    left = 0
    right = len(number) - 1
    result = []
    while left <= right:
        if abs(number[left]) > abs(number[right]):
            result.append(number[left]**2)
            left += 1
        else:
            result.append(number[right]**2)
            right -= 1
    l = 0
    r = len(number) - 1
    while l<r:
        result[l] , result[r] = result[r] , result[l]

        l += 1
        r -=1
    return result
print(square_of_sorted_array(nums))

