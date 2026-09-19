class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS
        # T: O(V + E)
        # S: O(V + E)
        graph = {i: [] for i in range(numCourses)}
        inDegree = [0] * numCourses
        for cre, pre in prerequisites:
            graph[pre].append(cre)
            inDegree[cre] += 1

        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)

        done = 0
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            done += 1

            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1

                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return res if done == numCourses else []
