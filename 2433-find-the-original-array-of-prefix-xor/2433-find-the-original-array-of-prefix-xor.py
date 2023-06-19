class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        original=[pref[0]]
        for i in range(len(pref)-1):
            original.append(pref[i]^pref[i+1])
        return original