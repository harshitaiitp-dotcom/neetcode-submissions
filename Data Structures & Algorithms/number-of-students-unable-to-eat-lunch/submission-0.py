class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        counts = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
        return counts[0] + counts[1]