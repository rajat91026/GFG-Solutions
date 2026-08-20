class Solution:
    def maxOnes(self, arr, k):
        ans =0
        left = 0
        freq ={}
        n = len(arr)
        for right in range(n):
            freq[arr[right]] =freq.get(arr[right],0)+1
            while freq.get(0,0)>k:
                freq[arr[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans