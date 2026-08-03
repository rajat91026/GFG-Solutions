class Solution:
    def armstrongNumber (self, n):
        temp = n
        sum = 0
        while temp > 0:
            digits = temp%10
            sum+=digits**3
            temp//=10
        return sum == n
        # code here 
        