class Solution:
    def isValid(self, s: str) -> bool:
        d={")":"(", "]":"[", "}":"{"}
        stack=[]
        for x in s:
            if x not in d:
                stack.append(x)
            elif stack and stack[-1]==d[x]:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False
                    
                

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack=[]
        mapping={')':'(', '}':'{', ']':'['}
        for x in s:
            if x in mapping:
                if stack and stack[-1]==mapping[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return not stack
    
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for character in s:
            if character in mapping:
                if stack and stack[-1]==mapping[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return True if not stack else False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # stack = []
        # for char in s:
        #     if char == '(' or char == '{' or char == '[':
        #         stack.append(char)
        #     else:
        #         if not stack:
        #             return False
        #         if char == ')' and stack[-1] == '(':
        #             stack.pop()
        #         elif char == '}' and stack[-1] == '{':
        #             stack.pop()
        #         elif char == ']' and stack[-1] == '[':
        #             stack.pop()
        #         else:
        #             return False
        # return not stack