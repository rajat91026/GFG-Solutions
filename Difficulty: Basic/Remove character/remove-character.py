class Solution:
    def removeChars (ob, str1, str2):
        ans= ""
        for i in range(len(str1)):
            if str1[i] not in str2:
                ans+=str1[i]
        return ans
        # code here 
        