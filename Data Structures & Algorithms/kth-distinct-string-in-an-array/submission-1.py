class Solution:
    def kthDistinct(self, arr, k):
        distinct_count = 0
        for word in arr:
            if arr.count(word) == 1:
                distinct_count += 1
                if distinct_count == k:
                    return word
        return ""