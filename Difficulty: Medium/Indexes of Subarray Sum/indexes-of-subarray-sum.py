class Solution:
    def subarraySum(self, arr, target):
        j = 0
        curr_sum = 0

        for i in range(len(arr)):
            curr_sum += arr[i]

            while curr_sum > target:
                curr_sum -= arr[j]
                j += 1

            if curr_sum == target:
                return [j + 1, i + 1]

        return [-1]  
            
        
         
        