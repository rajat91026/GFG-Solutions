class Solution:
    def removeSpaces(self, s):
        arr = list(s)
        j = 0
        for i in range(len(arr)):
            if arr[i]!=' ':
                arr[j]=arr[i]
                j+=1
        return ''.join(arr[:j])
        
        