class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty hash map (dictionary)
        # It will store {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate what number we need to find
            complement = target - num
            
            # Check if that number is already in our hash map
            if complement in seen:
                return [seen[complement], i]
            # If not found, add the current number and its index to the map
            seen[num] = i