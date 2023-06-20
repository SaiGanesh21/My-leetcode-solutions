class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()

#         for x in arr:
#             d[bin(x)[2:].count("1")].append(x)
#         print(d)
#         l=[]
#         for k, v in d.items():
#             l.append(v)
              
            
        
        
        
        return sorted(arr, key=lambda x: x.bit_count())
    # return sorted(sorted(arr), key=lambda x: bin(x).count('1'))