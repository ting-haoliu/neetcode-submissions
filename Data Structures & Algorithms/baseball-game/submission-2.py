class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Stack
        # T: O(n)
        # S: O(n)
        stack = []

        for c in operations:
            if c == "+":
                stack.append(stack[-1] + stack[-2])
            elif c == "D":
                stack.append(stack[-1] * 2)
            elif c == "C":
                stack.pop()
            else:
                stack.append(int(c))

        return sum(stack)
        