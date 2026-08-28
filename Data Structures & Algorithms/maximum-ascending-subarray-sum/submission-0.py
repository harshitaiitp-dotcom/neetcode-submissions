class Solution:
    def maxAscendingSum(self, nums):
        n = len(nums)
        answer = 0
        for start in range(n):
            current_sum = nums[start]
            answer = max(answer, current_sum)
            for end in range(start + 1, n):
                if nums[end] > nums[end - 1]:
                    current_sum += nums[end]
                    answer = max(answer, current_sum)
                else:
                    break
        return answer