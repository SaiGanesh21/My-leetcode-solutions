class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        
        Mindex=0
        Gindex=0
        Pindex=0
        time=0
        total=0
        for i in range(len(garbage)):
            for j in range(len(garbage[i])):
                  if garbage[i][j]=="M":
                           Mindex=i
                           
                  if garbage[i][j]=="G":
                           Gindex=i
                           
                  if garbage[i][j]=="P":
                       Pindex=i
                        
                  total+=1
                           
        for i in range(1,len(travel)):
                travel[i]+=travel[i-1]
                
        total+=travel[Mindex-1] if Mindex!=0 else 0
        total+=travel[Pindex-1] if Pindex!=0 else 0
        total+=travel[Gindex-1] if Gindex!=0 else 0
        return total
        
    
                
                
                
                           
                           
        
        
        
   