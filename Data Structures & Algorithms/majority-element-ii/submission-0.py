class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Step 1: Find potential candidates
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
        # Step 2: Verify the candidates
        result = []
        n = len(nums)
        
        # Count occurrences of candidates in the array
        if count1 > 0 and nums.count(cand1) > n // 3:
            result.append(cand1)
        if count2 > 0 and cand2 != cand1 and nums.count(cand2) > n // 3:
            result.append(cand2)
            
        return result