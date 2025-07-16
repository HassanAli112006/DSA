"""""""""""""""""""""""""""
🔹 Problem: Koko Eating Bananas
🔁 Pattern: Binary Search on Answer
⭐ Difficulty: Medium
📘 Source: Leetcode #875 → https://leetcode.com/problems/koko-eating-bananas/
🎯 Goal: Find the minimum eating speed (k) such that Koko can finish all banana piles in `h` hours.
"""""""""""""""""""""""""""
# piles_of_bananas = [3, 6, 7, 11]
# h = 8
# Output: 4

# piles_of_bananas = [30,11,23,4,20]
# h = 5
# Output: 30

# piles_of_bananas = [30,11,23,4,20]
# h = 6
# Output: 23

piles_of_bananas = [1_000_000_000]
h = 2
# Output: 500000000
import math
def minimum_eating_speed(pile:list, target_hours:int) -> int:
    def findHour(hr):
        hour =  0
        for i in pile:
            hour += math.ceil(i/hr)
        return hour
    l = 1
    r = max(pile)
    while l <= r:
        m = l + (r-l)//2
        required_hour = findHour(m)
        if required_hour <= target_hours: #can be a smaller number in range
            r = m-1 #move left
        else:
            l = m+1 #move right
    return l

print(minimum_eating_speed(piles_of_bananas, h))



