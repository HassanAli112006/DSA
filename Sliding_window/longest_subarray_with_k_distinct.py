# Longest Subarray With At Most K Distinct Elements
arr = [1, 2, 1, 2, 3]
k = 2

def longest_subarray_with_at_most_k_distinct(number: list, tr: int) -> int:
    max_length = 0
    l = 0
    freq = {}
    n = len(number)

    for r in range(n):
        freq[number[r]] = freq.get(number[r], 0) + 1

        while len(freq) > tr:
            freq[number[l]] -=1

            if freq[number[l]] == 0:
                del freq[number[l]]

            l += 1
        max_length = max(max_length, r-l+1)
    return max_length
print(longest_subarray_with_at_most_k_distinct(arr, k))