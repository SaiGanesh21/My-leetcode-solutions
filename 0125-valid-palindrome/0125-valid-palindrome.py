class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
        
        #         left, right = 0, len(s) - 1
        # while left < right:
        #     if not s[left].isalnum():
        #         left += 1
        #     elif not s[right].isalnum():
        #         right -= 1
        #     elif s[left].lower() != s[right].lower():
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True