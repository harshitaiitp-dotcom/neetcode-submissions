from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings
        str_nums = list(map(str, nums))
        
        # Custom comparator: if a + b > b + a, then a should come before b
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
                
        # Sort the strings using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers into a single string
        result = "".join(str_nums)
        
        # Edge case: if the result starts with '0', the only possible answer is '0'
        return "0" if result[0] == "0" else result
        