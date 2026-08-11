class Solution:
    def winner(self, arr):
        count = {}

        
        for name in arr:
            count[name] = count.get(name, 0) + 1

        winner_name = ""
        max_votes = 0

    
        for name in count:
            if count[name] > max_votes:
                max_votes = count[name]
                winner_name = name

            elif count[name] == max_votes and name < winner_name:
                winner_name = name

        return [winner_name, max_votes]