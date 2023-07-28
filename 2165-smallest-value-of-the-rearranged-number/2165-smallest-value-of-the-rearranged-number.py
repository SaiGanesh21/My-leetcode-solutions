class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
                s=str(abs(num))
                s=list(s)
                s=sorted(s,reverse=True)
                return int("-"+"".join(s))
        else:
            s=str(num)
            s=list(s)
            s.sort()
            if "0" in s:
                c=s.count("0")
                s=s[c:c+1]+["0"]*c+s[c+1:]
                print(s)
            s1=int("".join(s))
            return s1
