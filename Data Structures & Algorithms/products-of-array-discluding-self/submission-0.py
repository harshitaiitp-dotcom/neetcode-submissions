class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range (n):
            product = 1
            for j in range (n):
                if i != j:
                    product*= nums[j]
            ans.append(product)
        return ans