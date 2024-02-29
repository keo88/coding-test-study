class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 + n2)
            elif t == '-':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 - n2)
            elif t == '*':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 * n2)
            elif t == '/':
                n2 = stack.pop()
                n1 = stack.pop()
                if n1 * n2 < 0:
                    stack.append(ceil(n1 / n2))
                else:
                    stack.append(floor(n1 / n2))
            else:
                stack.append(int(t))
        return stack[0]
            

