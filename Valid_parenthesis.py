class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map.values():  # Opening brackets
                stack.append(char)
            elif char in bracket_map:  # Closing brackets
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()  # Remove matched opening bracket
        
        return len(stack) == 0  # True if stack is empty


#example usage 
sol = Solution()
print(sol.isValid("()"))       
print(sol.isValid("()[]{}"))   
print(sol.isValid("(]"))      
print(sol.isValid("([])"))   