class Solution:
    def findDuplicates(self, arr):
        freq ={}
        for num in arr:
            freq[num] = freq.get(num,0)+1
        ans =[]
        for key in freq:
            if freq[key] == 2:
                ans.append(key)
        return ans     
        
        
        