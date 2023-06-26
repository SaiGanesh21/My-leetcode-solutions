class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minsofar=prices[0]
        for price in prices:
            minsofar=min(minsofar,price)
            profit=price-minsofar
            maxprofit=max(maxprofit,profit)
        return maxprofit
        
  
        
        
        
        
        
        
        
        
        
        

    
        
            
              
        
       
        