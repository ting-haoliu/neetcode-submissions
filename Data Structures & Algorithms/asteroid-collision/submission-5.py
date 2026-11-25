class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Stack
        # T: O(n)
        # S: O(1)
        stack = []

        for ast in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and ast < 0:
                diff = stack[-1] + ast

                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(ast)
        return stack
