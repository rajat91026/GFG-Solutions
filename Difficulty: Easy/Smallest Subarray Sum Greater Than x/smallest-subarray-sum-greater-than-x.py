class Solution:
    def smallestSubWithSum(self, x, arr):
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(arr)):
            current_sum += arr[right]

            while current_sum > x:
                min_len = min(min_len, right - left + 1)
                current_sum -= arr[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
     