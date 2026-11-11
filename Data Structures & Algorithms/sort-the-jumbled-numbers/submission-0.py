class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def get_mapped_value(num: int) -> int:
            if num == 0:
                return mapping[0]
            
            mapped_val = 0
            place = 1
            while num > 0:
                num, digit = divmod(num, 10)
                mapped_val += mapping[digit] * place
                place *= 10
            return mapped_val

        # Sort based on the mapped value while preserving original relative order using index
        return [num for _, _, num in sorted((get_mapped_value(num), i, num) for i, num in enumerate(nums))]