class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def ispossible(ranks,cars,mid):
            cars1=0
            for x in ranks:
                cars1+= int(sqrt(mid//x))
            return cars1>=cars
                
        
        
        
        l=1
        h=cars**2*(100)
        
        while l<=h:
            mid=(l+h)//2
            
            if ispossible(ranks,cars,mid):
                h=mid-1
            else:
                l=mid+1
        return l
            
            
        
        
        
        
        
        
            