"""""""""""""""""""""""""""""
🔽 Next Classic LeetCode Problem:
Problem: Two Sum
📘 Given:
An array of integers nums and an integer target.
🧪 Task:
Return indices of the two numbers such that they add up to target.
You may assume exactly one solution, and you may not use the same element twice.
"""""""""""""""""""""""""""""

nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1] because 2 + 7 = 9

def two_sum(number, tr):
    seen = {}
    l = 0
    for index, num in enumerate(number):
        difference = tr - num
        if difference in seen:
            return [seen[difference], index ]
        seen[num] = index
    return False
print(two_sum(nums, target))