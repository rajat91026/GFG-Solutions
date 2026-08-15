class Solution:
    def divisibleBy11(self, s: str) -> bool:
  
        odd = 0
        even = 0

        for i in range(len(s)):
            if i % 2 == 0:
                odd += int(s[i])
            else:
                even += int(s[i])

        return (odd - even) % 11 == 0
  
    # code here
    