class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        print(shifts)
        l=[]
        for i in range(len(s)):
            index=((ord(s[i])-ord("a"))+shifts[i])%26
            l.append(chr(index+97))
        return "".join(l)
            
            