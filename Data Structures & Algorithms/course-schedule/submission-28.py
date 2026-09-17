class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        # T: O(V + E)
        # S: O(V + E)
        graph = {i: [] for i in range(numCourses)}
        for cre, pre in prerequisites:
            graph[pre].append(cre)

        visited = [0] * numCourses

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
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True
