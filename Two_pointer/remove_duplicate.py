"""""""""""""""""""""
🔹 Problem: Remove Duplicates from Sorted Array
🔁 Pattern: Two Pointers
⭐ Difficulty: Easy
📘 Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
🎯 Goal: Remove duplicates in-place from a sorted array and return the number of unique elements.
"""""""""""""""""""""


nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5
# Modified nums = [0,1,2,3,4,_,_,_,_,_]  # `_` means we don't care what's there

def remove_duplicates(number:list[int]) -> int:
    # tracks the unique element's index
    unique = 0

    # iterate through the list to find the next unique element
    for next in range(len(number)):
        # We don't care about the case where the unique and next elements are same so we ignore that case
        if number[unique] != number[next]:
            # since we want to store next unique at the next index than the previous we do [unique+1]
            number[unique+1] = number[next]
            unique+=1
    # just in case we need to fill the rest of list
    # unique += 1

    # In actual leetcode problem you don't need to fill the rest of array
    # while unique < len(number):
    #     number[unique] = '_'
    #     unique+=1
    # we return unique +1 because list start from 0 index
    return unique+1
print(remove_duplicates(nums))

