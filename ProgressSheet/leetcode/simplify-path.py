class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        strs = path.split("/")
        
        for char in strs:
            if char == "..":
                if stack:
                    stack.pop()
            elif char == "." or char == "":
                continue
            else:
                stack.append(char)

        return "/"+"/".join(stack)