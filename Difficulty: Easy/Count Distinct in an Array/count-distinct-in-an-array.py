class Solution:
    def countDistinct(self, arr):
        freq = {}

        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            
      
 
        
        return len(freq)