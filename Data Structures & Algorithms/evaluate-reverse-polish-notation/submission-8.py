class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack
        # T: O(n)
        # S: O(n)
        stack = []
        operations = {"+", "-", "*", "/"}

        for c in tokens:
            if c in operations:
                b = stack.pop()
                a = stack.pop()

                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(c))
        
        return stack[0]
        