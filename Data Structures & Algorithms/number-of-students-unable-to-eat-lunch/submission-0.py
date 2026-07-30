class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # T: O(n)
        # S: O(1)
        res = len(students)
        bucket = [0, 0]
        for food in students:
            bucket[food] += 1

        for s in sandwiches:
            if bucket[s]:
                bucket[s] -= 1
                res -= 1
            else:
                break
        
        return res