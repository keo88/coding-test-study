class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')
        for p in paths:
            if not p or p == '.':
                continue
            elif p == '..':
                if len(stack):
                    stack.pop()
            else:
                stack.append(p)
        
        return '/' + '/'.join(stack)
