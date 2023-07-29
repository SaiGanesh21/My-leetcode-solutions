class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
            s1=set()
            s2=set()
            for i in range(len(s)-9):
                p=s[i:i+10]
                if p in s1:
                    s2.add(p)
                if p not in s1:
                    s1.add(p)
            return s2
                    
                
            
                