class Solution:
    def nonRepeatingChar(self,s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for x in s:
            if freq[x] == 1:
                return x
        return '$'
    
        #code here
    
    