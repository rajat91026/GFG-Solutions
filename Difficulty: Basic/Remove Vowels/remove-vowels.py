class Solution:
	def removeVowels(self, s):
	    ans =""
	    for ch in s:
	        if ch in 'aeiou':
	            continue
	        ans +=ch
	    return ans
	        
	    
		# code here
		