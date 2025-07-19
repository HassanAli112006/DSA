# nums = [1,3,5,6]
# target = 5
# Output: 2

nums = [1,3,5,6]
target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7  
# Output: 4

def index(number: list, tr: int) -> int:
    l = 0
    r = len(number) - 1
    while l<=r:
        m = l + (r-l)//2
        if number[m] == tr:
            return m
        elif number[m] <= tr:
            l = m + 1
        else:
            r = m - 1
    return l
print(index(nums, target))