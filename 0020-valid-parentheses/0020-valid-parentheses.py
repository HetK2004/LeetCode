class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        a = 0
        for c in s:
            if c == '(' or c == '[' or c == '{' :
                stack.append(c)
            elif (c == ')' or c == ']' or c == '}') :
                if len(stack) == 0:
                    return False
                elif c == ')' and stack[-1] == '(' :
                    stack.pop()
                elif c == ']' and stack[-1] == '[' :
                    stack.pop()
                elif c == '}' and stack[-1] == '{' :
                    stack.pop()
                else :
                    return False

        if len(stack) == 0 :
            return True
        else:
            return False