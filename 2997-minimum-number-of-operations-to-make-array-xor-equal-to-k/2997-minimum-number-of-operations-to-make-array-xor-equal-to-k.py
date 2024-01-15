class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
#         Commutivity : a^b == b^a
#         Associativity: (a^b)^c == a^(b^c)
#         Self-inverse : a^b^b == a

# In Python, the bit_count() function is used to count the number of set bits (bits with a value of 1) in a given integer. 


           # we are calculating the number of 1s
     # res = 0
     #    for num in nums:
     #        res ^= num
     #    return bin(res^k)[2:].count('1')
    
          nums.append(k)
          s=0
          for x in nums:
                s^=x
          print(s)
          return bin(s)[2:].count("1")
    
    
           # return bin(res^k)[2:].count('1')