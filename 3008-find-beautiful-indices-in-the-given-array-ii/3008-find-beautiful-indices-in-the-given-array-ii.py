class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # copied from contest
        # KMP
        def partial(s):
            g, pi = 0, [0] * len(s)
            for i in range(1, len(s)):
                while g and (s[g] != s[i]):
                    g = pi[g - 1]
                pi[i] = g = g + (s[g] == s[i])

            return pi


        def match(s, pat):
            pi = partial(pat)

            g, idx = 0, []
            for i in range(len(s)):
                while g and pat[g] != s[i]:
                    g = pi[g - 1]
                g += pat[g] == s[i]
                if g == len(pi):
                    idx.append(i + 1 - g)
                    g = pi[g - 1]

            return idx
        
        i1 = match(s, a)
        i2 = match(s, b)
        i1.sort()
        i2.sort()
        
        ans = []
        for i in i1:
            good = False
            l = bisect_left(i2, i)
            r = bisect_right(i2, i) - 1
            if 0 <= l < len(i2) and abs(i - i2[l]) <= k:
                good = True
            if 0 <= r < len(i2) and abs(i - i2[r]) <= k:
                good = True
            if good:
                ans.append(i)
        
        return ans