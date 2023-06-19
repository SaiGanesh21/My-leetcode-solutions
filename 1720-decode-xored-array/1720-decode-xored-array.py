class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        hidden=[first]
        for i in range(len(encoded)):
            hidden.append(encoded[i]^first)
            temp=encoded[i]^first
            first=temp
        return hidden
    
    
        arr=[first]
        temp=0
        for i in encoded:
            temp=i^first
            arr.append(temp)
            first=temp
        return arr