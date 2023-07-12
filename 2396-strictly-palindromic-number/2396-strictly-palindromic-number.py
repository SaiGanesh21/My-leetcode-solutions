class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def palindrome(i,n):
            l=[]
            while n>0:
                l.append(n%2)
                n=n//i
            
        for i in range(2,n-2+1):
            if not palindrome(i,n):
                return False
        return True