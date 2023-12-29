class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        res=[]
      
        for x in spells:
            
            l=0
            r=len(potions)-1
            index=len(potions)
            
            while l<=r:
                
                m=(l+r)//2
                if x *potions[m]>=success:
                    r=m-1
                    index=m
                else:
                    l=m+1
            res.append(len(potions)-index)
        return res
                
                
                
            
            
        
        
        
            
        
                
            
            
        
        
            
        
        
        
        
       
