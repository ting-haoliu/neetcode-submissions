class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS
        # T: O(V + E)
        # S: O(V + E)
        graph = {i: [] for i in range(numCourses)}
        inDegree = [0] * numCourses # number of pre for each courses
        for cre, pre in prerequisites:
            graph[pre].append(cre)
            inDegree[cre] += 1

        availableCourse = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                availableCourse.append(course)

        done = 0
        while availableCourse:
            course = availableCourse.popleft()
            done += 1

            for nextCourse in graph[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    availableCourse.append(nextCourse)

        return done == numCourses
