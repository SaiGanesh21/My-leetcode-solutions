class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        output=[]
        sfreq=[0]*26
        pfreq=[0]*26
        
        for i in range(len(p)):
            sfreq[ord(s[i])-ord("a")]+=1
            pfreq[ord(p[i])-ord("a")]+=1
        if sfreq==pfreq:
            output.append(0)
        for i in range(len(p),len(s)):
            sfreq[ord(s[i-len(p)])-ord("a")]-=1
            sfreq[ord(s[i])-ord("a")]+=1
            
            if sfreq==pfreq:
                    output.append(i-len(p)+1)
        return output
            
            
            
            
        
        
       
                    
            
        
        
