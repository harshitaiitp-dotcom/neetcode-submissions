class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        target = skill[left] + skill[right]
        chemistry = 0

        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry