class Solution:
    def factorialNumbers(self, n):
        ans = []
        fact = 1

        for i in range(1, n + 1):
            fact = fact * i

            if fact <= n:
                ans.append(fact)
            else:
                break

        return ans
        