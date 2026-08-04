class Solution:
    def maximumFrequency(self, s):

        words = s.split()
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        ans = ""
        maxFreq = 0

        for word in words:
            if freq[word] > maxFreq:
                maxFreq = freq[word]
                ans = word

        return ans + " " + f"{maxFreq}"