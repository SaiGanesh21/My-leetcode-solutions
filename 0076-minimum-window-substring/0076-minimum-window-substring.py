class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""
        
        countt={}
        window={}
        
        res=[-1,-1]
        reslen=float("infinity")
        l=0
        
        for c in t:
            countt[c]=countt.get(c,0)+1
        have,need=0,len(countt)
        
        for r in range(len(s)):
            c=s[r]
            
            window[c]=window.get(c,0)+1
            
            if c in countt and window[c]==countt[c]:
                have+=1
            
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                    # pop from left of window
                window[s[l]]-=1
                if s[l] in countt and window[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
        l,r=res
          
        if reslen!=float("infinity"):
              return s[l:r+1] 
        else:
            return ""
        
    
        
        