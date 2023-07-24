class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta=[0]*101
        for birth,death in logs:
            delta[birth-1950]+=1
            delta[death-1950]-=1
        
        year=0
        maxpopulation=0
        prefixsum=0
        for i in range(101):
            prefixsum+=delta[i]
            if prefixsum>maxpopulation:
                maxpopulation=prefixsum
                year=i+1950
        return year
            
        