class Solution:
    def dfs(self,n1,n2,s):
        if s=="":
            return True
        n3=str(n1+n2)
        if s[0:len(n3)]==n3:
            return self.dfs(n2,int(n3),s[len(n3):])
        return False
        
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1,len(num)-1):
            n1=int(num[0:i])
            if str(n1)!=num[0:i]:
                    break
            for j in range(i+1,len(num)):
                n2=int(num[i:j])
                if str(n2)!=num[i:j]:
                    break
                if self.dfs(n1,n2,num[j:]):
                       return True
        return False
                    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def find_rec(self,n1,n2,s):
    #     if s=="":
    #         return True
    #     n3=str(n1+n2)
    #     if s[0:len(n3)]==n3:
    #         return self.find_rec(n2,int(n3),s[len(n3):])
    #     return False
    # def isAdditiveNumber(self, num: str) -> bool:
    #     n=len(num)
    #     for i in range(1,n-1):
    #         n1=int(num[0:i])
    #         if str(n1)!=num[0:i]:
    #             break
    #         for j in range(i+1,n):
    #             n2=int(num[i:j])
    #             if str(n2)!=num[i:j]:
    #                 break
    #             if self.find_rec(n1,n2,num[j:]):
    #                 return True
    #     return False

        
            
        
        