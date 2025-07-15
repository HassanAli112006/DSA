"""""""""""""""""""""""""""
🔹 Problem: Element Exists in Sorted Array  
🔁 Pattern: Binary Search (Classic)  
⭐ Difficulty: Easy  
📘 Custom Practice Problem  
🎯 Goal: Return True if target exists in sorted array, else False.  
🧠 Insight: Shrink the search space by comparing mid element with target.  
🛠️ Technique: Adjust left/right bounds based on mid comparison.
"""""""""""""""""""""""""""
nums = [5,7,7,8,8,10]
target = 8
# Output: [3, 4]



def first_and_last(number:list[int] , tr:int) ->list:

    def searchFisrt():
        l = 0
        r = len(number) -1
        first = -1
        while l<=r:
            m = l+(r-l)//2
            if number[m] == tr:
                first = m
                r = m-1
            elif number[m] <= tr:
                l = m+1
            else:
                r = m-1
        return first
    def searchLast():
        l = 0
        r = len(number) -1
        last = -1
        while l<=r:
            m = l+(r-l)//2
            if number[m] == tr:
                last = m
                l = m+1
            elif number[m] <= tr:
                l = m+1
            else:
                r = m-1
        return last
    return [searchFisrt(),searchLast()]
print(first_and_last(nums, target))