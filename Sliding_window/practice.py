"""""""""""""""""
You are given an array of integers nums and an integer k.
Find the maximum sum of any contiguous subarray of size k.
"""""""""""""""""

# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: The subarray [5, 1, 3] has the maximum sum = 9.

nums = [2, 1, 5, 1, 3, 2]
k = 3


def max_sum_of_number(number:list[int], target: int) ->int:
    l = 0
    max_sum= 0
    cur_sum = 0
    for r in range(len(number)):
        cur_sum += number[r]
        # max_sum = max(cur_sum, max_sum)
        while r-l+1 > target:
            cur_sum -= number[l]
            l+=1
        if r-l+1 == target:
            max_sum = max(cur_sum, max_sum)
    return max_sum
print(max_sum_of_number(nums, k))