class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS
        # T: O(V + E)
        # S: O(V + E)
        graph = {i: [] for i in range(numCourses)}
        for cre, pre in prerequisites:
            graph[pre].append(cre)

        visited = [0] * numCourses
        res = []

        def hasCycle(course: int) -> bool:
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1
            for nextCourse in graph[course]:
                if hasCycle(nextCourse):
                    return True
                
            visited[course] = 2
            res.append(course)
            return False

        for i in range(numCourses):
            if hasCycle(i):
                return []
        return res[::-1]
        