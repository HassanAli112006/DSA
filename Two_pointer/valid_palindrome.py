""""""""""""""""""""""
Problem: Valid Palindrome
📘 Given:
A string s, which may contain letters, digits, symbols, and spaces.
🧪 Task:
Return True if s is a palindrome, ignoring non-alphanumeric characters and case. Otherwise, return False.
"""""""""""""""""""""""

# s = "A man, a plan, a canal: Panama"
# Output: True

s = "race a car"
# Output: False

def isPalindrome(line: str) -> bool:
    l = 0
    r = len(line)-1
    while l<r:
        if not line[l].isalnum():
            l+=1
            continue
        if not line[r].isalnum():
            r-=1
            continue
        if line[l].lower() != line[r].lower():
            return False
        l+=1
        r-=1
    return True
print(isPalindrome(s))




