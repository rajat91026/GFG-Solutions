class Solution:
    def transitionPoint(self, arr): 
        # Code here
        low  = 0
        high = len(arr)-1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] ==1:
                ans =  mid
                high = mid -1
            else:
                low = mid +1
        return ans